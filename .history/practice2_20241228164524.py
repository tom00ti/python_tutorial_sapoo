year = 2025

if year%400 == 0 :
        print("うるう年です")
if year%100 == 0 :
        print("うるう年です")
    elif year%400 == 0 :
        print("うるう年です")
else:
    print("平年です")