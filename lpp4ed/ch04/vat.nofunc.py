# vat.nofunc.py

# improves traceability.

# Here are four professional ways to do the same thing and all are valid.
# if we needed to trace everywhere in a program where this calculation is
# made, how hard would it be?

price = 100
final_price1 = price * 1.2
final_price2 = price + price / 5.0
final_price3 = price * (100 + 20) / 100.0
final_price4 = price + price * 0.2

print(final_price1, final_price2, final_price3, final_price4)
