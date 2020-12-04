for l in range(0,5):
    if l == 0 or l == 4:
        for c in range(0, 5):
            print(f"X", end="")
        print()
    else:
        print(f"X", end="")
        print(f" ", end="")
        print(f" ", end="")
        print(f" ", end="")
        print(f"X", end="")
        print()