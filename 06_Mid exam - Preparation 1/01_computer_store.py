command = input()
total_price = 0
total_tax = 0

while command != 'special' and command != 'regular':

    current_price = float(command)
    current_tax = 0.2 * current_price

    if current_price < 0:
        print('Invalid price!')
        command = input()
        continue

    total_price += current_price
    total_tax += current_tax

    command = input()

if total_price == 0:
    print('Invalid order!')
elif command == 'special':
    discounted_price = 0.9 * (total_price + total_tax)

    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\nTaxes: {total_tax:.2f}$")
    print('-----------')
    print(f"Total price: {discounted_price:.2f}$")

else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\nTaxes: {total_tax:.2f}$")
    print('-----------')
    print(f"Total price: {total_tax + total_price:.2f}$")

