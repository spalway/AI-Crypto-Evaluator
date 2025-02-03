# 🚀 AI Crypto Evaluator

![image](https://github.com/user-attachments/assets/064b8604-5679-44cc-acd7-9e0a4a41d679)


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
$ git clone https://github.com/your-username/AI-Crypto-Evaluator.git
$ cd AI-Crypto-Evaluator
```

### 2. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 3. Set Up API Keys
The project requires **OpenAI API** and **CoinMarketCap API** keys. You can store them either locally or via GitHub Secrets.

#### **Option 1: Local `.env` File**
Create a `.env` file in the project root and add:
```plaintext
OPENAI_API_KEY=your_openai_api_key_here
CMC_API_KEY=your_coinmarketcap_api_key_here
```

#### **Option 2: GitHub Secrets (Recommended for CI/CD)**
1. Go to **Settings** → **Secrets and variables** → **Actions** in your GitHub repository.
2. Add the following secrets:
   - **OPENAI_API_KEY** → Your OpenAI API key
   - **CMC_API_KEY** → Your CoinMarketCap API key

## Usage
Run the script using:
```sh
$ python crypto_assistant.py
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
Akshanth Palway - [Linkedin](https://www.linkedin.com/in/apalway/)

---

**Now you’re ready to evaluate cryptocurrencies with AI-powered insights! 🚀**

