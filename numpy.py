import numpy as np
matrix1 = []
matrix2 = []
act = input("Выберите действие: +, -, *, T: ")
if act == 'T':
    n = int(input("Введите кол-во строк: "))
    m = int(input("Введите кол-во столбцов: "))
    for i in range(n):
        vector = []
        for j in range(m):
            k = int(input("Введите элемент: "))
            vector.append(k)
        matrix1.append(vector)
    matrix1 = np.array(matrix1)
    print(matrix1.T)
else:
    n = int(input("Введите кол-во строк: "))
    m = int(input("Введите кол-во столбцов: "))
    for i in range(n):
        vector = []
        for j in range(m):
            k = int(input("Введите элемент: "))
            vector.append(k)
        matrix1.append(vector)
    matrix1 = np.array(matrix1)
    n = int(input("Введите кол-во строк: "))
    m = int(input("Введите кол-во столбцов: "))
    for i in range(n):
        vector = []
        for j in range(m):
            k = int(input("Введите элемент: "))
            vector.append(k)
        matrix2.append(vector)
    matrix2 = np.array(matrix2)
    if act == '+':
        print(matrix1 + matrix2)
    elif act == '-':
        print(matrix1 - matrix2)
    elif act == '*':
        print(matrix1 @ matrix2)
    else:
        print("Выбрано неверное действие")
