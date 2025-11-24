import pandas as pd
from order_bot import OrderBot
import json

# Load config
with open("config.json", "r") as f:
    cfg = json.load(f)

# Load Excel file
df = pd.read_excel("items.xlsx")  # Columns: ItemName, Quantity, Price

def process_order():
    bot = OrderBot()
    bot.open_app(cfg["app_url"])
    bot.login(cfg["username"], cfg["password"])

    orders_list = []

    for _, row in df.iterrows():
        bot.place_order(row["ItemName"], row["Quantity"], row["Price"])
        orders_list.append({
            "ItemName": row["ItemName"],
            "Quantity": row["Quantity"],
            "Price": row["Price"]
        })

    # Show bill in a new tab
    bot.show_bill_tab(orders_list)

    # Wait for user interaction
    input("Press Enter after downloading the bill to close the browser...")

    bot.close()
    print("Order batch completed.")

if __name__ == "__main__":
    print("\nRunning Order Process...")
    process_order()
