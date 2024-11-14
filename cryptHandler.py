def encrypt(decryptedTxt):
    encrypted = ''
    for char in decryptedTxt:
        num = ord(char)
        somaIndutiva = int((num / 2) * (num + 1))
        encrypted += chr(somaIndutiva)
    return encrypted

def decrypt(encryptedTxt):
    decrypted = ''
    for char in encryptedTxt:
        soma = ord(char)
        n = 0
        while True:
            soma -= n
            if soma <= 0:
                break
            n += 1
        decrypted += chr(n)
    return decrypted

def isDecriptable(encryptedTxt):
    for char in encryptedTxt:
        soma = ord(char)
        n = 0
        while True:
            soma -= n
            if soma < 0:
                return False
            elif soma == 0:
                break
            n += 1
    return True
        