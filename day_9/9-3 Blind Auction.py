from blind_auction_art import logo

bids = {}
winner_name = ""
highest_bid = 0
continue_bidding = True

while continue_bidding:
    bidder_name = input("Please enter your name:\n")
    bid = int(input("Please enter your bid $:\n"))
    bids.update({bidder_name: bid})

    if input("Please enter 'yes' if there are more bidders\
or 'no'if bidding is finished") == "no":
        continue_bidding = False

for bidder, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner_name = bidder
print(f"{winner_name} has won the auction, with a bid of {highest_bid}")
    
