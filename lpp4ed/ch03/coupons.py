# coupons.py

# In this example, we want to show you a technique
# called a lookup table, which we are very fond of.
# We will start by simply writing some code that
# assigns a discount to customers based on their
# coupon value. We will keep the logic down to a
# minimum here—remember that all we really care about
# is understanding conditionals and loops:

customers = [
    dict(id=1, total=200, coupon_code="F20"),
    dict(id=2, total=150, coupon_code="P30"),
    dict(id=3, total=100, coupon_code="P50"),
    dict(id=4, total=110, coupon_code="F15"),
]

for cust in customers:
    match cust["coupon_code"]:
        case "F20":
            cust["discount"] = 20.0
        case "F15":
            cust["discount"] = 15.0
        case "P30":
            cust["discount"] = cust["total"] * 0.3
        case "P50":
            cust["discount"] = cust["total"] * 0.5
        case _:
            cust["discount"] = 0.0

for cust in customers:
    print(cust["id"], cust["total"], cust["discount"])


# This code is simple to understand, but all
# those match cases are cluttering the logic.
# Adding more coupon codes requires adding
# additional cases and implementing the discount
# calculation for each case. The discount
# calculation is very similar in most cases,
# which makes the code repetitive and violates
# the Don’t Repeat Yourself (DRY) principle. In
# cases like this, you can use a dictionary to your
# advantage, like this:”
