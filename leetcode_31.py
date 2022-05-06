# Python3 implementation of the approach

# Function to print the
# contents of an array
def printArr(arr, n):
    for i in range(n):
        print(arr[i], end=" ");


# Function to find the lexicographically
# smallest alternating array
def smallestArr(arr, n):
    # Sort the array
    arr.sort();

    # Swap every two consecutive elements
    for i in range(0, n - 1, 2):
        temp = arr[i];
        arr[i] = arr[i + 1];    
        arr[i + 1] = temp;

    # Print the re-arranged array
    printArr(arr, n);


# Driver code
if __name__ == '__main__':
    arr = [3, 2, 1, 4, 5];
    n = len(arr);
    smallestArr(arr, n);

# This code contributed by Rajput-Ji
