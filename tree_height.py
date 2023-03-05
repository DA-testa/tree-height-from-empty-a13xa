# python3
# 221RDB069 Aleksandra Červinska 12.grupa

import sys
import threading
#import numpy


def compute_height(n, parents):
    # Write this function
    def get_height(node):
        if all_h[node] != 0:
            return all_h[node]
        if parents[node] == -1:
            all_h[node] = 1
        else:
            all_h[node] = 1 + get_height(parents[node])
        return all_h[node]

    max_height = 0
    all_h = [0] * n
    # Your code here
    for i in range(n):
        max_height = max(max_height, get_height(i))
    return max_height


def main():
    # implement input form keyboard and from files
    ievade = input("Input I or F: ")
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # if ievade.upper() not in ["I", "F"]:
    #     print("Wrong input")
    #     return

    if ievade.upper() == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        fails = "./test/" + input("Input filename(01-25): ")
        if "a" in fails:
            print("Wrong file name")
            return
        # try:
        with open(fails, "r") as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
        # except FileNotFoundError:
        #     print("File not found")
        #     return
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    height = compute_height(n, parents)
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))
