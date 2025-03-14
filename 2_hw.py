#__________________________________

#Лекция 2, задание 1


def task_1() -> None:
    num = 10001
    decimal = 9.1
    text = "All your base are belong to us"
    items = [10, 1000, 10000]
    is_valid = True

    print(num)
    print(decimal)
    print(text)
    print(items)
    print(is_valid)

task_1()

#__________________________________

#Лекция 2, задание 2


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[:3]

r = task_2()
print(r)

#__________________________________

#Лекция 2, задание 3

def task_3(num: int) -> int:
    return num * num

print(task_3(4))
