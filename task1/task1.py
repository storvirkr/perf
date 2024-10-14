import sys

def find_path(n, m):
    current = 1
    path = [current]
    
    while True:
        current = (current + m - 1) % n
        if current == 0:
            current = n
        
        if current == 1:
            break
        
        path.append(current)
    
    return path

def main():
    if len(sys.argv) != 3:
        print("Использование: python task1.py n m")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Ошибка: n and m должны быть числами")
        sys.exit(1)
    
    if n < 1 or m < 1:
        print("Ошибка: n and m должны быть положительными числами")
        sys.exit(1)
    
    path = find_path(n, m)
    print(''.join(map(str, path)))

if __name__ == "__main__":
    main()