# The quickstart on pleaxy.ai/sdks. Loaded in CI (rake examples) with PLEAXY_DRY_RUN set, so it can't drift from the SDK.
require 'pleaxy'

client = Pleaxy::Client.new(
  api_key: ENV.fetch('PLEAXY_API_KEY', 'dry-run.key'),
  workspace_id: ENV.fetch('PLEAXY_WORKSPACE_ID', 'dry-run')
)

input = Pleaxy::CreatePurchaseOrderInput.new(
  supplier: 'Amazon Web Services',
  provider: 'aws',
  line_items: [
    Pleaxy::LineItemInput.new(
      scope_type: 'sku',
      scope_id: 'AWS-EC2-M5LG',
      name: 'EC2 m5.large',
      rule_type: 'quantity',
      unit: 'hr',
      unit_price: 0.096,
      qty: 5000,
      nte_amount: 0,
      payment_terms: 'Net 30',
      valid_from: '2026-01-01',
      valid_until: '2026-12-31'
    )
  ]
)

if ENV['PLEAXY_DRY_RUN']
  raise 'no create_purchase_order' unless client.purchase_orders.respond_to?(:create_purchase_order)
else
  begin
    po = client.purchase_orders.create_purchase_order(input)
    puts "#{po.id} #{po.status}"
  rescue Pleaxy::ApiError => e
    error = Pleaxy::Client.error(e)
    warn "#{e.code} #{error&.dig(:code)}: #{error&.dig(:message)}"
  end
end
