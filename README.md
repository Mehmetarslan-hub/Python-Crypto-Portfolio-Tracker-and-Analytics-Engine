# 📈 Python Crypto Portfolio Tracker & Analytics Engine

A CLI-based cryptocurrency portfolio management and financial analytics engine built with Python. It provides real-time P&L calculations, risk monitoring (Stop-Loss and Portfolio Concentration thresholds), price updates, and automated JSON data persistence.

## 🚀 Key Features

- **Automated Data Persistence:** Reads portfolio data from `portfolio.json`. Dynamically generates demo data if missing or corrupted.
- **Financial Analytics Engine:**
  - Calculates Total Cost, Current Value, Net Profit/Loss ($P\&L$), and ROI percentage.
  - Computes asset allocation weight (%) within the overall portfolio.
- **Risk Auditing & Alert System:**
  - **Stop-Loss Alert:** Triggers if an asset's loss exceeds $-15\%$.
  - **Concentration Risk:** Triggers if an asset's weight exceeds $40\%$ of the portfolio.
- **Interactive CLI Interface:**
  - Tabular financial report formatting.
  - Real-time asset price updates with automated file saving and input sanitization (`.replace(",", ".")`).

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Modules Used:** `json`
- **Core Concepts:** File I/O, Error Handling (`try-except`), Dynamic Lists/Dictionaries, Lambda-free Aggregations, CLI Menu Architecture.

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/Mehmetarslan-hub/Python-Crypto-Portfolio-Tracker-and-Analytics-Engine.git](https://github.com/Mehmetarslan-hub/Python-Crypto-Portfolio-Tracker-and-Analytics-Engine.git)