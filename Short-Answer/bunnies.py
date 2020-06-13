def bunnyEars(bunnies, count=0):
    if bunnies == 0:
        print(count)
        return 0
    count += 1
    return 2 + bunnyEars(bunnies-1, count)

if __name__ == "__main__":
    for i in range(10):
        bunnyEars(i)