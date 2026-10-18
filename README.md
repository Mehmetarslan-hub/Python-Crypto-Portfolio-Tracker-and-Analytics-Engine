# Crypto Portfolio Tracker

A small command-line tool that tracks a crypto portfolio stored in a JSON file.
For each coin it calculates cost, current value, profit/loss and portfolio share,
and warns about two kinds of risk. Prices are entered manually by the user.

I wrote this as a Python practice project to work with file I/O, error handling
and lists/dictionaries.

## Features

- Loads the portfolio from `portfolio.json`. If the file is missing or not valid JSON,
  it creates demo data and saves it.
- For each coin: cost, current value, profit/loss and share of the total portfolio (%).
- Portfolio summary: total cost, total value, total profit/loss and overall performance (%).
- Two risk warnings:
  - **Stop-loss:** a coin has lost more than 15% compared to its buying price.
  - **High share:** a single coin is more than 40% of the total portfolio value.
- Menu to show the report or update a coin's price. Updated prices are saved to the file.

## Requirements

- Python 3.6 or newer (uses f-strings)
- No external libraries, only the built-in `json` module

## How to run

```bash
git clone https://github.com/Mehmetarslan-hub/Python-Crypto-Portfolio-Tracker-and-Analytics-Engine.git
cd Python-Crypto-Portfolio-Tracker-and-Analytics-Engine
python main.py
```

## Settings

The two risk limits are constants at the top of the file and can be changed:

| Constant | Default | Meaning |
|---|---|---|
| `STOP_LOSS_SINIRI` | `-15.0` | Loss (%) that triggers the stop-loss warning |
| `MAX_PORTFOY_PAYI` | `40.0` | Maximum share (%) of one coin before a warning |

## Example output (demo data)

```
==============================================================
VARLIK           MALIYET         DEGER     KAR/ZARAR   PAY (%)
--------------------------------------------------------------
Bitcoin       100,000.00    110,000.00    +10,000.00     86.55
Ethereum       16,000.00     12,000.00     -4,000.00      9.44
Solana          2,900.00      3,000.00       +100.00      2.36
Avax            1,400.00      1,500.00       +100.00      1.18
Ripple            550.00        600.00        +50.00      0.47
--------------------------------------------------------------
ÖZET          120,850.00    127,100.00     +6,250.00   %100.00
Net Portföy Performansi: %+5.17
==============================================================

[!] FİNANSAL RİSK BİLDİRİMLERİ:
 -> Bitcoin: Yüksek Portföy Payi (%86.55)
 -> Ethereum: Stop-Loss Riski (%-25.00)
```

## Known limitations

- Prices are not fetched from the internet; they must be entered by hand.
- If `portfolio.json` is corrupted, it is overwritten with demo data, so the old data is lost.
- The program checks that the file can be read, but not that its content is correct.
- A missing key (for example `"adet"`) or a price written as text will crash the analysis.
- Pressing Ctrl+C in the menu exits with a Python error message instead of a clean exit.
- New coins cannot be added from the menu; they must be added to the JSON file.