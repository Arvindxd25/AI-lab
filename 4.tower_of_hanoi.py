""" Assignment 4 - Tower of Hanoi """

# Tower of Hanoi using recursion

def tower_of_hanoi(disks, source, helper, destination):
    if disks == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(disks - 1, source, destination, helper)
    print("Move disk", disks, "from", source, "to", destination)
    tower_of_hanoi(disks - 1, helper, source, destination)

n = int(input("Enter number of disks: "))
tower_of_hanoi(n, "A", "B", "C")
print("Total moves:", 2 ** n - 1)
