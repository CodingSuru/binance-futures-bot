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

def twap_order(symbol, side, total_quantity, parts, interval_seconds):
    try:
        client = Client(API_KEY, API_SECRET, testnet=True)
        server_time = client.get_server_time()
        local_time = int(time.time() * 1000)
        time_offset = local_time - server_time['serverTime']
        client.timestamp_offset = -time_offset - 1000
        
        
        qty_per_part = total_quantity / parts
        
        print(f"🔄 Starting TWAP order:")
        print(f"   Total Quantity: {total_quantity}")
        print(f"   Parts: {parts}")
        print(f"   Quantity per part: {qty_per_part}")
        print(f"   Interval: {interval_seconds}s\n")
        
        orders = []
        for i in range(parts):
            try:
                order = client.futures_create_order(
                    symbol=symbol.upper(),
                    side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=qty_per_part
                )
                
                orders.append(order)
                logging.info(f"TWAP part {i+1}/{parts}: {side} {qty_per_part} {symbol} - OrderID={order.get('orderId')}")
                print(f"✅ Part {i+1}/{parts} executed | Order ID: {order.get('orderId')}")
                
                if i < parts - 1:
                    print(f"   Waiting {interval_seconds}s before next part...")
                    time.sleep(interval_seconds)
                    
            except Exception as e:
                logging.error(f"TWAP part {i+1} error: {e}")
                print(f"❌ Part {i+1} failed: {e}")
        
        print(f"\n✅ TWAP order completed! {len(orders)}/{parts} parts executed")
        return orders
        
    except Exception as e:
        logging.error(f"TWAP error: {e}")
        print(f"❌ TWAP error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python twap.py SYMBOL SIDE TOTAL_QTY PARTS INTERVAL_SEC")
        print("Example: python twap.py BTCUSDT BUY 0.1 5 30")
        sys.exit(1)
    
    _, symbol, side, total_qty, parts, interval = sys.argv
    twap_order(symbol, side, float(total_qty), int(parts), int(interval))