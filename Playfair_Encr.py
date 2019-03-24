import json
from collections import OrderedDict


alphabet = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ .,'123456789"

message = (input("Введіть повідомлення для шифрування: ")).upper()

""" Перевірка на непарність символів в повідомленні """
if len(message) % 2 != 0:
    message = message + "X"

""" Поділ повідомлення на пари із символів """
wrapped_message = []
k = ""
for symbol in message:
    k += symbol
    if len(k) == 2:
        wrapped_message.append(k)
        k = ""

key = (input("Введіть ключ для створення матриці: ")).upper()
key = "".join(OrderedDict.fromkeys(key))
# print(key)

matrix = "".join(OrderedDict.fromkeys(key + alphabet))

matrix = [ list(matrix[:5]),
           list(matrix[5:10]),
           list(matrix[10:15]),
           list(matrix[15:20]),
           list(matrix[20:25]),
           list(matrix[25:30]),
           list(matrix[30:35]),
           list(matrix[35:40]),
           list(matrix[40:])
           ]

encrypt_message = ""
switch = 0

for i in range(len(wrapped_message)):
    for k in range(2):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == wrapped_message[i][k]:
                    if wrapped_message[i][0] in matrix[x] and wrapped_message[i][1] in matrix[x]:
                        if matrix[x][y] != matrix[x][-1]:
                            encrypt_message +=matrix[x][y+1]
                        else:
                            encrypt_message += matrix[x][y-4]
                    else:
                        for a in range(len(matrix)):
                            for b in range(len(matrix[a])):
                                if matrix[a][b] == wrapped_message[i][0]:
                                    x0 = a
                                if matrix[a][b] == wrapped_message[i][1]:
                                    x1 = a
                        if switch == 0:
                            encrypt_message += matrix[x1][y]
                            switch = 1
                        else:
                            encrypt_message += matrix[x0][y]
                            switch = 0

print("Зашифроване повідомлення: ", encrypt_message)
with open("cypher.txt", "w+") as data:
    cripher_message = data.write(json.dumps(encrypt_message))