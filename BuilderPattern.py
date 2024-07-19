class Burgir():
    def __init__(self):
        self.buns = None
        self.meat = None
        self.cheese = None
        self.toppings = None
        self.sauce = None
    
    def setBuns(self, buns):
        self.buns = buns
    
    def setMeat(self, meat):
        self.meat = meat
    
    def setCheese(self, cheese):
        self.cheese = cheese

    def setToppings(self, toppings):
        self.toppings = toppings

    def setSauce(self, sauce):
        self.sauce = sauce

    def __str__(self):
        return f"Buns: {self.buns}\nMeat: {self.meat}\nCheese: {self.cheese}\nToppings: {self.toppings}\nSauce: {self.sauce}"

class BurgirBuilder():

    def __init__(self):
        self.burgir = Burgir()

    def addBuns(self, buns):
        self.burgir.setBuns(buns)
        return self
    
    def addMeat(self, meat):
        self.burgir.setMeat(meat)
        return self
    
    def addCheese(self, cheese):
        self.burgir.setCheese(cheese)
        return self
    
    def addToppings(self, toppings):
        self.burgir.setToppings(toppings)
        return self
    
    def addSauce(self, sauce):
        self.burgir.setSauce(sauce)
        return self
    
    def build(self):
        return self.burgir
    
burgirBuilder = BurgirBuilder()
sussyburger = burgirBuilder.addBuns("bunbuns").addMeat("meat meat").addSauce("sauce sauce").build()
burburgir = burgirBuilder.addBuns("bunbuns").addMeat("meat meat").addSauce("sauce sauce").build()
awesomeburger = burgirBuilder.addBuns("awesomebuns").addMeat("awesome meat").addSauce("awesome sauce").build()
huggyburger = burgirBuilder.addBuns("huggybuns").addMeat("huggy meat").addSauce("huggy sauce").build() 

array = [
    sussyburger,
    burburgir,
    awesomeburger,
    huggyburger
]
print(array)

# class BurgirDirector():
    
#         def __init__(self, builder):
#             self.builder = builder
        
#         def makeBurgir(self):
#             self.builder.addBuns("Sesame Seed Buns")
#             self.builder.addMeat("Beef")
#             self.builder.addCheese("American Cheese")
#             self.builder.addToppings("Lettuce, Tomato, Onion")
#             self.builder.addSauce("Ketchup, Mustard, Mayo")
#             return self.builder.build()


