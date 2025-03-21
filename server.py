#!/usr/bin/env python3
import sys
import logging
import os
import base64
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from typing import Union

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,  # Log to stderr as recommended
)
logger = logging.getLogger("Daraja_mcp_server")

# Initialize FastMCP server
mcp = FastMCP("Daraja_mcp_server")

# Get credentials from environment variables
CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET")
BASE_URL = "https://sandbox.safaricom.co.ke"  # Use production URL in production


@mcp.tool()
def generate_token() -> str:
    """Generate an access token for Mpesa Daraja API"""
    try:
        if not CONSUMER_KEY or not CONSUMER_SECRET:
            raise ValueError(
                "Consumer key and secret must be set in environment variables"
            )

        # Create Basic Auth header
        auth_string = f"{CONSUMER_KEY}:{CONSUMER_SECRET}"
        auth_bytes = auth_string.encode("ascii")
        base64_bytes = base64.b64encode(auth_bytes)
        base64_auth = base64_bytes.decode("ascii")

        # Prepare headers
        headers = {"Authorization": f"Basic {base64_auth}"}

        # Prepare parameters
        params = {"grant_type": "client_credentials"}

        # Make the request
        response = requests.get(
            f"{BASE_URL}/oauth/v1/generate", headers=headers, params=params
        )

        # Check if request was successful
        response.raise_for_status()

        # Parse response
        data = response.json()
        access_token = data.get("access_token")
        expires_in = data.get("expires_in")

        if not access_token or not expires_in:
            raise ValueError("Invalid response from OAuth endpoint")

        logger.info(
            f"Successfully generated access token. Expires in {expires_in} seconds"
        )
        return f"Access token generated successfully: {access_token}"

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to generate access token: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while generating access token: {str(e)}")
        raise


# Start the server
if __name__ == "__main__":
    try:
        logger.info("Starting Mpesa Daraja API server...")
        mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Server failed to start: {str(e)}")
        sys.exit(1)
