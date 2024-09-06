
def bubble_sort(arr,n):
    for i in range(n - 1):
        j=i
        for j in range(n  - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap elements if the current

# Get the number of elements
n = int(input())

# Get space-separated input values and convert to a list of integers
arr = list(map(int, input().split()))

# Use the sorted function to sort the array
# sorted_arr = sorted(arr)


# Apply Bubble Sort
bubble_sort(arr,n)

# Print the sorted array
print("Sorted Array:", end=" ")
for i in arr:
    print(i,end=" ")
print()
