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

def setup_grid_orders(symbol, lower_price, upper_price, grid_levels, quantity_per_level):
    try:
        client = Client(API_KEY, API_SECRET, testnet=True)
        server_time = client.get_server_time()
        local_time = int(time.time() * 1000)
        time_offset = local_time - server_time['serverTime']
        client.timestamp_offset = -time_offset - 1000
        
        
        price_step = (upper_price - lower_price) / (grid_levels - 1)
        
        print(f"🎯 Setting up Grid Trading Strategy:")
        print(f"   Symbol: {symbol}")
        print(f"   Price Range: {lower_price} - {upper_price}")
        print(f"   Grid Levels: {grid_levels}")
        print(f"   Price Step: {price_step}")
        print(f"   Quantity per level: {quantity_per_level}\n")
        
        buy_orders = []
        sell_orders = []
        
        for i in range(grid_levels):
            price = lower_price + (i * price_step)
            
            if i < grid_levels // 2:
                try:
                    order = client.futures_create_order(
                        symbol=symbol.upper(),
                        side=SIDE_BUY,
                        type=ORDER_TYPE_LIMIT,
                        quantity=quantity_per_level,
                        price=round(price, 2),
                        timeInForce=TIME_IN_FORCE_GTC
                    )
                    buy_orders.append(order)
                    logging.info(f"Grid BUY order at {price}: {order.get('orderId')}")
                    print(f"✅ BUY order placed at ${price:.2f} | Order ID: {order.get('orderId')}")
                except Exception as e:
                    print(f"❌ Failed to place BUY at ${price:.2f}: {e}")
            
            else:
                try:
                    order = client.futures_create_order(
                        symbol=symbol.upper(),
                        side=SIDE_SELL,
                        type=ORDER_TYPE_LIMIT,
                        quantity=quantity_per_level,
                        price=round(price, 2),
                        timeInForce=TIME_IN_FORCE_GTC
                    )
                    sell_orders.append(order)
                    logging.info(f"Grid SELL order at {price}: {order.get('orderId')}")
                    print(f"✅ SELL order placed at ${price:.2f} | Order ID: {order.get('orderId')}")
                except Exception as e:
                    print(f"❌ Failed to place SELL at ${price:.2f}: {e}")
        
        print(f"\n✅ Grid setup complete!")
        print(f"   Buy orders: {len(buy_orders)}")
        print(f"   Sell orders: {len(sell_orders)}")
        
        return buy_orders, sell_orders
        
    except Exception as e:
        logging.error(f"Grid strategy error: {e}")
        print(f"❌ Grid error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python grid_strategy.py SYMBOL LOWER_PRICE UPPER_PRICE LEVELS QTY")
        print("Example: python grid_strategy.py BTCUSDT 58000 62000 10 0.01")
        sys.exit(1)
    
    _, symbol, lower, upper, levels, qty = sys.argv
    setup_grid_orders(symbol, float(lower), float(upper), int(levels), float(qty))