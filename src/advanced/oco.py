import sys
import time
import logging
from binance.client import Client
from dotenv import load_dotenv
import os
load_dotenv()

logging.basicConfig(
    filename="bot.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

def place_oco_order(symbol, quantity, take_profit_price, stop_price, stop_limit_price):
    try:
        client = Client(API_KEY, API_SECRET, testnet=True)
        server_time = client.get_server_time()
        local_time = int(time.time() * 1000)
        time_offset = local_time - server_time['serverTime']
        client.timestamp_offset = -time_offset - 1000
        
        print("⚠️ OCO not natively supported on Futures API")
        print("Creating separate take-profit and stop-loss orders...")
        
        tp_order = client.futures_create_order(
            symbol=symbol.upper(),
            side="SELL",
            type="LIMIT",
            quantity=quantity,
            price=take_profit_price,
            timeInForce="GTC"
        )
        
        sl_order = client.futures_create_order(
            symbol=symbol.upper(),
            side="SELL",
            type="STOP_MARKET",
            quantity=quantity,
            stopPrice=stop_price
        )
        
        logging.info(f"OCO orders placed: TP={take_profit_price}, SL={stop_price}")
        print(f"✅ OCO-style orders placed!")
        print(f"   Take Profit Order ID: {tp_order.get('orderId')}")
        print(f"   Stop Loss Order ID: {sl_order.get('orderId')}")
        
        return tp_order, sl_order
        
    except Exception as e:
        logging.error(f"Error placing OCO order: {e}")
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python oco.py SYMBOL QUANTITY TP_PRICE STOP_PRICE")
        print("Example: python oco.py BTCUSDT 0.01 62000 58000")
        sys.exit(1)
    
    _, symbol, qty, tp, stop = sys.argv
    place_oco_order(symbol, float(qty), float(tp), float(stop), float(stop) * 0.995)