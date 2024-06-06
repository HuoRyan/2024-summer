dealer_hand_input = input("Enter the dealer's hand (e.g., A K 5): ")
dealer_hand = dealer_hand_input.split()  

total = 0
aces = 0

for card in dealer_hand:
    if card in "JQK": 
        total += 10
    elif card == "A":  
        aces += 1
    else: 
        total += int(card)

for _ in range(aces):
    if total + 11 <= 21: 
        total += 11
    else: 
        total += 1

if total > 21:
    print("Bust")
elif total >= 17:
    print("Stay")
else:
    print("Hit")