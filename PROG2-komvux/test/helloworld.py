class Base:
    def __init__(self, name="noname"):
        self.__name = name
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def copy_from(self, o):
        self.__name = o.name
    
    def __str__(self):
        return self.__name+" - Base() "
    
    name = property(get_name, set_name)

class Point(Base): # Skapar klassen
    def __init__(self, x = 0.0, y = 0.0, name="Point ("): # Definierar attribut till klassen (namn, koordinater)
        super().__init__(name) 
        self.__x = x
        self.__y = y
        # Nedan följer olika metoder som klassen använder för att definiera olika objekt (Point)
    def set_x(self, x): # Till exempel "set" metoderna anger koordinater för "point" objekt
        self.__x = x
        
    def set_y(self, y):
        self.__y = y
        
    def set(self, x, y):
        self.__x = x
        self.__y = y
	
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
        
    def copy_from(self, p):
        super().copy_from(p)
        self.__x = p.x
        self.__y = p.y
    
    def __str__(self):
        return self.name+str(self.__x)+", "+str(self.__y)+")"
    
    x = property(get_x, set_x)
    y = property(get_y, set_y)

class Circle(Point):
    def __init__(self, x=0.0, y=0.0, r=1.0, name="Circle ("):
        super().__init__(x, y, name)
        self.__r = r
    
    def set_r(self, r):
        self.__r = r
    
    def get_r(self):
        return self.__r
    
    def copy_from(self, c):
        super().copy_from(c)
        self.r = c.r
    
    def __str__(self):
        return self.name+str(self.x) + ", "+str(self.y)+", "+str(self.r)+")"
    
    r = property(get_r, set_r)
    
import math    
class Line(Base):
    def __init__(self, name = "Line "):
        super().__init__(name)
        self.__p0 = Point()
        self.__p1 = Point()
    
    def get_p0(self):
        return self.__p0
    
    def get_p1(self):
        return self.__p1
    
    def set_p0(self, p0):
        self.__p0 = p0
    
    def set_p1(self, p1):
        self.__p1 = p1
    
    def length(self):
        return math.sqrt(
            math.pow(self.__p1.x - self.__p0.x, 2) + 
            math.pow(self.__p1.y - self.__p0.y, 2))
    
    def __str__(self):
        return_string = self.name+"from: \n\t"
        return_string += str(self.__p0) + "\n"
        return_string += "To: \n\t"
        return_string += str(self.__p1) + "\n"
        return_string += "Length : \n\t"
        return_string += str(self.length()) + "\n"
        return return_string
    p0 = property(get_p0, set_p0)
    p1 = property(get_p1, set_p1)
    

    
shapes = []

shapes.append(Point(1.0, 2.0))
shapes.append(Circle(3.0, 2.0, 2.0))
shapes.append(Line())

for shape in shapes:
    print(shape)