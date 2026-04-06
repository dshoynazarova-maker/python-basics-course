print()
print("=== Coffee Shop Order System ===\nEnter drink sizes: small, medium, or large\nType 'done' when finished ordering")
total=0
while True:
    print()
    size=input('Enter drink size: ')
    if size=='done':
        break
    if size=='small':
        price = 3.50
    elif size=='medium':
        price = 4.50
    elif size=='large':
        price = 5.50
    else:
        print('We have not this this')
        continue
    total+=price
    print(f'Price: ${price:.2f}')
    print(f'Current total: ${total:.2f}')
if total >=20:
    loyalty= 3.00
else: 
    loyalty=0.00
final_total=total-loyalty

print('\n=== Order Summary ===\n')
print(f'Subtotal: ${total:.2f}')
print(f"Loyalty Discount: -${loyalty:.2f}")
print(f'Final Total: ${final_total:.2f}\nThank you for your order!')