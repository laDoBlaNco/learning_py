# vat.function.py

# how much easier would it be to track down this code
def calculate_price_with_vat(price,vat):
    return price*(100+vat)/100

print(calculate_price_with_vat(100.00,20))
