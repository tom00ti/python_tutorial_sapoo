year = 2025

if year%400 == 0 :
    print("うるう年です")
elif year%100 == 0 :
    print("平年です")
elif year%4 == 0 :
    print("うるう年です")
else:
    print("平年です")


for num