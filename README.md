🚀 AI Crypto Evaluator
    AI Crypto Evaluator streamlines cryptocurrency analysis by leveraging OpenAI's GPT API to generate structured insights based on user input. 
    When a user enters a cryptocurrency ticker, the program constructs a well-defined prompt that instructs GPT to return essential details, including the developer, current price, circulating supply, market capitalization, and significant historical events. 
    By setting parameters like temperature and max tokens, the program ensures consistent and informative responses. 
    Additionally, it incorporates error handling mechanisms to validate API keys, allowing users to enter their own key while providing a fallback option if needed. 
    This seamless integration with GPT allows AI Crypto Evaluator to function as a dynamic and user-friendly tool for retrieving cryptocurrency insights.

📌 Features
    ✔ Fetch accurate cryptocurrency data using OpenAI's API
    ✔ User-provided API key support (with a fallback mechanism)
    ✔ Error handling with retry prompts for invalid API keys
    ✔ Simple CLI-based interaction

🛠 Installation
  1️⃣ Clone the repository
  2️⃣ Install dependencies & run
    Ensure you have Python 3.7+ installed
    then run: pip install -r requirements.txt
    ▶ Running the Program
    Run the script using: python ai_crypto_evaluator.py


🔑 API Key Handling
    Upon startup, the program prompts the user to enter their OpenAI API key.
    If the key is invalid, it falls back to a hardcoded backup API key.
    If both keys fail, the program will prompt the user to re-enter a valid API key. 

The program will then prompt the user to:
    Enter the cryptocurrency ticker symbol (e.g., BTC, ETH, XRP): BTC  

    Users will input the ticker symbol of their desired token and the program will input the relevant information.

Crypto Details:

Developer: "Satoshi Nakamoto"  
Price: "$42,500"  
Circulating Supply: "19.5 million BTC"  
Market Cap: "$830 billion"  
Important events:  
- "Bitcoin halving event in April 2024"  
- "Increased institutional adoption"  

Feel free to report any issues to me via Linkedin or Email.
