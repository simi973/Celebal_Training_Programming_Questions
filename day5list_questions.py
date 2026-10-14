# PROG 3: Shuffle Card
import random
card_point = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_signs = ['HEART', 'CLUB', 'DIAMOND', 'SPADE']
deck = []
for sign in card_signs:
    for point in card_point:
        deck.append(sign + "-" + point)
print("Initial Deck:")
for i, card in enumerate(deck, start=1):
    print("Position", i, ":", card)
king_positions = [i for i, card in enumerate(deck, start=1) if card.endswith("-K")]
print("\nInitial positions of all Kings:")
print(king_positions)
random.shuffle(deck)
print("\nShuffled Deck:")
for i, card in enumerate(deck, start=1):
    print("Position", i, ":", card)
king_positions = [i for i, card in enumerate(deck, start=1) if card.endswith("-K")]
print("\nShuffled positions of all Kings:")
print(king_positions)


# PROG 4: Execution Time Calculation
import random
import time
def generate_numbers(n):
    return [random.randint(1, 100) for i in range(n)]
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def remove_primes(numbers):
    return [num for num in numbers if not is_prime(num)]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,31, 37, 41, 43, 47, 53, 59, 61, 67,71, 73, 79, 83, 89, 97]
def remove_primes_optimized(numbers):
    return [num for num in numbers if num not in prime_numbers]
sizes = [100, 10000, 100000]
for n in sizes:
    print("\nComputing execution time for list size:", n)
    start = time.time()
    numbers = generate_numbers(n)
    generation_time = time.time() - start
    start = time.time()
    result1 = remove_primes(numbers)
    normal_time = time.time() - start
    start = time.time()
    result2 = remove_primes_optimized(numbers)
    optimized_time = time.time() - start
    print("Time to generate random numbers:", round(generation_time, 6), "seconds")
    print("Normal prime-checking time:", round(normal_time, 6), "seconds")
    print("Optimized removal time:", round(optimized_time, 6), "seconds")
    print("Time difference:", round(normal_time - optimized_time, 6), "seconds")
    if optimized_time < normal_time:
        print("Optimization improved execution time.")
    else:
        print("No improvement in this run.")



# PROG 5: Retail Invoicing App

import random
items = ["Banana", "Masala", "Tomato", "Rice", "Milk",
         "Soap", "Bread", "Oil", "Sugar", "Tea",
         "Biscuits", "Shampoo", "Potato", "Juice", "Detergent"]
prices = [15, 200, 10, 60, 30, 40, 35, 150, 45, 100,
          25, 120, 20, 50, 90]
gst = [0.05, 0.12, 0.05, 0.05, 0.05, 0.05, 0.12, 0.12,
       0.05, 0.12, 0.12, 0.05, 0.05, 0.12, 0.05]
buyer = input("Enter the buyer name: ")
selected = random.sample(range(15), 3)
total = 0
total_gst = 0
print("\nRetail Invoicing App")
print("--------------------------------")
print("Buyer Name:", buyer)
print("--------------------------------")
for i in selected:
    qty = random.randint(1, 5)
    amount = prices[i] * qty
    tax = amount * gst[i]
    total += amount
    total_gst += tax
    print(items[i], "Qty:", qty, "Price:", amount)
print("--------------------------------")
print("Total: Rs", round(total, 2))
print("GST: Rs", round(total_gst, 2))
print("Total Billing: Rs", round(total + total_gst, 2))