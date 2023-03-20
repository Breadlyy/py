import math
class Shape:
    def __init__(self, sides):
        self.sides = sides
        
    def resize(self, new_sides):
        self.sides = new_sides
        
    def draw(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(None)
        self.radius = radius
        
    def resize(self, new_radius):
        self.radius*=new_radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def draw(self):
        for i in range(2 * int(self.radius)):
            for j in range(2 *  int(self.radius)):
                if (i - self.radius) ** 2 + (j - self.radius) ** 2 <= self.radius ** 2:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

class Square(Shape):
    def __init__(self, length):
        super().__init__([length] * 4)
        self.length = length
        
    def resize(self, new_length):
        self.length*=new_length
        for i in range(len(self.sides)):
            self.sides[i]*=new_length
        
    def area(self):
        return self.length ** 2
    
    def perimeter(self):
        return 4 * self.length
    
    def draw(self):
        for i in range(int(self.length)):
            for j in range(int(self.length)):
                print("*", end="")
            print()
        print()

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height
        
    def resize(self, new_size):
        self.width*= new_size
        self.height*= new_size
        self.sides = [self.width, self.height, self.width, self.height]
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def draw(self):
        for i in range(int(self.height)):
            for j in range(int(self.width)):
                print("*", end="")
            print()
        print()


# Create some shapes
circle = Circle(5)
square = Square(10)
rectangle = Rectangle(10, 5)

# Get the area and perimeter of each shape
print("Circle area:", circle.area()) # Output: Circle area: 78.53981633974483
print("Circle perimeter:", circle.perimeter()) # Output: Circle perimeter: 31.41592653589793
print("Square area:", square.area()) # Output: Square area: 100
print("Square perimeter:", square.perimeter()) # Output: Square perimeter: 40
print("Rectangle area:", rectangle.area()) # Output: Rectangle area: 50
print("Rectangle perimeter:", rectangle.perimeter()) # Output: Rectangle perimeter: 30

# Resize the shapes
circle.resize(2)
square.resize(0.5)
rectangle.resize(1.5)

# Draw the shapes (not really plots... yet!)
circle.draw() # Output: Drawing shape
square.draw() # Output: Drawing shape
rectangle.draw() # Output: Drawing shape