import coder
print("Hello, I'm Coder, and I'll help you with your base64 code")
print("Write a name of file")
path1 = input()

print("Your file is txt or binary? (txt or b)")
txtorB = str(input()).lower()

while not (txtorB == "b" or txtorB == "txt"):
    print("Your input is not correct. Try again")
    txtorB = input().lower()


if txtorB == "b":   #Binary
    f = open(path1, "rb")
    ftext = f.read()
    print(ftext)
    print("Encode or decode? (e or dec)")
    codervariable = input()
    if codervariable == "e":
        coder.encode(ftext)
    else:
        coder.decode(ftext)

elif txtorB == "txt":   #txt or html
    f = open("./"+path1, "r")
    ftext = f.read()
    print(ftext)
    print("Encode or decode? (e or dec)")
    codervariable = input()
    if codervariable == "e":
        coder.encode(ftext)
    else:
        coder.decode(ftext)
