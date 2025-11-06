import sys
import time
import logging
from binance.client import Client
from binance.enums import *
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

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        client = Client(API_KEY, API_SECRET, testnet=True)
        server_time = client.get_server_time()
        local_time = int(time.time() * 1000)
        time_offset = local_time - server_time['serverTime']
        client.timestamp_offset = -time_offset - 1000
        
        
        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
            type=FUTURE_ORDER_TYPE_STOP,
            quantity=quantity,
            price=limit_price,
            stopPrice=stop_price,
            timeInForce=TIME_IN_FORCE_GTC
        )
        
        logging.info(f"Stop-Limit order placed: Symbol={symbol}, Stop={stop_price}, Limit={limit_price}")
        print(f"✅ Stop-Limit {side.upper()} order placed!")
        print(f"   Symbol: {symbol}")
        print(f"   Stop Price: {stop_price}")
        print(f"   Limit Price: {limit_price}")
        print(f"   Order ID: {order.get('orderId')}")
        
        return order
        
    except Exception as e:
        logging.error(f"Error placing stop-limit order: {e}")
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python stop_limit.py SYMBOL SIDE QUANTITY STOP_PRICE LIMIT_PRICE")
        print("Example: python stop_limit.py BTCUSDT BUY 0.01 59000 59100")
        sys.exit(1)
    
    _, symbol, side, qty, stop, limit = sys.argv
    place_stop_limit_order(symbol, side, float(qty), float(stop), float(limit))