#Função que criptografa uma string, a partir de uma soma por indução
# com a seguinte fórmula: S(n) = ½n * (n + 1)
def encrypt(decryptedTxt):
    encrypted = ''
    
    #Itera a string criptografando carácter por carácter
    for char in decryptedTxt:
        num = ord(char) # Converte carácter em um código Unicode
        somaIndutiva = int((num / 2) * (num + 1)) # Aplica a fórmula da soma por indução sobre o código unicode
        encrypted += chr(somaIndutiva) # Converte o resultado da soma para carácter
    return encrypted

#Descriptografa uma string revertendo a soma por indução dos números naturais de cada código de carácter
def decrypt(encryptedTxt):
    decrypted = ''

    
    #Itera a string descriptografando carácter por carácter
    for char in encryptedTxt:
        soma = ord(char) # Converte o carácter para seu código unicode
        n = 0

        # Subtrai n progressivamente (1,2,3,4,...) até o valor do carácter chegar a 0.
        # Baseado na soma de indução onde a fórmula é S(n) é a soma de todos os números até chegar a n
        while True:
            soma -= n
            if soma <= 0:
                break
            n += 1
        decrypted += chr(n) #  Converte o valor de n para carácter
    return decrypted

#Função que valida se uma string pode ser descriptografada
def isDecriptable(encryptedTxt):
    # Valida se todos os códigos unicode dos caracteres são resultandos
    # de uma soma progressiva de números naturais onde S(n) = 1 + 2 + 3 + ... + n
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
        
