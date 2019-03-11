import json

alphabet = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_.,’ 0123456789'

with open("cypher.txt", "r") as data:
    cry_message = json.loads(data.read())

    for key in range(len(alphabet)):
        decrypt = ""
        for el in cry_message:
            num = (alphabet.index(el) - key) % len(alphabet)
            decrypt += alphabet[num]
        print("Ключ: {}\nОтримане повідомлення: {}".format(key, decrypt))

    key = int(input("\nВведіть ключ для збереження результату:\t"))
    decrypt = ""
    for el in cry_message:
        num = (alphabet.index(el) - key) % len(alphabet)
        decrypt += alphabet[num]
    print(decrypt)
    with open("open1.txt", "w+") as decrypt_data:
        save_process = decrypt_data.write(json.dumps(decrypt))