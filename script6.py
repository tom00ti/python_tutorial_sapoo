year = 2025

if year%400 == 0 :
    print("うるう年です")
elif year%100 == 0 :
    print("平年です")
elif year%4 == 0 :
    print("うるう年です")
else:
    print("平年です")

def hello():
    print("hello")

def add_numbers(a,b):
    c=a+b
    return c

def add_sub_numbers(a,b):
    c = a+b
    d = a-b
    return c,d


x,y = add_sub_numbers(10,100)
print(x)
#print(y)

class User:
    def __init__(self, name, mail_address, point):
        self.name = name
        self.mail_address =mail_address
        self.point = point
    def add_point(self, point):
        self.point += point

user_1 = User("")