print("=== FAMILY GROCERY COST REPORT ===")

price_item_1 = 12.50
price_item_2 = 4.25
price_item_3 = 8.99
target_item  = 6.50

incorrect_total = 45.00
incorrect_count = 5
actual_correct_item_price = 15.75

discount_rate = 0.15
discounted_total = (price_item_1 + price_item_2) * (1 - discount_rate)

items_bought = 14
pack_size = 4

remainder_items = items_bought % pack_size
is_evenly_divisible = (items_bought % pack_size == 0)

corrected_total = incorrect_total + actual_correct_item_price
corrected_mean = corrected_total / incorrect_count

comparison_result = ""
if target_item > price_item_1 and target_item > price_item_2 and target_item > price_item_3:
    comparison_result = "Target item is the most expensive."
elif target_item < price_item_1 and target_item < price_item_2 and target_item < price_item_3:
    comparison_result = "Target item is the cheapest."
else:
    comparison_result = "Target item falls in the middle range."

print("\n" + "="*50)
print(f"{'CHALLENGE METRIC':<30} | {'CALCULATED RESULT':<20}")
print("="*50)
print(f"{'Part 1: Discounted Total':<30} | ${discounted_total:.2f}")
print(f"{'Part 2: Remainder Items':<30} | {remainder_items} left over")
print(f"{'Part 3: Corrected Mean':<30} | ${corrected_mean:.2f}")
print(f"{'Part 4: Price Evaluation':<30} | {comparison_result}")
print("="*50)