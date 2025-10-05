# MACD Technical Analysis

Project work period: March 2025

## Overview
Python project analyzing financial assets using the **MACD (Moving Average Convergence/Divergence)** indicator. Includes simulations of trades based on historical data for **Gold (XAU/USD)** and **Bitcoin**.

## Features
- Compute MACD and signal line  
- Simulate buy/sell trades  
- Visualize prices, MACD, and trading signals  
- Generate performance statistics  

## Data
- Historical prices from March 2022 – March 2025  
- Source: [Stooq](https://stooq.pl)
  
## Folder Structure

MACD/
├── src/       # Python scripts (MACD calculation, simulation)
├── data/      # CSV files with historical prices (Gold, Bitcoin)
├── results/   # Charts, graphs, and output files
├── .venv/     # Python virtual environment (do not push to GitHub)
└── README.md  # Project descriptionv

## Run

python -m venv .venv
# activate virtual environment:
# On Windows
.venv\Scripts\activate
# On Linux/macOS
source .venv/bin/activate

pip install pandas matplotlib
python src/simulation.py
