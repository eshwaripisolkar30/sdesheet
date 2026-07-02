
def generatePermutations(res, arr, idx):

    # Base case
    if idx == len(arr) - 1:
        res.append(arr[:])
        return

    # Generate permutations by swapping
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]

        # Recursive call
        generatePermutations(res, arr, idx + 1)

        # Backtrack
        arr[idx], arr[i] = arr[i], arr[idx]


# Function to find the next permutation
def nextPermutation(arr):
    res = []

    # Generate all permutations
    generatePermutations(res, arr, 0)

    # Remove duplicate permutations (if any) and sort
    res = sorted(set(tuple(x) for x in res))
    res = [list(x) for x in res]

    # Find current permutation
    for i in range(len(res)):
        if res[i] == arr:
            if i == len(res) - 1:
                arr[:] = res[0]
            else:
                arr[:] = res[i + 1]
            break


# Driver Code
if __name__ == "__main__":

    # Input number of elements
    n = int(input("Enter the number of elements: "))

    # Input array
    print(f"Enter {n} elements separated by spaces:")
    arr = list(map(int, input().split()))

    # Validate input
    if len(arr) != n:
        print("Error: Number of elements entered does not match n.")
    else:
        # Find next permutation
        nextPermutation(arr)

        # Display result
        print("Next Permutation:")
        print(*arr)