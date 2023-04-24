ascii = ["NUL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "TAB"]
message = input("enter a string to encrypt ")
def encript(string): 
    cipherText = ""
    shift = 0
    for char in string: 
        if char.isalpha():
            print(char)
            charNum = ord(char)
            charNum += shift
            cipherText += chr(charNum)
        else:
            cipherText += char
        shift += 1
    return(cipherText)
print(encript(message))
def encode(message):
    asciiText = ""
    for char in message:
        if char.isalpha():
            asciiVal = str(ord(char))
        asciiText += "("
        
        for num in asciiVal:
            print(asciiVal, num)
            asciiText += ascii[int(num)]

            asciiText += ", "
        asciiText += ")"
                     
        asciiText += " "
    return(asciiText)
print(encode(encript(message)))