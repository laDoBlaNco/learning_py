# discounts.py

from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)

products = [
    {"sku": 1, "expiration_date": today, "price": 100.0},
    {"sku": 2, "expiration_date": tomorrow, "price": 50.0},
    {"sku": 3, "expiration_date": today, "price": 20.0},
]

for product in products:
    print("processing sku", product["sku"])
    if product["expiration_date"] != today:
        continue
    product["price"] *= 0.8
    print("Sku", product["sku"], "price is now", product["price"])
