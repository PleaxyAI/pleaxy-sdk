//! Official Rust client for the [Pleaxy API](https://pleaxy.ai/api-reference): purchase orders,
//! invoices and settlement for cloud spend.
//!
//! ```no_run
//! # async fn run() -> Result<(), Box<dyn std::error::Error>> {
//! let client = pleaxy::Client::builder()
//!     .api_key(std::env::var("PLEAXY_API_KEY")?)
//!     .workspace_id(std::env::var("PLEAXY_WORKSPACE_ID")?)
//!     .build()?;
//! let orders = client.purchase_orders().list_purchase_orders(None, None).await?;
//! # Ok(()) }
//! ```
//!
//! Operations are grouped by API area ([`Client::purchase_orders`], [`Client::invoices`], ...) and
//! named after the operations in the API Reference: CreatePurchaseOrder is
//! `purchase_orders().create_purchase_order`. A failed call returns [`apis::Error`];
//! [`api_error`] reads the API's error body from it.
#![allow(clippy::all, unused_imports, dead_code)]

pub mod apis;
mod client;
pub mod models;
mod resources;

pub use client::{api_error, ApiErrorBody, BuildError, Client, ClientBuilder, DEFAULT_BASE_URL};
pub use resources::*;
