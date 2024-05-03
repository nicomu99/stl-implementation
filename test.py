import numpy as np

# Example 2D array
array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])

# Get dimensions of the array
rows, cols = array_2d.shape

# Split the array into four equal parts
top_left = array_2d[:rows//2, :cols//2]
top_right = array_2d[:rows//2, cols//2:]
bottom_left = array_2d[rows//2:, :cols//2]
bottom_right = array_2d[rows//2:, cols//2:]

# Display the results
print("Top Left Quadrant:")
print(top_left)
print("\nTop Right Quadrant:")
print(top_right)
print("\nBottom Left Quadrant:")
print(bottom_left)
print("\nBottom Right Quadrant:")
print(bottom_right)
