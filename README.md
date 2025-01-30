# 🔍 Anti-Phishing Scanner

## 📌 Overview
The **Anti-Phishing Scanner** is a Python-based security tool designed to analyze website URLs and detect potential phishing threats. It helps users verify if a given URL is suspicious, recently registered, or flagged as a phishing site.

## 🚀 Features
✅ **Domain Age Verification** - Checks how old a domain is using WHOIS lookup.
✅ **Typosquatting Detection** - Identifies if a URL closely resembles popular websites (e.g., "g00gle.com").
✅ **Phishing Database Check** - Compares URLs against the PhishTank API to detect known phishing sites.
✅ **SSL Certificate Validation** - Ensures the website has a valid and secure SSL certificate.
✅ **Content Analysis** - Scans the webpage for phishing-related keywords like "Enter your password" or "Verify account."
✅ **Real-time Logging** - Displays scanning logs dynamically inside the GUI.
✅ **User-friendly GUI** - Built with `tkinter`, allowing users to easily scan URLs and review results visually.

---

## 🛠 Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/anti-phishing-scanner.git
cd anti-phishing-scanner
```
### **2️⃣ Install Required Dependencies**
Ensure you have Python installed (>=3.7). Then, install the required packages:
```bash
pip install -r requirements.txt
```

---

## 🔍 How to Use
### **Run the Scanner**
```bash
python main.py
```
### **Steps:**
1. Enter a website URL into the input field.
2. Click the **"🔍 Scan"** button.
3. View the result and risk level (Safe, Suspicious, or Dangerous).
4. Check the real-time log output for more details.
5. Click **"📜 Show Logs"** to see past logs.
6. Click **"❌ Exit"** to close the application.

---

## 📊 Output Interpretation
| **Risk Level**  | **Meaning**  |
|----------------|-------------|
| ✅ **Safe**  | The domain is old and does not exhibit phishing behavior. |
| ⚠️ **Suspicious** | The domain is relatively new or contains phishing indicators. |
| ❌ **Dangerous** | The domain is very new, matches phishing patterns, or is blacklisted. |

---

## 📜 Logging & Reports
- The tool generates real-time logs stored in the `logs/phishing_logs.log` file.
- Reports are saved in `reports/phishing_report.json`.
- Logs are also displayed in the built-in **Output Box** inside the GUI.

---

## 🏗️ Project Structure
```plaintext
anti-phishing-scanner/
│── scanner/                  # Core scanning modules
│   │── url_checker.py        # Checks domain age (WHOIS)
│   │── similarity_checker.py # Identifies typosquatting domains
│   │── phishing_api.py       # Queries PhishTank API
│   │── ssl_checker.py        # Checks SSL validity
│   │── content_scanner.py    # Scans HTML for phishing-related keywords
│
│── gui/                      # Graphical User Interface (GUI)
│   │── app.py                # Tkinter-based GUI
│
│── utils/                    # Helper functions
│   │── logger.py             # Handles real-time logging
│
│── logs/                     # Stores scanning logs
│── reports/                  # Saves scan results
│── main.py                   # Entry point to start the application
│── requirements.txt           # Required Python dependencies
│── README.md                  # Project documentation
│── LICENSE                    # Open-source license
```

---

## ⚠️ Disclaimer
This tool is intended for **educational and security awareness purposes only**.  
Do not use it for malicious purposes or scan websites without proper authorization.


Utilizing ChatGPT for refinement, the code has been optimized for efficiency, clarity, and performance, eliminating typos and logical errors.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
Pull requests are welcome! Feel free to suggest improvements or report issues via GitHub.

---

## 🌍 Contact
📧 Email: [mtnhb355@gmail.com](mailto\:mtnhb355@gmail.com)

---

