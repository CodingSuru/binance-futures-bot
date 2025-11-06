import sys
import logging
import time
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

def validate_inputs(symbol, side, quantity, price):
    if not symbol or len(symbol) < 3:
        raise ValueError("Invalid symbol")
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be BUY or SELL")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if price <= 0:
        raise ValueError("Price must be positive")
    return True

def place_limit_order(symbol, side, quantity, price):
    try:
        validate_inputs(symbol, side, quantity, price)
        
        client = Client(API_KEY, API_SECRET, testnet=True)
        server_time = client.get_server_time()
        local_time = int(time.time() * 1000)
        time_offset = local_time - server_time['serverTime']
        client.timestamp_offset = -time_offset - 1000
        
        
        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )
        
        logging.info(f"Limit {side.upper()} order placed: Symbol={symbol}, Qty={quantity}, Price={price}, OrderID={order.get('orderId')}")
        print(f"✅ Limit {side.upper()} order placed successfully!")
        print(f"   Symbol: {symbol}")
        print(f"   Quantity: {quantity}")
        print(f"   Price: {price}")
        print(f"   Order ID: {order.get('orderId')}")
        print(f"   Status: {order.get('status')}")
        
        return order
        
    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
        print(f"❌ Validation Error: {ve}")
    except Exception as e:
        logging.error(f"Error placing limit order: {e}")
        print(f"❌ Error placing limit order: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py SYMBOL SIDE QUANTITY PRICE")
        print("Example: python limit_orders.py BTCUSDT BUY 0.01 60000")
        sys.exit(1)
    
    _, symbol, side, qty, price = sys.argv
    place_limit_order(symbol, side, float(qty), float(price))