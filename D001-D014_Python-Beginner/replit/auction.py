print("Welcome to the secret auction program.")
more_participants = True
bidders = {}

def find_highest_bidder(bidders_list):
    biggest_bid = 0
    for person in bidders_list:
        if bidders_list[person] > biggest_bid:
            biggest_bid = bidders_list[person]
            winner = person
    print(f"The winner is {winner} with a bid of ${biggest_bid}")
    
while more_participants:
    name = input("What is your name?: ")
    value = int(input("What is your bid?: $"))
    bidders[name]=value
    bidder_situation = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if bidder_situation == "no":
        more_participants = False
        find_highest_bidder(bidders)
