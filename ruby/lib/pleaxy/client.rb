# frozen_string_literal: true

require 'json'
require 'logger'
require 'uri'

module Pleaxy
  # The Pleaxy API client, scoped to one workspace.
  #
  #   client = Pleaxy::Client.new(api_key: ENV.fetch("PLEAXY_API_KEY"), workspace_id: ENV.fetch("PLEAXY_WORKSPACE_ID"))
  #   orders = client.purchase_orders.list_purchase_orders
  #
  # Operations are grouped by API area (+purchase_orders+, +invoices+, ...) and named after the operations in the
  # API Reference (CreatePurchaseOrder is +purchase_orders.create_purchase_order+). A non-2xx response raises
  # Pleaxy::ApiError; Client.error reads the API's error body from it.
  class Client
    DEFAULT_BASE_URL = 'https://api.pleaxy.ai'

    # The generated configuration, sending only the credential the client was given.
    class ClientConfiguration < Configuration
      attr_accessor :pleaxy_auth

      def auth_settings
        super.select { |name, _| name == pleaxy_auth }
      end
    end

    # The underlying generated client, for anything the API classes don't cover.
    attr_reader :api_client

    # @param workspace_id [String] Company profile → Workspace ID in the Pleaxy console, e.g. reg_01k5x8p9j3q7vn2mhb4tzc6rde.buyer.
    # @param api_key [String] An API key, <keyId>.<secret>, minted by a workspace administrator. Sent as X-Api-Key.
    # @param access_token [String] A signed-in session's access token instead, for the few operations that need a person.
    # @param base_url [String] The API's origin. The client adds /v1/workspaces/<workspace_id>.
    # @param timeout [Integer] Seconds to wait for a response.
    # @param logger [Logger] Where the generated client logs (debugging, saved downloads). Default: nowhere.
    # @yield [Faraday::Connection] Optionally configure the connection (a proxy, an adapter, ...).
    def initialize(workspace_id:, api_key: nil, access_token: nil, base_url: DEFAULT_BASE_URL, timeout: 30, logger: Logger.new(IO::NULL), &faraday)
      raise ArgumentError, 'Pleaxy: workspace_id is required (Company profile → Workspace ID in the Pleaxy console).' if blank?(workspace_id)
      raise ArgumentError, 'Pleaxy: pass an api_key or an access_token.' if blank?(api_key) && blank?(access_token)

      uri = URI.parse(base_url.sub(%r{/+\z}, ''))
      config = ClientConfiguration.new
      config.scheme = uri.scheme
      config.host = uri.port == uri.default_port ? uri.host : "#{uri.host}:#{uri.port}"
      config.base_path = "#{uri.path}/v1/workspaces/#{URI.encode_www_form_component(workspace_id).gsub('+', '%20')}"
      config.ignore_operation_servers = true
      config.server_index = nil
      config.timeout = timeout
      config.logger = logger
      if blank?(api_key)
        config.pleaxy_auth = 'session'
        config.access_token = access_token
      else
        config.pleaxy_auth = 'apiKey'
        config.api_key['X-Api-Key'] = api_key
      end
      config.configure_faraday_connection(&faraday) if faraday
      @api_client = ApiClient.new(config)
    end

    # One accessor per API area: purchase_orders -> Pleaxy::PurchaseOrdersApi, ...
    Pleaxy.constants.grep(/\A[A-Z]\w*Api\z/).each do |name|
      accessor = name.to_s.delete_suffix('Api').gsub(/([a-z\d])([A-Z])/, '\1_\2').downcase
      api_class = Pleaxy.const_get(name)
      define_method(accessor) do
        @apis ||= {}
        @apis[accessor] ||= api_class.new(api_client)
      end
    end

    # The API's error body - :statusCode, :code (e.g. "PO_ID_AMBIGUOUS") when it names one, and :message - as a
    # Hash, or nil when the response had none.
    def self.error(api_error)
      body = api_error.response_body
      return nil if body.nil? || body.empty?

      JSON.parse(body, symbolize_names: true)
    rescue JSON::ParserError
      nil
    end

    private

    def blank?(value)
      value.nil? || value.to_s.empty?
    end
  end
end
