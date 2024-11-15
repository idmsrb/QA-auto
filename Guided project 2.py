width = input("Flag width:\n")
width = int(width)
half_width = width // 2
for _ in range(2):
    print('#' * half_width + '-' * half_width)
for _ in range(2):
    print('-' * width)