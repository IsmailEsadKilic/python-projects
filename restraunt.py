from BuilderPattern import Burgir, BurgirBuilder, BurgirDirector

# Create a BurgirBuilder object

burgirBuilder1 = BurgirBuilder()
burgirBuilder2ElectricBoogaloo = BurgirBuilder()
burgirer = BurgirDirector(burgirBuilder2ElectricBoogaloo)

ardaburger = burgirer.makeBurgir()

esadburger = burgirBuilder1.addBuns("sussybuns").addMeat("pizza meat").addSauce("pink sauce").build()

print(esadburger)