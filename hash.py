_xormap = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}
def xor(x, y):
    return ''.join([_xormap[a, b] for a, b in zip(x, y)])

inp = input('input msg \t')
bitsStream = ''.join(format(x, 'b') for x in bytearray(inp,encoding='ascii'))
hashLength = 16
blocks = []
blocks = [bitsStream[i:i+hashLength] for i in range(0, len(bitsStream), hashLength)] 
if len(blocks[-1]) < hashLength:
    blocks[-1] = blocks[-1] + ('0' * (hashLength - len(blocks[-1])))
print(blocks)
result = xor(blocks[0], blocks[1])
if len(blocks) > 2:
    for i in range(len(blocks) - 2):
        result = xor(result, blocks[i + 2])

print(result)
