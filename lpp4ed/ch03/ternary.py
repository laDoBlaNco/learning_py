order_total = 247

# classic if/else form
if order_total > 100:
    discount = 25
else:
    discount = 0
print(order_total,discount)

#we could write
discount=25 if order_total>100 else 0

print(order_total,discount)


