#Magic/Dunder Methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):              #print(obj)
        return f"Book: '{self.title}' ({self.pages} pages)"

    def __len__(self):              #len(obj)
        return self.pages

    def __add__(self, other):       #obj1 + obj2
        combined = self.pages + other.pages
        return Book(f"{self.title} + {other.title}", combined)

    def __gt__(self, other):        #obj1 > obj2
        return self.pages > other.pages

b1 = Book("Python Basics", 300)
b2 = Book("ML Crash Course", 450)

print(b1)
print(len(b2))
combined = b1 + b2
print(combined)
print(b1 > b2)
print(b2 > b1)
