# M-PESA MCP Server

A Python server implementation for M-PESA payment integration using MCP (M-PESA Connect Protocol).

## Features

- STK Push functionality for mobile payment initiation
- Environment-based configuration
- Secure token management
- Error handling and logging

## Prerequisites

- Python 3.x
- M-PESA Daraja API credentials
- MCP (M-PESA Connect Protocol) setup

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
MPESA_CONSUMER_KEY=your_consumer_key
MPESA_CONSUMER_SECRET=your_consumer_secret
PASSKEY=your_passkey
BUSINESS_SHORTCODE=your_shortcode
CALLBACK_URL=your_callback_url
BASE_URL=https://sandbox.safaricom.co.ke
PHONE_NUMBER=your_phone_number
ACCOUNT_REFERENCE=your_account_reference
```

## Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the server:

```bash
mcp dev main.py
```

The server exposes an STK Push endpoint that accepts payment amount as a parameter.

## Response Format

Successful STK Push response:

```json
{
  "MerchantRequestID": "29115-34620561-1",
  "CheckoutRequestID": "ws_CO_191220191020363925",
  "ResponseCode": "0",
  "ResponseDescription": "Success. Request accepted for processing",
  "CustomerMessage": "Success. Request accepted for processing"
}
```

## License

MIT
