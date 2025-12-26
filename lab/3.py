print('задание 1')
with open ("example.txt", "w", encoding="utf-8") as file:
    file.write(input("Введите первую строку: ") + "\n")
    file.write(input("Введите вторую строку: ") + "\n")
    file.write(input("Введите третью строку: ") + "\n")

def read_file(file_name, type = "all_read"):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            if type == "all_read":
                content = file.read()
                return content
            elif type == "for_read":
                result = ""
                for line in file:
                    result += line
                return result
            else:
                return "Нет такого типа чтения"
    except FileNotFoundError:
        return "Нет такого файла"

print(read_file("example.txt", type = "all_read"))
print(read_file("exaple.txt", type = "for_read"))






print('задание 2')

user_text = input("Введите текст:")
with open('user_input.txt', 'w', encoding='utf-8') as file:
    file.write(user_text)

user_text = input("Введите текст:")
with open('user_input.txt', 'a', encoding='utf-8') as file:
    file.write(user_text)