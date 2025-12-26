print('Задание 1')
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}.\nАвтор: {self.author}.\nГод издания: {self.year}"



book1 = Book("Мастер и Маргарита", "Михаил Афанасьевич Булгаков",  1967)
print(book1.get_info())



print('Задание 2')
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        if new_radius > 0:
            self.radius = new_radius
        else:
            print("Ошибка: радиус должен быть положительным")
start_radius = float(input("Введите начальный радиус круга: "))
circle = Circle(start_radius)
print("Начальный радиус круга:", circle.get_radius())
new_radius = float(input("Введите новый радиус круга: "))
circle.set_radius(new_radius)
print("Новый радиус круга:", circle.get_radius())