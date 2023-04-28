# Project 8 - Blind Auction
"""
Idea:
Write a program that will be able to create an auction and invite bidders to participate by placing bids. The highest bidder will win. 
"""

# Project 8 - Solution
import os
import auction_art

print(auction_art.logo)
bidders = {}
while (True):
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidders[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls')
    if others == 'no':
        break

highest_bid = 0
name = ""
for key in bidders:
    new_bid = int(bidders[key])
    if new_bid > highest_bid:
        name = key
        highest_bid = new_bid

print(f"The winner is {name} with a bid of ${highest_bid}.")