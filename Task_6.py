ticket = int(input("Введите число вашего билета: "))
ticket1 = ticket % 1000
ticket2 = ticket // 1000
a = 0
b = 0
while ticket1 > 0:
    x = ticket1 % 10
    a = a + x
    ticket1 = ticket1 // 10

while ticket2 > 0:
    x = ticket2 % 10
    b = b + x
    ticket2 = ticket2 // 10

if a == b:
    print("YES!")
else:
    print("NO!")