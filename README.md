# 🤖 Binance Futures Trading Bot

A comprehensive, production-ready CLI trading bot for Binance USDT-M Futures that automates various trading strategies with enterprise-grade logging, validation, and error handling.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()
[![Binance](https://img.shields.io/badge/Exchange-Binance%20Futures-yellow.svg)](https://www.binance.com/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Order Types & Usage](#-order-types--usage)
- [Advanced Strategies](#-advanced-strategies)
- [Configuration](#-configuration)
- [Monitoring & Logs](#-monitoring--logs)
- [Error Handling](#-error-handling)
- [Use Cases](#-use-cases)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Disclaimer](#-disclaimer)

---

## 🎯 Overview

The **Binance Futures Trading Bot** is a command-line interface (CLI) application designed to automate cryptocurrency trading on Binance Futures. It provides a robust framework for executing various order types and implementing sophisticated trading strategies without manual intervention.

### Why This Project?

Manual trading on cryptocurrency exchanges presents several challenges:
- **Emotional Decision Making**: Fear and greed often lead to poor trading decisions
- **Limited Execution Speed**: Humans cannot react as quickly as automated systems
- **Time-Intensive**: Requires constant market monitoring
- **Inconsistent Strategy Implementation**: Difficult to maintain discipline manually
- **Complex Order Management**: Managing multiple orders simultaneously is error-prone
- **No 24/7 Availability**: Crypto markets never sleep, but humans need to

This bot solves these problems by providing automated, emotionless, and consistent trade execution.

---

## 💡 Problem Statement

### Challenges in Crypto Trading:

1. **Market Impact on Large Orders**
   - Large orders can significantly move market prices
   - **Solution**: TWAP (Time-Weighted Average Price) strategy

2. **Range-Bound Market Opportunities**
   - Missing profit opportunities in sideways markets
   - **Solution**: Grid Trading Strategy

3. **Risk Management Complexity**
   - Difficult to set both profit targets and stop-losses manually
   - **Solution**: OCO (One-Cancels-Other) orders

4. **Timing & Execution Precision**
   - Missing optimal entry/exit points
   - **Solution**: Stop-Limit orders for conditional execution

5. **Lack of Trade Logging**
   - No audit trail for analyzing trading performance
   - **Solution**: Comprehensive logging system

---

## ✨ Key Features

### 🔐 Safety & Security
- ✅ **Testnet Support**: Safe testing environment with no real funds at risk
- ✅ **Input Validation**: All parameters validated before execution
- ✅ **Error Handling**: Comprehensive exception handling
- ✅ **Audit Trail**: Detailed logging of all operations
- ✅ **Environment Variables**: Secure API credential management

### 📊 Order Types
- 🎯 **Market Orders**: Instant execution at current market price
- 📌 **Limit Orders**: Execute at specific price or better
- 🛑 **Stop-Limit Orders**: Conditional order activation
- 🔄 **OCO Orders**: Combined profit/loss management
- ⏱️ **TWAP Orders**: Time-distributed order execution
- 📈 **Grid Trading**: Automated range trading

### 🛠️ Technical Features
- ⚡ **Timestamp Synchronization**: Automatic server time sync
- 📝 **Comprehensive Logging**: File-based operation logs
- 🔍 **Real-time Feedback**: Console output for all operations
- 🎨 **User-Friendly CLI**: Simple command-line interface
- 🐍 **Python-Based**: Easy to understand and modify

---

## 📁 Project Structure

```
binance_bot/
│
├── src/
│   ├── market_orders.py       # Instant market execution
│   ├── limit_orders.py        # Price-specific orders
│   │
│   └── advanced/
│       ├── stop_limit.py      # Conditional stop orders
│       ├── oco.py             # Profit/loss management
│       ├── twap.py            # Time-distributed execution
│       └── grid_strategy.py   # Range trading automation
│
├── .env                       # API credentials (not included)
├── bot.log                    # Execution logs (auto-generated)
├── requirements.txt           # Python dependencies
├── README.md                  # This documentation
└── report.pdf                 # Project analysis report
```

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Binance Futures account (testnet or live)

### Step 1: Clone the Repository
```bash
git clone https://github.com/CodingSuru/binance-futures-bot.git
cd binance-futures-bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- `python-binance` - Binance API wrapper
- `python-dotenv` - Environment variable management

### Step 3: Configure API Credentials

Create a `.env` file in the project root:

```env
API_KEY=your_binance_api_key_here
API_SECRET=your_binance_api_secret_here
```

**⚠️ Security Warning**: 
- Never commit `.env` file to version control
- Keep your API keys confidential
- Use testnet credentials for learning/testing

#### Getting API Keys:

**For Testnet (Recommended for Learning):**
1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com/)
2. Register/Login
3. Navigate to API Management
4. Create new API key
5. Copy credentials to `.env`

**For Live Trading (Advanced Users Only):**
1. Visit [Binance](https://www.binance.com/)
2. Navigate to API Management
3. Create API key with appropriate permissions
4. Enable futures trading permission
5. Configure IP whitelist for security

---

## 🎮 Quick Start

### Test Your Setup

Run a simple market order to verify everything is working:

```bash
python src/market_orders.py BTCUSDT BUY 0.01
```

**Expected Output:**
```
✅ Market BUY order placed successfully!
   Symbol: BTCUSDT
   Quantity: 0.01
   Order ID: 123456789
   Status: FILLED
```

If you see this, congratulations! Your bot is ready to use.

---

## 📘 Order Types & Usage

### 1. Market Orders

**Purpose**: Execute immediately at the best available market price.

**Syntax:**
```bash
python src/market_orders.py SYMBOL SIDE QUANTITY
```

**Examples:**
```bash
# Buy 0.01 BTC at current market price
python src/market_orders.py BTCUSDT BUY 0.01

# Sell 0.5 ETH at current market price
python src/market_orders.py ETHUSDT SELL 0.5

# Buy 1 SOL
python src/market_orders.py SOLUSDT BUY 1
```

**When to Use:**
- ✅ Need immediate execution
- ✅ High liquidity markets
- ✅ Emergency exits
- ❌ Avoid for large orders (use TWAP instead)

---

### 2. Limit Orders

**Purpose**: Execute only at your specified price or better.

**Syntax:**
```bash
python src/limit_orders.py SYMBOL SIDE QUANTITY PRICE
```

**Examples:**
```bash
# Buy BTC only if price drops to $60,000
python src/limit_orders.py BTCUSDT BUY 0.01 60000

# Sell ETH only if price rises to $3,500
python src/limit_orders.py ETHUSDT SELL 0.5 3500

# Buy SOL at $150
python src/limit_orders.py SOLUSDT BUY 1 150
```

**When to Use:**
- ✅ Want specific entry/exit price
- ✅ Not urgent
- ✅ Setting up positions in advance
- ❌ Don't use if you need guaranteed execution

---

## 🎓 Advanced Strategies

### 3. Stop-Limit Orders

**Purpose**: Trigger a limit order when price reaches your stop price.

**How It Works:**
1. Price reaches stop price → Order activates
2. Limit order placed at your specified price
3. Executes if market reaches limit price

**Syntax:**
```bash
python src/advanced/stop_limit.py SYMBOL SIDE QUANTITY STOP_PRICE LIMIT_PRICE
```

**Examples:**
```bash
# Stop-loss: Sell if BTC drops to $59,000, limit at $59,100
python src/advanced/stop_limit.py BTCUSDT SELL 0.01 59000 58900

# Buy breakout: Buy if ETH breaks $3,000, limit at $3,010
python src/advanced/stop_limit.py ETHUSDT BUY 0.5 3000 3010
```

**Use Cases:**
- 🛡️ Stop-loss protection
- 🚀 Breakout trading
- 📈 Trend following
- 🎯 Conditional entries

---

### 4. OCO Orders (One-Cancels-Other)

**Purpose**: Simultaneously manage profit target and stop-loss.

**How It Works:**
- Creates two orders: Take-Profit (limit) and Stop-Loss (stop)
- When one executes, the other cancels automatically
- Perfect for risk management

**Syntax:**
```bash
python src/advanced/oco.py SYMBOL QUANTITY TAKE_PROFIT_PRICE STOP_PRICE
```

**Example:**
```bash
# Profit at $62,000 OR stop-loss at $58,000
python src/advanced/oco.py BTCUSDT 0.01 62000 58000
```

**Real-World Scenario:**
```
You bought BTC at $60,000
- Take profit: $65,000 (+8.3% gain)
- Stop loss: $57,000 (-5% loss)

python src/advanced/oco.py BTCUSDT 0.01 65000 57000
```

**Benefits:**
- ✅ Automated risk management
- ✅ Locks in profits
- ✅ Limits losses
- ✅ Set and forget

---

### 5. TWAP Strategy (Time-Weighted Average Price)

**Purpose**: Execute large orders gradually to minimize market impact.

**Problem Solved:**
Large orders can cause significant price slippage. TWAP splits your order into smaller chunks executed over time.

**Syntax:**
```bash
python src/advanced/twap.py SYMBOL SIDE TOTAL_QUANTITY PARTS INTERVAL_SECONDS
```

**Example:**
```bash
# Buy 1 BTC split into 10 parts over 5 minutes
python src/advanced/twap.py BTCUSDT BUY 1.0 10 30
```

**Execution Process:**
```
📊 Starting TWAP order:
   Total Quantity: 1.0
   Parts: 10
   Quantity per part: 0.1
   Interval: 30s

✅ Part 1/10 executed | Order ID: 123456
   Waiting 30s before next part...
✅ Part 2/10 executed | Order ID: 123457
   Waiting 30s before next part...
...
✅ TWAP order completed! 10/10 parts executed
```

**Benefits:**
- 📉 Reduced market impact
- 💰 Better average price
- 🎯 More consistent fills
- 📊 Professional execution

**When to Use:**
- Large position sizes
- Low liquidity markets
- When price stability matters
- Accumulation strategies

---

### 6. Grid Trading Strategy

**Purpose**: Profit from price oscillations in range-bound markets.

**How It Works:**
1. Define price range (lower and upper bounds)
2. Place buy orders in lower half
3. Place sell orders in upper half
4. Profit as price moves up and down

**Syntax:**
```bash
python src/advanced/grid_strategy.py SYMBOL LOWER_PRICE UPPER_PRICE GRID_LEVELS QUANTITY_PER_LEVEL
```

**Example:**
```bash
# Setup 10 grid levels between $58,000 - $62,000
python src/advanced/grid_strategy.py BTCUSDT 58000 62000 10 0.01
```

**Visual Representation:**
```
$62,000 ├─ SELL 0.01 ─┤
$61,600 ├─ SELL 0.01 ─┤
$61,200 ├─ SELL 0.01 ─┤
$60,800 ├─ SELL 0.01 ─┤
$60,400 ├─ SELL 0.01 ─┤
────────────────────────  Current Price
$60,000 ├─ BUY 0.01 ──┤
$59,600 ├─ BUY 0.01 ──┤
$59,200 ├─ BUY 0.01 ──┤
$58,800 ├─ BUY 0.01 ──┤
$58,000 ├─ BUY 0.01 ──┤
```

**Example Output:**
```
🎯 Setting up Grid Trading Strategy:
   Symbol: BTCUSDT
   Price Range: 58000 - 62000
   Grid Levels: 10
   Price Step: 444.44
   Quantity per level: 0.01

✅ BUY order placed at $58000.00 | Order ID: 123451
✅ BUY order placed at $58444.44 | Order ID: 123452
✅ BUY order placed at $58888.89 | Order ID: 123453
...
✅ SELL order placed at $61111.11 | Order ID: 123458
✅ SELL order placed at $61555.56 | Order ID: 123459
✅ SELL order placed at $62000.00 | Order ID: 123460

✅ Grid setup complete!
   Buy orders: 5
   Sell orders: 5
```

**Best Market Conditions:**
- ✅ Sideways/ranging markets
- ✅ High volatility
- ✅ Predictable support/resistance
- ❌ Avoid in strong trends

**Profitability Example:**
```
Grid Range: $58,000 - $62,000
Grid Levels: 20
Investment: $1,000

If price oscillates 3 times across the range:
- Each cycle profit: ~1.5-2%
- Total profit: ~4.5-6% (excluding fees)
```

---

## ⚙️ Configuration

### Environment Variables

The `.env` file structure:

```env
# Binance API Credentials
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here

# Optional: Testnet Flag (default: True in code)
# TESTNET=True
```

### Code Configuration

Each script includes these configurable parameters:

**Timestamp Synchronization:**
```python
client.timestamp_offset = -time_offset - 1000
```

**Logging Configuration:**
```python
logging.basicConfig(
    filename="bot.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
```

**Testnet vs Live:**
```python
# Currently: testnet=True (safe for testing)
client = Client(API_KEY, API_SECRET, testnet=True)

# For live trading (Advanced users only):
# client = Client(API_KEY, API_SECRET, testnet=False)
```

---

## 📊 Monitoring & Logs

### Log File Structure

All operations are logged to `bot.log`:

```
2025-11-06 14:32:10 - INFO - Market BUY order placed: Symbol=BTCUSDT, Qty=0.01, OrderID=12345
2025-11-06 14:35:22 - INFO - Limit SELL order placed: Symbol=ETHUSDT, Qty=0.5, Price=3500, OrderID=12346
2025-11-06 14:40:15 - ERROR - Validation error: Quantity must be positive
2025-11-06 14:45:30 - INFO - TWAP part 1/5: BUY 0.02 BTCUSDT - OrderID=12347
```

### Viewing Logs

**Linux/Mac:**
```bash
# View last 20 entries
tail -n 20 bot.log

# Real-time monitoring
tail -f bot.log

# Search for errors
grep ERROR bot.log
```

**Windows:**
```powershell
# View last 20 entries
Get-Content bot.log -Tail 20

# Real-time monitoring
Get-Content bot.log -Wait

# Search for errors
Select-String -Path bot.log -Pattern "ERROR"
```

### Log Analysis

**Success Rate:**
```bash
grep "order placed" bot.log | wc -l  # Total successful orders
grep "ERROR" bot.log | wc -l         # Total errors
```

---

## 🛡️ Error Handling

### Validation Errors

The bot validates all inputs before execution:

```bash
# Invalid quantity
python src/market_orders.py BTCUSDT BUY -0.01
❌ Validation Error: Quantity must be positive

# Invalid symbol
python src/market_orders.py BTC BUY 0.01
❌ Validation Error: Invalid symbol

# Invalid side
python src/market_orders.py BTCUSDT PURCHASE 0.01
❌ Validation Error: Side must be BUY or SELL
```

### API Errors

**Timestamp Issues:**
```
Error: Timestamp for this request was 1000ms ahead
Solution: Automatic timestamp synchronization is built-in
```

**Insufficient Balance:**
```
Error: Insufficient balance
Solution: Add funds to your testnet/live account
```

**Invalid API Keys:**
```
Error: Invalid API-key, IP, or permissions
Solution: Verify .env file and API key permissions
```

---

## 💼 Use Cases

### 1. Day Trading
```bash
# Quick market entries
python src/market_orders.py BTCUSDT BUY 0.1

# Set take-profit and stop-loss
python src/advanced/oco.py BTCUSDT 0.1 61000 59000
```

### 2. Swing Trading
```bash
# Accumulate at specific price levels
python src/limit_orders.py ETHUSDT BUY 1.0 3200
python src/limit_orders.py ETHUSDT BUY 1.0 3100
python src/limit_orders.py ETHUSDT BUY 1.0 3000
```

### 3. Dollar-Cost Averaging (DCA)
```bash
# Buy $100 worth of BTC every week
# (Calculate quantity based on current price)
python src/twap.py BTCUSDT BUY 0.05 7 86400  # 7 parts over 7 days
```

### 4. Range Trading
```bash
# Profit from sideways market
python src/advanced/grid_strategy.py BTCUSDT 58000 62000 20 0.01
```

### 5. Breakout Trading
```bash
# Buy on breakout above $60,000
python src/advanced/stop_limit.py BTCUSDT BUY 0.1 60000 60100
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Timestamp error | Clock sync issue | Automatic fix included in code |
| API connection failed | Network/firewall | Check internet, disable VPN |
| Invalid symbol | Wrong format | Use BTCUSDT not BTC-USDT |
| Insufficient balance | Low funds | Add testnet funds via faucet |
| Order rejected | Min quantity not met | Check Binance minimums |
| Import error | Missing packages | Run `pip install -r requirements.txt` |

### System Time Synchronization

**Windows:**
```cmd
w32tm /resync
```

**Linux:**
```bash
sudo ntpdate -s time.nist.gov
```

**Mac:**
```bash
sudo sntp -sS time.apple.com
```

---

## 📌 Best Practices

### 1. Start with Testnet
- Always test strategies on testnet first
- Testnet provides risk-free environment
- Validate your logic before going live

### 2. Position Sizing
```python
# Never risk more than 1-2% per trade
account_balance = 10000  # USDT
risk_per_trade = account_balance * 0.02  # 2% = $200
```

### 3. Use Stop-Losses
```bash
# Always protect your capital
python src/advanced/oco.py BTCUSDT 0.1 65000 57000
```

### 4. Monitor Logs Regularly
```bash
# Check for errors daily
tail -n 50 bot.log | grep ERROR
```

### 5. Secure API Keys
- Use IP whitelist on Binance
- Limit API permissions to trading only
- Never share your API keys
- Rotate keys periodically

### 6. Backtesting
- Test strategies on historical data
- Adjust parameters based on results
- Consider market conditions

---

## 🗺️ Roadmap

### Current Version (v1.0)
- ✅ Core order types (Market, Limit)
- ✅ Advanced strategies (TWAP, Grid, OCO)
- ✅ Comprehensive logging
- ✅ Input validation

### Planned Features (v2.0)
- 🔄 Web-based dashboard
- 📈 Performance analytics
- 🤖 Strategy backtesting
- 📱 Mobile notifications
- 🔔 Price alerts
- 📊 Portfolio management
- 🌐 Multi-exchange support

### Future Enhancements (v3.0)
- 🧠 Machine learning price prediction
- 📡 WebSocket real-time data
- 🔐 Enhanced security features
- 📖 Strategy marketplace
- 🎯 Auto-optimization

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue with detailed description
2. **Suggest Features**: Share your ideas for improvements
3. **Submit Pull Requests**: Fork, develop, and submit PRs
4. **Improve Documentation**: Help make docs clearer
5. **Share Strategies**: Contribute profitable strategies

### Development Setup
```bash
# Fork and clone
git clone https://github.com/CodingSuru/binance-futures-bot.git
cd binance-futures-bot

# Create branch
git checkout -b feature/your-feature-name

# Make changes and test
python src/market_orders.py BTCUSDT BUY 0.01

# Commit and push
git add .
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
```

---

## ⚠️ Disclaimer

**IMPORTANT - READ CAREFULLY**

This bot is provided for **educational purposes only**. 

### Risk Warning
- ⚠️ Cryptocurrency trading carries substantial risk of loss
- ⚠️ Past performance does not guarantee future results
- ⚠️ Never trade with money you cannot afford to lose
- ⚠️ This is NOT financial advice
- ⚠️ Always do your own research (DYOR)

### Legal
- This software is provided "as is" without warranty
- The authors are not responsible for any financial losses
- Use at your own risk
- Comply with local regulations regarding crypto trading

### Best Practices
- ✅ Start with testnet and small amounts
- ✅ Understand each strategy before using it
- ✅ Never share your API keys
- ✅ Use proper risk management
- ✅ Keep software updated

---

## 📞 Support & Contact

- **Documentation**: This README and inline code comments
- **Issues**: [GitHub Issues](https://github.com/yourusername/binance-futures-bot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/binance-futures-bot/discussions)

---

## 📚 Resources

### Official Documentation
- [Binance Futures API](https://binance-docs.github.io/apidocs/futures/en/)
- [Python-Binance Library](https://python-binance.readthedocs.io/)
- [Python Documentation](https://docs.python.org/3/)

### Learning Resources
- [Binance Academy](https://academy.binance.com/)
- [Trading Strategies Guide](https://www.binance.com/en/support/faq)
- [Risk Management](https://www.investopedia.com/terms/r/riskmanagement.asp)

---

## 📄 License

This project is released under the MIT License - see the LICENSE file for details.

**Educational Use Only** - Not licensed for commercial trading without proper review and testing.

---

## 🙏 Acknowledgments

- Binance for providing comprehensive API
- Python-Binance library maintainers
- Open-source community
- All contributors and testers

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/binance-futures-bot?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/binance-futures-bot?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/binance-futures-bot)
![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)

---

**Made with ❤️ for the crypto trading community**

**Last Updated**: November 6, 2025  
**Version**: 1.0.0  
**Status**: Active Development

---
