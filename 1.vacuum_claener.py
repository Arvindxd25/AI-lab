""" Assignment 1 - Simple Reflex Agent (Vacuum Cleaner) """

# Simple Vacuum Cleaner Agent

rooms = {
    "A": input("Room A (clean/dirty): ").strip().lower(),
    "B": input("Room B (clean/dirty): ").strip().lower()
}

# Validate room status
while rooms["A"] not in ["clean", "dirty"]:
    rooms["A"] = input("Invalid input! Enter Room A (clean/dirty): ").strip().lower()

while rooms["B"] not in ["clean", "dirty"]:
    rooms["B"] = input("Invalid input! Enter Room B (clean/dirty): ").strip().lower()

# Get and validate starting location
location = input("Vacuum starts at room A or B: ").strip().upper()

while location not in ["A", "B"]:
    location = input("Invalid input! Enter A or B: ").strip().upper()

# Vacuum cleaner agent
while rooms["A"] == "dirty" or rooms["B"] == "dirty":
    print("\nVacuum is in room", location)

    if rooms[location] == "dirty":
        print("Action: Suck")
        rooms[location] = "clean"

    elif location == "A":
        print("Action: Move Right")
        location = "B"

    else:
        print("Action: Move Left")
        location = "A"

print("\nBoth rooms are clean. Vacuum stops.")
