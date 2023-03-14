a = int(input("Введите трёхзначное число: "))
b = 0
while a > 0:
    x = a % 10
    b = b + x
    a = a // 10
print(b)