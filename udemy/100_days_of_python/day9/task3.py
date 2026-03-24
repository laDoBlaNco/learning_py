# task3.py

# Final Project - Silent Auctions

import art
from subprocess import run

print(art.logo)

bids = {}

finished_bidding = False

while not finished_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if more_bidders == "no":
        finished_bidding = True
    
    run(['clear']) 

big_bidder = None
big_bid = None
for key in bids:
    if big_bidder is None or bids[key] > big_bid:
        big_bidder = key
        big_bid = bids[key]
print(f"The winner is {big_bidder} with a bid of ${big_bid}.")
# print(bids)
