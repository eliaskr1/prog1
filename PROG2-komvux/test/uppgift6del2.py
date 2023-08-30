class Book:
    def __init__(self, title, auth, pgs, price):
        self._title = title
        self._auth = auth
        self._pgs = pgs
        self._price = price
    
    def set_title(self, title): # Metoder för att ange värden till böcker
        self._title = title
    def set_auth(self, auth):
        self._auth = auth
    def set_pgs(self, pgs):
        self._pgs = pgs
    def set_price(self, price):
        self._price = price
        
    def get_title(self, title): # Metoder för att hämta värden ur böcker
        return self._title
    def get_auth(self, auth):
        return self._auth
    def get_pgs(self, pgs):
        return self._pgs
    def get_price(self, price):
        return self._price
    
    def __str__(self): # Definierar hur "Book" objekten skrivs ut
        return "Titel: "+self._title+"\n"+"Författare: "+self._auth+"\n"+"Sidantal: "+self._pgs+"\n"+"Pris: "+self._price+"\n"
    
    title = property(get_title, set_title) # Definierar mina fget och fset metoder för mina attributer
    auth = property(get_auth, set_auth)
    pgs = property(get_pgs, set_pgs)
    price = property(get_price, set_price)
   
b0 = Book("The Hunger Games", "Suzanne Collins", "400", "199kr") # Skapar objekt
b1 = Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", "450", "149kr")

print(b0)
print(b1)

b0.title = "Lord of the flies" # Använder mina inkapslade metoder för att ändra attributer till objekten
b0.auth = "William Golding"
b0.pgs = "350"
b0.price = "89kr"

b1.title = "Häxan"
b1.auth = "Camilla Läckberg"
b1.pgs = "400"
b1.price = "249kr"

print(b0)
print(b1)