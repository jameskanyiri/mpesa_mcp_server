# Mpesa Daraja MCP Server

A Python-based server that implements the Mpesa Daraja API functionality using FastMCP. This server provides a simple interface to interact with Safaricom's Mpesa Daraja API, starting with access token generation.

## Features

- OAuth token generation for Mpesa Daraja API
- Secure credential management using environment variables
- Comprehensive error handling and logging
- FastMCP-based server implementation

## Prerequisites

- Python 3.7 or higher
- Mpesa Daraja API credentials (Consumer Key and Secret)
- pip (Python package installer)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mpesa_mcp_server.git
cd mpesa_mcp_server
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Mpesa Daraja credentials:

```env
MPESA_CONSUMER_KEY="your_consumer_key"
MPESA_CONSUMER_SECRET="your_consumer_secret"
PASSKEY="your_passkey"
BUSINESS_SHORTCODE="your_business_shortcode"
CALLBACK_URL="your_callback_url"
```

## Usage

1. Start the server:

```bash
python server.py
```

2. The server will start and listen for requests. You can interact with it using the FastMCP client.

## API Endpoints

### Generate Access Token

Generates an OAuth access token for authenticating Mpesa Daraja API requests.

```python
# Example response
"Access token generated successfully: <your_access_token>"
```

## Error Handling

The server includes comprehensive error handling for:

- Missing environment variables
- API request failures
- Invalid responses
- Network issues

All errors are logged with detailed messages for debugging.

## Security

- Credentials are stored in environment variables
- `.env` file is excluded from version control
- HTTPS is used for all API communications

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Safaricom Daraja API documentation
- FastMCP team for the server framework
