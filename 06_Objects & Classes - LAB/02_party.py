class Party:
    def __init__(self):             #init does not require input of other info
        self.peoples_list = []

party1 = Party()

command = input()
while command != "End":
    party1.peoples_list.append(command)
    command = input()

print(f"Going: {', '.join(party1.peoples_list)}")
print(f'Total: {len(party1.peoples_list)}')