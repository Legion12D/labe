class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = None
        self.set_password(password)

    def set_password(self, new_password):
        if not isinstance(new_password, str):
            raise TypeError("Пароль должен быть строкой.")
        new_password = new_password.strip()
        if len(new_password) < 6:
            raise ValueError("Пароль должен быть не короче 6 символов.")
        self.__password = new_password

    def check_password(self, password):
        if not isinstance(password, str):
            return False
        return password == self.__password



user = UserAccount("Alex", "Alex@gmail.com", "PAROL1")
print("Проверка верного:", user.check_password("PAROL1"))
print("Проверка неверного:", user.check_password("123"))

user.set_password("novPAROL1")
print("Проверка старого:", user.check_password("PAROL1"))
print("Проверка нового:", user.check_password("novPAROL1"))


print('Задание 2')
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}"

vehicle = Vehicle("ГАЗ", "21Р")
car = Car("hongqi", "h9", "Бензин")

print(vehicle.get_info())
print(car.get_info())