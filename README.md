# AI Crypto Evaluator
![image](https://github.com/user-attachments/assets/145eb3cd-27f3-4da3-b00a-8860c4332c4a)

## Google Collab Link Below (If you are having issues running on your local environment) 
*Upload the ENV template from Github into content/api.env in Google Collab*
*CMC API is already provided, you will only need an OpenAI API which you can obtain at platform.openai.com*

[![If you are having trouble running the program on your local environment, click here for the Google Colab version](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dZwECFGlu2HNV7DC2dbvBaLtrYTIkY3s?usp=sharing)

## Overview
**AI Crypto Evaluator** is an advanced cryptocurrency analysis tool that leverages **OpenAI's GPT-4 Turbo** and **CoinMarketCap API** to provide real-time cryptocurrency insights. It fetches live market data and combines it with AI-driven analysis to present:
- **Developer Information**
- **Current Price, Market Cap, and Circulating Supply**
- **Important Historical Events**
- **Recent News Highlights**
- **Future Analysis & Predictions**

## Features
- **Real-Time Data:** Fetches live cryptocurrency data from **CoinMarketCap API**.
- **AI-Powered Insights:** Uses **OpenAI GPT-4 Turbo** to generate intelligent market analysis.
- **Secure API Handling:** Stores API keys securely via **GitHub Secrets** or `.env` files.
- **Error Handling:** Gracefully manages errors in API requests and OpenAI interactions.
- **User-Friendly Interface:** CLI-based input for quick evaluations.

## Installation & Setup

### 1. Clone the Repository
```sh
$ git clone https://github.com/spalway/AI-Crypto-Evaluator.git
$ cd AI-Crypto-Evaluator
```

### 2. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 3. Set Up API Keys
The project requires **OpenAI API** and **CoinMarketCap API** keys. You can store them either locally or via GitHub Secrets.

#### **GitHub Secrets (Preconfigured for Users)**
API keys have already been set up as **GitHub Secrets**, so users can run the application without manual configuration. No need to create a `.env` file manually.

To verify or update the keys:
1. Go to **Settings** → **Secrets and variables** → **Actions** in your GitHub repository.
2. Ensure the following secrets are set:
   - **OPENAI_API_KEY** → Your OpenAI API key
   - **CMC_API_KEY** → Your CoinMarketCap API key

The script will automatically fetch these keys when executed.
1. Go to **Settings** → **Secrets and variables** → **Actions** in your GitHub repository.
2. Add the following secrets:
   - **OPENAI_API_KEY** → Your OpenAI API key
   - **CMC_API_KEY** → Your CoinMarketCap API key

## Usage
Run the script using:
```sh
$ python cryptotracker.py
```
You will be prompted to enter a **cryptocurrency ticker symbol** (e.g., BTC, ETH). The tool will fetch data, analyze trends, and present structured insights.

### Example Output
```
Welcome to the Cryptocurrency Assistant!
Enter 'quit' to exit the program.

Enter the cryptocurrency ticker symbol (e.g., XRP, BTC, ETH): BTC

Crypto Details:
Developer: "Bitcoin Core Team"
Price: "45,000.00 USD"
Circulating Supply: "19,200,000 BTC"
Market Cap: "864,000,000,000 USD"
Important events:
- "Bitcoin halving event in 2024, reducing mining rewards."
- "ETF approval in 2023 led to increased institutional investment."
Recent News:
- "Bitcoin reaches all-time high in Q1 2024."
- "Regulatory discussions impact cryptocurrency adoption."
Future Analysis:
- "Expected price increase due to scarcity and adoption."
- "Potential risks related to government regulations."
```

## File Structure
```
AI-Crypto-Evaluator/
│-- crypto_assistant.py  # Main program
│-- .gitignore           # Prevents sensitive files from being tracked
│-- README.md            # Project documentation
│-- requirements.txt     # Required dependencies
```

## Contributing
Pull requests are welcome. For significant changes, open an issue first to discuss your ideas.

## License
MIT License. See `LICENSE` for details.

## Author
Akshanth Palway - [[Linkedin](https://www.linkedin.com/in/apalway/)]

---

**Now you’re ready to evaluate cryptocurrencies with AI-powered insights! 🚀**

