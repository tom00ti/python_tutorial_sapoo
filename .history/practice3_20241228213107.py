class Product:
    def __init__(self,id,name,price, purchase_price):
            self.id = id
            self.name = name
            self.price = price
            self.purchese_price = purchase_price
    def cost_rate(self):
          rate = (self.purchese_price/self.price)*100

product_1 = Product("A0001","半袖クールTシャツ",5000,2250)