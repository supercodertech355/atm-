print("=== ATM cash Dispenser ===")
print("Dispensing cash for customers one at a time.\n")

notes = [100,50,20,10,5,1]
customer_served = 0
total_dispensed = 0
log = []

serving = True
while serving:
    name = input("enter customer name:")
    amount = int(input(f"hello{name}! enter withdrawel amount:"))

    if amount <= 0:
        print("invalid amount")
        continue

    print(f"\nDispensing {amount}units for {name}")
    print("-" * 30)

    remaining = amount
    i = 0
    used = {}

    while i < len(notes):
        count = remaining // notes[i]
        if count > 0 :
            print(f"{count} x {notes[i]}-unit note(s) = {count * notes[i]}")

            used[notes[i]] = count
            remaining -= count * notes[i]
        i+=1

    customer_served +=1
    total_dispensed+= amount
    log.append({"name":name, "used":used})
    print( "please collect your cash")

    again = input("next customer? (yes / no:").strip().lower()
    if again!="yes":
      serving = False
print("\n=== Daily Denomination Report ===")
for note in notes:
    total_notes = 0
    # Inner for loop — checks every customer's usage of this denomination
    for entry in log:
        total_notes += entry["used"].get(note, 0)
    if total_notes > 0:
        print(f"  {note}-unit notes dispensed today : {total_notes}")

print(f"\nCustomers served : {customer_served}")
print(f"Total dispensed  : {total_dispensed} units")
print("ATM session closed. Goodbye!")
            