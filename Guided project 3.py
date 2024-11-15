width = input("Flag width:\n")
width = int(width)
height = input("Flag height:\n")
height = int(height)
half_width = width // 2
true_height = height // 2
for _ in range(true_height):
    print('#' * half_width + '-' * half_width)
for _ in range(true_height):
    print('-' * width)