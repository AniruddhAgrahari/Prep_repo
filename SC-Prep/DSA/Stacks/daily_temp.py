# LC 739 - Daily Temperatures
# Pattern: Monotonic Stack (Decreasing)
# Time Complexity: O(n) - each element pushed and popped at most once
# Space Complexity: O(n) - stack + result array

def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for day in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[day]:
            popped = stack.pop()
            result[popped] = day - popped
        stack.append(day)


    return result



print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# expected: [1, 1, 4, 2, 1, 1, 0, 0]