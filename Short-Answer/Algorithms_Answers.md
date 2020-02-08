#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(C).  Once n > 0, the while loops stops.


b)  O(n).  Because j is being set to 1, the for loop is the only driver of operations n > 1


c)  O(n^1) = O(n).  One recursive call per n

## Exercise II

The floors are effectively a sorted list where n = 1 to max floor.  Drop an egg in the middle. If it breaks, search the bottom middle.  If not, the top middle.  Split, and repeat.

def find_floor(height, f):
    if egg_breaks(height+1):
        return height
    else:
        if egg_breaks(height, f):
            find_floor(split_height[0], f)
        else:
            find_floor(split_height[1], f)


We are splitting the list each time.  This is a lot like a binary search, O(log n)