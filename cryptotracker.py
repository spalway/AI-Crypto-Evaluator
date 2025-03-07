# -*- coding: utf-8 -*-
"""CryptoTracker.ipynb - Google Colab Compatible Version"""

import os
import requests
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file in the main directory
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(env_path)

# Fetch API keys from environment variables
api_key = os.getenv("OPENAI_API_KEY")
cmc_api_key = os.getenv("CMC_API_KEY")

if not api_key or not cmc_api_key:
    raise ValueError("API keys not found. Ensure '.env' is correctly placed in the main directory.")

# Initialize OpenAI Client
client = openai.OpenAI(api_key=api_key)

class CryptoAssistant:
    """A class to handle cryptocurrency information retrieval using OpenAI's API and CoinMarketCap API."""

    def __init__(self):
        """Initialize the CryptoAssistant with proper client configuration."""
        self.client = client  # Use the initialized OpenAI client
        self.cmc_api_key = cmc_api_key

    def get_crypto_details(self, ticker: str) -> str:
        """
        Fetch real-time cryptocurrency details using CoinMarketCap API and OpenAI API.

        Args:
            ticker (str): Cryptocurrency ticker symbol (e.g., BTC, ETH)

        Returns:
            str: Formatted cryptocurrency information
        """
        cmc_url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={ticker}&convert=USD"
        headers = {"X-CMC_PRO_API_KEY": self.cmc_api_key, "Accept": "application/json"}

        try:
            response = requests.get(cmc_url, headers=headers)
            response.raise_for_status()
            data = response.json()["data"][ticker]
            price = f"{data['quote']['USD']['price']:.2f} USD"
            market_cap = f"{data['quote']['USD']['market_cap']:.2f} USD"
            circulating_supply = f"{data['circulating_supply']:.2f} {ticker}"
        except Exception as e:
            print(f"Error fetching real-time data: {str(e)}")
            price = "Unavailable"
            market_cap = "Unavailable"
            circulating_supply = "Unavailable"

        # Prompt for OpenAI API
        prompt = f"""
        Provide information about the cryptocurrency {ticker} in exactly this format:

        Developer: "Name of the developer or team behind the coin"
        Price: "{price}"
        Circulating Supply: "{circulating_supply}"
        Market Cap: "{market_cap}"
        Important events:
        - "Brief description of a notable event"
        - "Another key event related to the coin"
        Recent News:
        - "Latest news headline and summary"
        - "Another significant news event"
        Future Analysis:
        - "Predicted trends based on market behavior and global events"
        - "Predicted price for the end of the year based on data and factoring in news and history"
        - "Potential risks and opportunities"

        Ensure all responses strictly follow this format.
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a cryptocurrency assistant. Always provide information in the exact format specified."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Detailed error: {str(e)}")
            raise Exception(f"Error getting crypto details: {str(e)}")

def main():
    """Main execution function with error handling."""
    print("Welcome to the Cryptocurrency Assistant!")

    # Check if running in a CI/CD environment
    is_github_actions = os.getenv("GITHUB_ACTIONS") == "true"

    if is_github_actions:
        ticker_symbol = "BTC"  # Default to BTC in GitHub Actions
        print(f"Running in GitHub Actions - Using default ticker: {ticker_symbol}")
    else:
        print("Enter 'quit' to exit the program.")
        ticker_symbol = input("\nEnter the cryptocurrency ticker symbol (e.g., XRP, BTC, ETH) or type quit: ").strip().upper()

    assistant = CryptoAssistant()

    while True:
        if ticker_symbol.lower() == 'quit':
            print("Thank you for using the CryptoTracker Assistant!")
            break

        try:
            details = assistant.get_crypto_details(ticker_symbol)
            print("\nCrypto Details:\n")
            print(details)
        except Exception as e:
            print(f"An error occurred: {e}")

        if is_github_actions:
            break  # Exit after one run in CI/CD

        # Ask for the next input if running locally
        ticker_symbol = input("\nEnter the cryptocurrency ticker symbol (e.g., XRP, BTC, ETH) or type quit: ").strip().upper()

if __name__ == "__main__":
    main()
