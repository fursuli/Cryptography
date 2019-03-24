import json
from collections import OrderedDict



with open("cypher.txt", "r") as  data:
    cry_message = json.loads(data.read())

    alphabet = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ .,'123456789"

    print("Повідомлення: ", cry_message)


    key = (input("Введіть ключ для дешифрування повідомлення: ")).upper()
    key = "".join(OrderedDict.fromkeys(key))
    # print(key)

    wrapped_encr_message = []
    k = ""
    for symbol in cry_message:
        k += symbol
        if len(k) == 2:
            wrapped_encr_message.append(k)
            k = ""
    # print(wrapped_encr_message)

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


    decry_message = ""
    switch = 0

    for i in range(len(wrapped_encr_message)):
        for k in range(2):
            for x in range(len(matrix)):
                for y in range(len(matrix[x])):
                    if matrix[x][y] == wrapped_encr_message[i][k]:
                        if wrapped_encr_message[i][0] in matrix[x] and wrapped_encr_message[i][1] in matrix[x]:
                            if matrix[x][y] != matrix[x][0]:
                                decry_message += matrix[x][y - 1]
                            else:
                                decry_message += matrix[x][y + 4]
                        else:
                            for a in range(len(matrix)):
                                for b in range(len(matrix[a])):
                                    if matrix[a][b] == wrapped_encr_message[i][0]:
                                        x0 = a
                                    if matrix[a][b] == wrapped_encr_message[i][1]:
                                        x1 = a
                            if switch == 0:
                                decry_message += matrix[x1][y]
                                switch = 1
                            else:
                                decry_message += matrix[x0][y]
                                switch = 0

    # for i in range(len(decry_message)-1):
    #     if decry_message[i] == "X":
    #         if decry_message[i] != decry_message[-1]:
    #             if decry_message[i-1] == decry_message[i+1]:
    #                 decry_message.remove(decry_message[i])
    #         else:
    #             decry_message.remove(decry_message[i])

    print("Розшифроване повідомлення: ", decry_message)