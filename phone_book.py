phone_book = {}
entry = input()
my_entries = []
my_entries.append(entry)
while entry:
    entry = input()
    if entry:
        my_entries.append(entry)
        
for i in range(1, (int(my_entries[0]) + 1)):
    phone_book[(my_entries[i].split()[0])] = (my_entries[i].split()[1])

for i in range((int(my_entries[0])) + 1,(len(my_entries))):
    if my_entries[i] in phone_book:
        print(f"{my_entries[i]}={phone_book[my_entries[i]]}")
    else:
        print("Not found")