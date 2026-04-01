# coupons.dict.py

customers = [
    dict(id=1, total=200, coupon_code="F20"),
    dict(id=2, total=150, coupon_code="P30"),
    dict(id=3, total=100, coupon_code="P50"),
    dict(id=4, total=110, coupon_code="F15"),
]
discounts = dict(
    F20=(0.0, 20.0),
    P30=(0.3, 0.0),
    P50=(0.5, 0.0),
    F15=(0.0, 15.0),
)

for cust in customers:
    code = cust["coupon_code"]
    percent, fixed = discounts.get(code, (0.0, 0.0))
    cust["discount"] = percent * cust["total"] + fixed

for cust in customers:
    print(cust["id"], cust["total"], cust["discount"])

# “lines shorter, but more importantly, we gained
# a lot in readability, as the body of the for loop
# is now just three lines long and easy to
# understand. The key idea here is to use a
# dictionary as a lookup table”

