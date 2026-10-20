""" Assignment 1 - Simple Reflex Agent (Vacuum Cleaner) """

# Simple vacuum cleaner agent

rooms = {
    "A": input("Room A (clean/dirty): ").strip().lower(),
    "B": input("Room B (clean/dirty): ").strip().lower()
}

location = input("Vacuum starts at room A or B: ").strip().upper()

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
