Market Vision AI is an **advisory trading assistant** designed to analyze market conditions in real time and provide **contextual feedback** on trade entries.

This system **does not place trades**.  
It exists to enforce discipline, validate setups, and prevent low-quality entries.

---

## 🎯 Project Goal

Act as a *silent trading coach* that evaluates:
- Market bias
- Price displacement
- Liquidity context
- Volume behavior
- Entry timing

And returns clear feedback such as:
- VALID_ENTRY
- WAIT
- LATE
- DISCOURAGED
- NO_TRADE

---

## 🧠 Design Philosophy

- **Rules first, code second**
- Human-in-the-loop (no automation of execution)
- Deterministic logic over prediction
- Vision and data are inputs — rules are law

> The system is designed to prevent bad trades, not generate more trades.

---

## 🏗️ Architecture Overview
Market Data / Screen Vision
↓
MarketState
↓
Rule Engine
↓
Decision + Reason

---


The engine evaluates a snapshot of market conditions (`MarketState`) against a versioned ruleset.

---

## 📁 Project Structure
market-vision-ai/
├─ docs/
│ └─ trading_model.md # Human-readable trading model
├─ src/
│ ├─ rules/
│ │ └─ trading_rules.json # Machine-readable ruleset
│ ├─ models/
│ │ └─ market_state.py # Market state contract
│ └─ engine/
│ ├─ evaluator.py # Rule evaluators
│ └─ rule_engine.py # Decision engine
└─ README.md


---

## 🚦 Current Status

✅ Trading model defined  
✅ Machine-readable ruleset  
✅ Rule engine skeleton implemented  

🔜 Unit tests  
🔜 Liquidity refinement  
🔜 Screen vision integration  

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.  
It does not provide financial advice and does not execute trades.

---

## 📌 Future Direction

- Screen vision (candles, volume, VWAP)
- Live market data feeds
- Voice or overlay feedback
- Strategy versioning and backtesting

---

## 🧑‍💻 Author

Built as a long-term systems project focused on **discipline, structure, and clarity** in discretionary trading.
