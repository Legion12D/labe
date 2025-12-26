print('Задание 1')

def greet(name):
    print("Hello", name)
n=input()
greet(n)


def square(number):
    return number**2
num=int(input())
print(square(num))


def max_of_two(x,y):
    return (max(x,y))
num_x=int(input())
num_y=int(input())
print(max_of_two(num_x,num_y))






print('Задание 2')

def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age}")

print('Введите имя:')
b=input()
print('хотите ли вы написать возраст:  да или нет')
s=input()
if s=='да':
    print('Введите возраст:')
    a = int(input())
    print(describe_person(b, a))
else:
    print(describe_person(b))




print('Задание 3')

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
n=int(input())
print(is_prime(n))





























































