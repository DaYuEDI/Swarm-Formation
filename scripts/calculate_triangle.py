import math
import matplotlib.pyplot as plt


def rotate_point(point, base_point, angle):
    """旋转点绕基点旋转指定角度"""
    x, y = point
    x0, y0 = base_point
    x_rot = (x - x0) * math.cos(angle) - (y - y0) * math.sin(angle) + x0
    y_rot = (x - x0) * math.sin(angle) + (y - y0) * math.cos(angle) + y0
    return x_rot, y_rot


def calculate_formation(base_point, side_length, rotation_angle):
    """
    计算旋转后的等边三角形队形的点坐标
    """
    x1, y1 = base_point

    # 原始坐标（未旋转）
    points = [(x1, y1),
              (x1 - 0.5 * side_length, y1 - math.sqrt(3) * 0.5 * side_length),
              (x1 + 0.5 * side_length, y1 - math.sqrt(3) * 0.5 * side_length),
              (x1 - side_length, y1 - math.sqrt(3) * side_length),
              (x1, y1 - math.sqrt(3) * side_length),
              (x1 + side_length, y1 - math.sqrt(3) * side_length)]

    # 应用旋转矩阵
    rotated_points = [
        rotate_point(p, base_point, rotation_angle) for p in points
    ]
    return rotated_points


def plot_formation(points):
    """
    绘制队形
    """
    x, y = zip(*points)
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, "o-", color="black", label="Formation")

    # 标记点
    for i, (xi, yi) in enumerate(points, start=1):
        plt.text(xi, yi, f"P{i}", fontsize=12, ha='center', va='bottom')

    # 配置图形
    plt.axhline(0, color="gray", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="gray", linewidth=0.5, linestyle="--")
    plt.grid(color="lightgray", linestyle="--", linewidth=0.5)
    plt.title("Equilateral Triangle Formation with Heading")
    plt.legend()
    plt.axis("equal")
    plt.show()


# 示例使用
base_point = (0, 0)
side_length = 0.2
rotation_angle = math.radians(-45)  # 旋转角度，45度
points = calculate_formation(base_point, side_length, rotation_angle)

# 打印结果
print("旋转后的6个点坐标：")
for i, point in enumerate(points, start=1):
    print(f"Point {i}: {point}")

# 绘制队形
plot_formation(points)
