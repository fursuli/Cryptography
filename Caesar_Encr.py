import json

alphabet = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_.,’ 0123456789'

text = u"Я, Стрільчук Марія Михайлівна, студентка 342"
key = int(input("Ключ:\n"))

result = ""
decrypt = ""

for el in text.upper():
    num = (alphabet.index(el) + key) % len(alphabet)
    result += alphabet[num]
print(result)

# for el in result:
#     num = (alphabet.index(el) - key) % 48
#     decrypt += alphabet[num]
# print(decrypt)

with open("cypher.txt", "w+") as data:
    cripher_message = data.write(json.dumps(result))
