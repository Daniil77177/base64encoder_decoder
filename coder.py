import random, base64
def encode (input1):
    base64variable = base64.b64encode(bytes(input1,'utf-8'))
    print(base64variable)

def decode (input1):
    base64variable = base64.b64decode(bytes(input1,'utf-8'))
    print(str(base64variable))