import sys
import math

def read_circle_data(filename):
    with open(filename, 'r') as f:
        x, y = map(float, f.readline().split())
        r = float(f.readline())
    return x, y, r

def read_points(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

def calculate_position(cx, cy, r, px, py):
    distance = math.sqrt((px - cx)**2 + (py - cy)**2)
    if math.isclose(distance, r):
        return 0  # точка на окружности
    elif distance < r:
        return 1  # точка внутри
    else:
        return 2  # точка снаружи

def main(circle_file, points_file):
    cx, cy, r = read_circle_data(circle_file)
    points = read_points(points_file)

    for px, py in points:
        position = calculate_position(cx, cy, r, px, py)
        print(position)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py circle_file points_file")
        sys.exit(1)
    
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    main(circle_file, points_file)