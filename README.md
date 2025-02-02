# 🚀 AI Crypto Evaluator

AI Crypto Evaluator streamlines cryptocurrency analysis by leveraging OpenAI's GPT API to generate structured insights based on user input.

When a user enters a cryptocurrency ticker, the program constructs a well-defined prompt that instructs GPT to return essential details, including the developer, current price, circulating supply, market capitalization, and significant historical events.

By setting parameters like temperature and max tokens, the program ensures consistent and informative responses. Additionally, it incorporates error handling mechanisms to validate API keys, allowing users to enter their own key while providing a fallback option if needed.

This seamless integration with GPT allows the AI Crypto Evaluator to function as a dynamic and user-friendly tool for retrieving cryptocurrency insights.

---

## 📌 Features

- ✔ Fetch accurate cryptocurrency data using OpenAI's API
- ✔ User-provided API key support (with a fallback mechanism)
- ✔ Error handling with retry prompts for invalid API keys
- ✔ Simple CLI-based interaction

---

## 🛠 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai-crypto-evaluator.git
   cd cryptotracker.py
   ```

2. **Install Dependencies**  
   Ensure you have Python 3.7+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Program**
   ```bash
   python cryptotracker.py
   ```

---

## 🔑 API Key Handling

- Upon startup, the program prompts the user to enter their OpenAI API key.
- If the key is invalid, it falls back to a hardcoded backup API key.
- If both keys fail, the program will prompt the user to re-enter a valid API key.

---

## 🚀 Usage

1. Run the script:
   ```bash
   python cryptotracker.py
   ```

2. Enter the cryptocurrency ticker symbol when prompted:
   ```
   Enter the cryptocurrency ticker symbol (e.g., BTC, ETH, XRP): BTC
   ```

3. Receive detailed insights:
   ```
   Crypto Details:

   Developer: "Satoshi Nakamoto"
   Price: "$42,500"
   Circulating Supply: "19.5 million BTC"
   Market Cap: "$830 billion"
   Important events:
   - "Bitcoin halving event in April 2024"
   - "Increased institutional adoption"
   ```

---

## ⚠️ Error Handling

- If an invalid API key is provided, the program retries with the backup key.
- If errors persist, the program prompts the user to re-enter a valid API key.
- Detailed error messages are displayed for debugging.

---

## 🤝 Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

---

## 📬 Contact
Developed by: Akshanth Palway
Southern Methodist University
For issues, questions, or suggestions, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/apalway) or email.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

