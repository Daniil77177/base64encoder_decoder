import random, base64
def encode (input):
    base64variable = base64.b64encode(input)
    print(base64variable)

def decode (input):
    base64variable = base64.b64decode(input)
    print(str(base64variable))
