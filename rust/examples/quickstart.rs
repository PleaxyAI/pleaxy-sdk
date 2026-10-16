//! The quickstart on pleaxy.ai/sdks. Built in CI (cargo build --examples), so it can't drift from the SDK.
use pleaxy::models::{
    create_purchase_order_input, line_item_input, CreatePurchaseOrderInput, LineItemInput,
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = pleaxy::Client::builder()
        .api_key(std::env::var("PLEAXY_API_KEY")?)
        .workspace_id(std::env::var("PLEAXY_WORKSPACE_ID")?)
        .build()?;

    let mut line = LineItemInput::new(
        line_item_input::ScopeType::Sku,
        "EC2 m5.large".into(),
        line_item_input::RuleType::Quantity,
        "hr".into(),
        0.096,
        5000.0,
        0.0,
        "2026-01-01".into(),
        "2026-12-31".into(),
    );
    line.scope_id = Some(Some("AWS-EC2-M5LG".into()));
    line.payment_terms = Some("Net 30".into());

    let mut input = CreatePurchaseOrderInput::new("Amazon Web Services".into(), vec![line]);
    input.provider = Some(create_purchase_order_input::Provider::Aws);

    match client.purchase_orders().create_purchase_order(input).await {
        Ok(po) => println!("{} {:?}", po.id, po.status),
        Err(err) => match pleaxy::api_error(&err) {
            Some(api) => eprintln!("{} {:?}: {}", api.status, api.code, api.message),
            None => return Err(err.into()),
        },
    }
    Ok(())
}
