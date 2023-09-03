string = input("Digite uma mensagem a ser criptografada: ")
ct = 1
preString = ""
print(f"Mensagem original: {string}")
for j in range(len(string)):
    asciiString = ord(string[j])
    asciiString += 1
    asciiString = chr(asciiString)
    preString += asciiString

print(f"Intermediário: {preString}\nMensagem criptografada: ", end="")
for i in range(len(string)):
    if i < (len(string) / 2):
        print(f"{preString[i]}", end="")
    if len(string) % 2 != 0:
        if i < (len(preString) / 2) - 1:
            print(f"{preString[i - ct]}", end="")
    else:
        if i < (len(string) / 2):
            print(f"{preString[i - ct]}", end="")
    ct += 2

print("\n")

string = input("Digite uma mensagem a ser descriptografada: ")
ct = 0
preString = ""
for l in range(len(string)):
    asciiString = ord(string[l])
    asciiString -= 1
    asciiString = chr(asciiString)
    preString += asciiString

print(f"Mensagem criptografada: {string}")
print(f"Intermediário: {preString}")
print("Mensagem descriptografada: ", end="")
for i in range(len(string)):
    if i < (len(string) / 2):
        print(f"{preString[i + ct]}", end="")
    ct += 1
ct = 2
for j in range(len(string)):
    if len(string) % 2 != 0:
        if j < (len(string) / 2) - 1:
            print(f"{preString[len(string) - ct]}", end="")
    else:
        if j < (len(string) / 2):
            print(f"{preString[len(string) - (ct - 1)]}", end="")
    ct += 2
