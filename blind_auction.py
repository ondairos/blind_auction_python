#create the customers dictionary
customers = {}

still_playing = True

#function that finds the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner= bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while still_playing:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bidding price?: $"))
    customers[name] = bid_price
        #ask the user for their name and bid price
    answer = input("Is there an other bidder? Type yes or no \n")
    if answer == "no":
        still_playing = False
        find_highest_bidder(customers)
    elif answer == "yes":
        print("Next bidder...")