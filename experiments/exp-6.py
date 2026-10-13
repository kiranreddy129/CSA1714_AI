a = input("Enter status of Room A (Clean/Dirty): ").lower()
b = input("Enter status of Room B (Clean/Dirty): ").lower()
pos = input("Enter vacuum position (A/B): ").upper()

if pos == "A":
    if a == "dirty":
        print("Room A cleaned")
        a = "clean"
    print("Move to Room B")
    if b == "dirty":
        print("Room B cleaned")
        b = "clean"
else:
    if b == "dirty":
        print("Room B cleaned")
        b = "clean"
    print("Move to Room A")
    if a == "dirty":
        print("Room A cleaned")
        a = "clean"

print("Final Status:")
print("Room A:", a)
print("Room B:", b)
