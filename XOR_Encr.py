import json


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

# def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
#     n = int(bits, 2)
#     return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

with open("open1.txt", "r") as data:
    message = json.loads(data.read())
    binary_message = text_to_bits(message)

    key = input("Ваш ключ:\t")
    encr_key = text_to_bits(key)
     # бмвстралгукпрвогімдалшзушчндтьвілдхцнквьюді

    encr_message = ""
    for (c1, c2) in zip(binary_message, encr_key):
        num = (ord(c1) ^ ord(c2)) % len(encr_key)
        encr_message += str(num)
    print(encr_message)

    with open("cypher2.txt", "w+") as data:
        cypher_text = data.write(json.dumps(encr_message))

    # decr_message = ""
    # for (c1, c2) in zip(encr_message, encr_key):
    #     num = (ord(c1) ^ ord(c2)) % len(binary_message)
    #     decr_message += str(num)
    # print(decr_message)
    #
    # returned_message = text_from_bits(decr_message)
    # print(returned_message)
