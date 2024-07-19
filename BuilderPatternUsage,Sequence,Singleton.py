from BuilderPattern import Burgir, BurgirBuilder, BurgirDirector

class SussySequence():

    def __init__(self, array):
        self.array = array

    def add(self, item):
        print("Adding item {item} to array {array}".format(item=item, array=self.array))
        self.array.append(item)

    def iter(self):
        self.start = 0
        self.current = self.start
        self.end = len(self.array) - 1
        return self
    
    def next(self):
        if self.current <= self.end:
            result = self.array[self.current]
            self.current += 1
            return result
        else:
            self.current = 0
            return self.array[self.current]

burgirBuilder = BurgirBuilder()
sussyburger = burgirBuilder.addBuns("bunbuns").addMeat("meat meat").addSauce("sauce sauce").build()
burburgir = burgirBuilder.addBuns("bunbuns").addMeat("meat meat").addSauce("sauce sauce").build()
awesomeburger = burgirBuilder.addBuns("awesomebuns").addMeat("awesome meat").addSauce("awesome sauce").build()
huggyburger = burgirBuilder.addBuns("huggybuns").addMeat("huggy meat").addSauce("huggy sauce").build() 

def new_func(SussySequence, sussyburger, burburgir, awesomeburger, huggyburger):
    sequence = SussySequence([
        sussyburger,
        burburgir
    ])

    sequence.add(awesomeburger)
    sequence.add(huggyburger)

    print(sequence.array)

    sequenceIter = sequence.iter()
    print(sequenceIter.start)
    print(sequenceIter.end)

    for i in range(0, 10):
        print(sequenceIter.current)
        print(sequenceIter.next())

#new_func(SussySequence, sussyburger, burburgir, awesomeburger, huggyburger)

class SussyStack ():
    def __init__(self, array):
        self.array = []

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        # Initialize the Singleton instance here
        self.value = 0

# Creating instances
singleton1 = Singleton()
singleton2 = Singleton()

# Modifying the value of singleton1
singleton1.value = 42

# Accessing the value from singleton2
print(singleton2.value)  # This will also print 42, demonstrating the Singleton pattern


