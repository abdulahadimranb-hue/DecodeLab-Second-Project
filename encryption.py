import string
text = input("Enter text :")
shift = int(input("Enter shift value :"))
# To shift the letters by a certain number of positions in the alphabet by ASCII values.

def Encryption():
    ciphertext = ""
    for char in text:
        if char.isupper():
            shifted = ord(char) + shift
            if shifted > ord("Z"):
                shifted -= 26
            ciphertext += chr(shifted)

        elif char.islower():
            shifted = ord(char) + shift
            if shifted > ord("z"):
                shifted -= 26
            ciphertext += chr(shifted)

        elif char.isdigit():
            shifted = int(char) + shift
            if shifted > 9:
                shifted -= 10
            ciphertext += str(shifted)
            
        elif char in string.punctuation:
            ciphertext += chr(ord(char) + shift)
        else:
            ciphertext += char
    return ciphertext

print("Encrypted Text :  " + Encryption())

def Decryption(ciphertext):
    decrypttext = ""
    for char in ciphertext:
        if char.isupper():
            shifted = ord(char) - shift
            if shifted < ord("A"):
                shifted += 26
            decrypttext += chr(shifted)

        elif char.islower():
            shifted = ord(char) - shift
            if shifted < ord("a"):
                shifted += 26
            decrypttext += chr(shifted)

        elif char.isdigit():
            shifted = int(char) - shift
            if shifted < 0:
                shifted += 10
            decrypttext += str(shifted)

        elif char in string.punctuation:
            decrypttext += chr(ord(char) - shift)
        else:
            decrypttext += char
    return decrypttext

print("Decrypted Text :  " + Decryption(Encryption()))