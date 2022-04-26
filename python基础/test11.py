# coding = utf-8
import json

# 异常
def exc1():
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("You can't divide by zero!")


def exc_file():
    filename = 'alice.txt'
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")


# 数据存储
def sava_data():
    file_name = "number.json"
    num = list(i**2 for i in range(100))
    with open(file_name, "w") as f:
        json.dump(num, f)


def read_data():
    file_name = "number.json"
    with open(file_name, "r") as f:
        number = json.load(f)
    print(type(number))
    str1 = '{"name":"lyl","old":"13"}'
    number1 = json.loads(str1)
    print(type(number1))


if __name__ == '__main__':
    read_data()