year = 2025

if year%400 == 0 :
    print("うるう年です")
elif year%100 == 0 :
    print("平年です")
elif year%4 == 0 :
    print("うるう年です")
else:
    print("平年です")


for number in range(1,101):
    if number % 15 == 0:
        print("fizzBuzz")
    elif number%3 ==0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)