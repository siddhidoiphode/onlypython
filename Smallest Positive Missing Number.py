class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Replace negatives and zeros with a large number
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1

        # Step 2: Mark the presence of elements
        for i in range(n):
            num = abs(arr[i])
            if 1 <= num <= n:
                arr[num - 1] = -abs(arr[num - 1])

        # Step 3: Find the first missing positive
        for i in range(n):
            if arr[i] > 0:
                return i + 1

        # Step 4: If all numbers are present
        return n + 1

class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Replace negatives and zeros with a large number
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1

        # Step 2: Mark the presence of elements
        for i in range(n):
            num = abs(arr[i])
            if 1 <= num <= n:
                arr[num - 1] = -abs(arr[num - 1])

        # Step 3: Find the first missing positive
        for i in range(n):
            if arr[i] > 0:
                return i + 1

        # Step 4: If all numbers are present
        return n + 1
