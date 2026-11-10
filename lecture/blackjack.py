import random

# Dealer başlıyor
dealer = random.randint(1, 11)
dealer_total = dealer
print("Dealer has:", dealer_total)

# Oyuncu başlıyor
player_total = 0
for _ in range(3):
    player_total += random.randint(1, 11)

print("Player has:", player_total)

# Oyuncu sırası
while player_total < 22:
    user_instruction = input("Do you want to hit or stay: ").lower()

    if user_instruction == "hit":
        card = random.randint(1, 11)
        player_total += card
        print(f"You drew a {card}. Total: {player_total}")

        if player_total > 21:
            print("YOU BUSTED! Dealer wins.")
            break

    elif user_instruction == "stay":
        break

    else:
        print("Enter a valid instruction (hit/stay).")

# Dealer sırası
if player_total <= 21:
    while dealer_total < 17:
        card = random.randint(1, 11)
        dealer_total += card
        print(f"Dealer drew a {card}. Total: {dealer_total}")

    if dealer_total > 21:
        print("DEALER BUSTED! You win.")
    elif dealer_total >= player_total:
        print("DEALER WON.")
    else:
        print("YOU WON.")
