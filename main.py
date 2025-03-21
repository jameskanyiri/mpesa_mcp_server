#!/usr/bin/env python3
import sys
import logging
import os
import json
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from mpesa.utils import initiate_stk_push
from typing import Union


def load_environment_variables() -> None:
    """
    Load environment variables from .env file.
    Raises an error if critical environment variables are missing.
    """
    load_dotenv()
    required_vars = [
        "MPESA_CONSUMER_KEY",
        "MPESA_CONSUMER_SECRET",
        "PASSKEY",
        "BUSINESS_SHORTCODE",
        "CALLBACK_URL",
        "BASE_URL",
        "PHONE_NUMBER",
        "ACCOUNT_REFERENCE",
    ]

    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing required environment variable: {var}")


# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,  # Log to stderr as recommended
)
logger = logging.getLogger("Daraja_mcp_server")

# Initialize FastMCP server
mcp = FastMCP("Daraja_mcp_server")


@mcp.tool()
def stk_push(amount: int) -> str:
    """
    Prompts the customer to authorize a payment on their mobile device.

    Args:
        amount (int): The amount to be paid.

    Returns:
        str: JSON formatted M-PESA API response
    """
    try:
        response = initiate_stk_push(amount)
        return json.dumps(response, indent=2)
    except Exception as e:
        return f"Failed to initiate STK Push: {str(e)}"


# Start the server
if __name__ == "__main__":
    try:
        # Load and validate environment variables before starting the server
        load_environment_variables()

        # Start the server
        mcp.run(transport="stdio")

    except Exception as e:
        logger.error(f"Server failed to start: {str(e)}")
        sys.exit(1)
