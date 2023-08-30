class Book:
    def __init__(self, title, auth):
        self._title = title
        self._auth = auth
        
    
    def set_title(self, title): # Metoder för att ange värden till böcker
        self._title = title
    def set_auth(self, auth):
        self._auth = auth
    
    def get_title(self, title): # Metoder för att hämta värden ur böcker
        return self._title
    def get_auth(self, auth):
        return self._auth
    
    
    def __str__(self): # Definierar hur "Book" objekten skrivs ut
        return "\nTitel: "+self._title+"\n"+"Författare: "+self._auth+"\n"
    
    title = property(get_title, set_title) # Definierar mina fget och fset metoder för mina attributer
    auth = property(get_auth, set_auth)
    

b0 = Book("Harry Potter", "J.K Rowling") # Skapar mina objekt
b1 = Book("Lord of the Rings", "J.R Tolkien")
b2 = Book("Aldrig fucka upp", "Jens Lapidus")

a = [b0, b1, b2] # Lägger in objekt i en lista

print(a[0]) # Skriver ut första objektet i listan
print(a[-1]) # Och sista

a.sort(key=lambda x: x._title) # Sorterar efter titel

for book in a: # Skriver ut alla böcker
    print(book)
    
print(len(a)) # Skriver ut hur många böcker som finns i min lista

b3 = Book("The Hunger Games", "Suzanne Collins") # Skapar en till bok

a.append(b3) # Lägger till nya boken i listan

for book in a: # Printar ut alla böcker igen
    print(book)