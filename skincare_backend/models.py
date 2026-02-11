class Product:
    def __init__(self,name,category,active_ingredients):
        self.name=name
        self.category=category
        self.active_ingredients=active_ingredients
class User:
    def __init__(self,name,age,skin_type,concerns):
        self.name=name
        self.age=age
        self.skin_type=skin_type
        self.concerns=concerns
        self.products=[]
    def add_product(self,product):
        self.products.append(product)
