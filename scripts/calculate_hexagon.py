import numpy as np
import matplotlib.pyplot as plt

def GenerateHexagonVertices(radius=1.0):
    """
    生成正六边形顶点坐标
    
    Args:
    - radius: 正六边形的半径（从中心到顶点的距离）
    
    Returns:
    - x, y: 正六边形顶点的坐标数组
    """
    angles = np.linspace(0, 2 * np.pi, 7)  # 包含起点与终点
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    return x, y

def PlotHexagon(x, y):
    """
    绘制正六边形
    
    Args:
    - x, y: 正六边形顶点的坐标数组
    """
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, "o-", color="blue", label="Hexagon")

    # 标记顶点坐标
    for i, (xi, yi) in enumerate(zip(x, y), start=1):
        plt.text(xi, yi, f"P{i}", fontsize=12, ha='center', va='bottom')
        print(f"顶点 P{i}: ({xi:.2f}, {yi:.2f})")
    
    # 配置图形
    plt.axhline(0, color="gray", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="gray", linewidth=0.5, linestyle="--")
    plt.grid(color="lightgray", linestyle="--", linewidth=0.5)
    plt.title("Regular Hexagon")
    plt.legend()
    plt.axis("equal")
    plt.show()

# 示例使用
radius = 0.2  # 半径
x, y = GenerateHexagonVertices(radius)
PlotHexagon(x, y)
