from replit import clear
from art import logo
print(logo)
bids = {}
bidding_finished = False
def highest_bid(bidding_record):
  highest_amount = 0
  winner=""
  for bidder in bidding_record:
    bidding_amount = bidding_record[bidder]
    if bidding_amount>highest_amount:
      highest_amount = bidding_amount
      winner = bidder
  print(f"The Winner is {winner} with a bid of ${highest_amount}")
while not bidding_finished:
  print("Welcome to the Noiseless-Auction\n")
  name = input("please enter your name to continue\n")
  amount = int(input("please enter your bid amount in $ "))
  bids[name]=amount
  is_continue = input("Are there any other bidders..? type 'yes' or 'no'").lower()
  if is_continue =="no":
    highest_bid(bids)
    bidding_finished= True
  elif is_continue == "yes":
    clear()

