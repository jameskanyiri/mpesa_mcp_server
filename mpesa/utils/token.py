import os
import base64
import requests
import logging
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

# Set up logging
logger = logging.getLogger("Daraja_mcp_server")


def get_auth_token() -> str:
    """
    Generate an access token for Mpesa Daraja API.
    Returns:
        str: Access token from the API
    Raises:
        ValueError: If the API response is invalid or credentials are missing
        requests.RequestException: If the API request fails
    """
    consumer_key = os.getenv("MPESA_CONSUMER_KEY")
    consumer_secret = os.getenv("MPESA_CONSUMER_SECRET")
    base_url = os.getenv("BASE_URL", "https://sandbox.safaricom.co.ke")

    if not consumer_key or not consumer_secret:
        raise ValueError("Missing MPESA_CONSUMER_KEY or MPESA_CONSUMER_SECRET")

    # Create Basic Auth string
    auth_str = base64.b64encode(f"{consumer_key}:{consumer_secret}".encode()).decode()

    # Prepare request
    url = f"{base_url}/oauth/v1/generate"
    headers = {"Authorization": f"Basic {auth_str}", "Content-Type": "application/json"}
    params = {"grant_type": "client_credentials"}

    logger.debug(f"Making token request to: {url}")
    logger.debug(f"Request headers: {headers}")
    logger.debug(f"Request params: {params}")

    # Make API request
    response = requests.get(url, headers=headers, params=params)

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Token request failed. Status: {response.status_code}")
        logger.error(f"Response body: {response.text}")
        raise

    # Parse response
    data = response.json()
    access_token = data.get("access_token")

    if not access_token:
        logger.error(f"Invalid response from OAuth endpoint: {data}")
        raise ValueError("Invalid response from OAuth endpoint - missing access token")

    logger.info("Successfully generated access token")
    return access_token
