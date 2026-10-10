require 'minitest/autorun'
require 'faraday'
require 'socket'
require 'pleaxy'

class ClientTest < Minitest::Test
  def client(status:, body:, content_type: 'application/json', **options)
    @seen = []
    stubs = Faraday::Adapter::Test::Stubs.new do |stub|
      handler = lambda do |env|
        @seen << env
        [status, { 'Content-Type' => content_type }, body]
      end
      stub.get(/.*/, &handler)
      stub.post(/.*/, &handler)
    end
    Pleaxy::Client.new(base_url: 'https://api.example.test/', **{ api_key: 'key.secret', workspace_id: 'reg_123.buyer' }.merge(options)) do |conn|
      conn.adapter :test, stubs
    end
  end

  def test_sends_the_api_key_to_the_workspace_url
    po = client(status: 200, body: '{"id":"PO-1","status":"draft"}').purchase_orders.get_purchase_order('PO-1', buyer: 'reg_9.buyer')
    assert_equal 'https://api.example.test/v1/workspaces/reg_123.buyer/purchase-orders/PO-1?buyer=reg_9.buyer', @seen[0].url.to_s
    assert_equal 'key.secret', @seen[0].request_headers['X-Api-Key']
    assert_nil @seen[0].request_headers['Authorization']
    assert_equal 'PO-1', po.id
  end

  def test_sends_a_json_body_with_a_session_token
    c = client(status: 201, body: '{"id":"PO-1"}', api_key: nil, access_token: 'tok')
    po = c.purchase_orders.cancel_purchase_order('PO-1', Pleaxy::CancelPurchaseOrderInput.new(reason: 'duplicate'))
    assert_equal :post, @seen[0].method
    assert_equal '/v1/workspaces/reg_123.buyer/purchase-orders/PO-1/cancel', @seen[0].url.path
    assert_equal 'Bearer tok', @seen[0].request_headers['Authorization']
    assert_nil @seen[0].request_headers['X-Api-Key']
    assert_equal({ 'reason' => 'duplicate' }, JSON.parse(@seen[0].request_body))
    assert_equal 'PO-1', po.id
  end

  def test_reads_the_api_error_code
    c = client(status: 409, body: '{"statusCode":409,"code":"PO_ID_AMBIGUOUS","message":"Two buyers issued PO-1"}')
    error = assert_raises(Pleaxy::ApiError) { c.purchase_orders.get_purchase_order('PO-1') }
    assert_equal 409, error.code
    assert_equal 'PO_ID_AMBIGUOUS', Pleaxy::Client.error(error)[:code]
  end

  # A real socket: downloads stream through Faraday's on_data, which the test adapter never calls.
  def test_returns_a_file_download
    server = TCPServer.new('127.0.0.1', 0)
    thread = Thread.new do
      socket = server.accept
      request_line = socket.gets
      while (line = socket.gets) && line != "\r\n"; end
      body = "invoice,amount\nINV-1,10\n"
      socket.write "HTTP/1.1 200 OK\r\nContent-Type: text/csv; charset=utf-8\r\nContent-Length: #{body.bytesize}\r\nConnection: close\r\n\r\n#{body}"
      socket.close
      request_line
    end
    c = Pleaxy::Client.new(api_key: 'k', workspace_id: 'w', base_url: "http://127.0.0.1:#{server.addr[1]}")
    file = c.invoices.get_payment_export('EXP-1')
    assert_equal "GET /v1/workspaces/w/invoices/payment-exports/EXP-1 HTTP/1.1\r\n", thread.value
    assert_equal "invoice,amount\nINV-1,10\n", File.read(file.path)
  ensure
    server&.close
  end

  def test_requires_a_workspace_and_a_credential
    assert_raises(ArgumentError) { Pleaxy::Client.new(api_key: 'k', workspace_id: '') }
    assert_raises(ArgumentError) { Pleaxy::Client.new(workspace_id: 'w') }
  end

  def test_has_an_accessor_for_every_api_area
    c = Pleaxy::Client.new(api_key: 'k', workspace_id: 'w')
    Pleaxy.constants.grep(/Api\z/).each do |name|
      accessor = name.to_s.delete_suffix('Api').gsub(/([a-z\d])([A-Z])/, '\1_\2').downcase
      assert_instance_of Pleaxy.const_get(name), c.public_send(accessor)
    end
  end
end
