from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

auction_house = {}
more_bidding = True

def create_bidder():
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  auction_house[name] = bid

def highest_bidder(bidders):
  highest_bid = 0
  winner = ''
  for bidder in bidders:
    bid_amount = bidders[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}!")

while more_bidding == True:
  create_bidder()
  if input("Are there any other bidders? Type 'yes' or 'no'. \n") == 'no':
    more_bidding = False

highest_bidder(auction_house)