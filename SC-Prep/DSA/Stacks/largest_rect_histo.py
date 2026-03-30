# height = heights[popped_index]
# right  = current index i
# left   = stack[-1] + 1  if stack else 0
# width  = right - left
# area   = height × width

def largest_rect_area(heights):
    stack = []
    max_area = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            popped_index = stack.pop()
            height = heights[popped_index]
            right = i
            if not stack:
                left = 0
            else:
                left = stack[-1] + 1
            width = right - left
            area = height * width
            max_area = max(max_area, area)
        stack.append(i)

    while stack:
        popped_index = stack.pop()
        height = heights[popped_index]
        right = len(heights)
        if not stack:
            left = 0
        else:
            left = stack[-1] + 1
        width = right - left
        area = height * width
        max_area = max(max_area, area)
    return max_area
        

    