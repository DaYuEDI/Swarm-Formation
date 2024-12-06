import math
import matplotlib.pyplot as plt

def calculate_formation(base_point, side_length):
    """
    Calculate the coordinates of 6 points forming an equilateral triangle formation.
    
    Args:
    - base_point: Tuple (x, y) representing the top vertex of the formation (first layer point).
    - side_length: The side length of the equilateral triangles.
    
    Returns:
    - A list of tuples representing the coordinates of the points in the formation.
    """
    x1, y1 = base_point
    
    # Second layer (2 points)
    x2 = x1 - 0.5 * side_length
    y2 = y1 - math.sqrt(3) * 0.5 * side_length
    
    x3 = x1 + 0.5 * side_length
    y3 = y2
    
    # Third layer (3 points)
    x4 = x2 - 0.5 * side_length
    y4 = y2 - math.sqrt(3) * 0.5 * side_length
    
    x5 = x1
    y5 = y4
    
    x6 = x3 + 0.5 * side_length
    y6 = y2 - math.sqrt(3) * 0.5 * side_length
    
    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6)]

def plot_formation(points):
    """
    Plot the formation of points.
    
    Args:
    - points: A list of tuples representing the coordinates of the points.
    """
    x, y = zip(*points)

    plt.figure(figsize=(8, 8))
    plt.plot([x[0], x[1], x[2], x[0]], [y[0], y[1], y[2], y[0]], label="Top Triangle", color="blue")
    plt.plot([x[1], x[3], x[4], x[1]], [y[1], y[3], y[4], y[1]], label="Second Layer", color="orange")
    plt.plot([x[2], x[4], x[5], x[2]], [y[2], y[4], y[5], y[2]], label="Third Layer", color="green")

    # Mark points
    for i, (xi, yi) in enumerate(points, start=1):
        plt.scatter(xi, yi, color="black")
        plt.text(xi, yi, f"P{i}", fontsize=12, ha='center', va='bottom')

    # Configure plot
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.grid(color="gray", linestyle="--", linewidth=0.5)
    plt.title("Equilateral Triangle Formation")
    plt.legend()
    plt.axis("equal")
    plt.show()

# Example usage
base_point = (0, 0)  # Starting point of the top layer
side_length = 0.2  # Side length of the triangle
points = calculate_formation(base_point, side_length)

print("Coordinates of the 6 points:")
for i, point in enumerate(points, start=1):
    print(f"Point {i}: {point}")

# Plot the formation
plot_formation(points)
