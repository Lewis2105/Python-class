
amount_purchase = float(input("Enter the amount of purchase: "))

if amount_purchase > 1000:
    discount = amount_purchase * 0.05
    final_amount = amount_purchase - discount
    print(f"A 5% discount is applied. Final amount: KSH {final_amount:.2f}")
else:
    final_amount = amount_purchase
    print(f"No discount applied. Final amount: KSH {final_amount:.2f}")