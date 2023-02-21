def menu():
    print("1. Caesar Cipher")
    print("2. Playfair Cipher")
    print("3. Hill Cipher")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def caesar_cipher_encryption():
    ptext = input("Enter the plain text : ")
    key = int(input("Enter the key : "))
    ctext = ""
    for i in ptext:
        if ord(i) >= 65 and ord(i) <= 90:
            ctext += chr((ord(i) + key - 65) % 26 + 65)
        elif ord(i) >= 97 and ord(i) <= 122:
            ctext += chr((ord(i) + key - 97) % 26 + 97)
        else:
            ctext += i
    print("The cipher text is : ", ctext)

def caesar_cipher_decryption():
    ctext = input("Enter the cipher text : ")
    key = int(input("Enter the key : "))
    ptext = ""
    for i in ctext:
        if ord(i) >= 65 and ord(i) <= 90:
            ptext += chr((ord(i) - key - 65) % 26 + 65)
        elif ord(i) >= 97 and ord(i) <= 122:
            ptext += chr((ord(i) - key - 97) % 26 + 97)
        else:
            ptext += i
    print("The plain text is : ", ptext)

def playfair_cipher_encryption():
    ptext = input("Enter the plain text : ")
    key = input("Enter the keyword : ")
    k = 0
    matrix = [[' ' for i in range(5)] for j in range(5)]

    for i in range(5):
        for j in range(5):
            if k < len(key):
                matrix[i][j] = key[k]
                k += 1
            else:
                break
    for i in range(26):
        if chr(65 + i) not in key and chr(65 + i) != 'J':
            matrix[i//5][i%5] = chr(65 + i)

    ptext = ptext.replace('J', 'I')
    ptext = ptext.replace(' ', '')
    if len(ptext) % 2 != 0:
        ptext += 'X'

    ctext = ""
    for i in range(0, len(ptext), 2):
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        for j in range(5):
            for k in range(5):
                if matrix[j][k] == ptext[i]:
                    x1, y1 = j, k
                if matrix[j][k] == ptext[i+1]:
                    x2, y2 = j, k

        if x1 == x2:
            ctext += matrix[x1][(y1+1)%5] + matrix[x2][(y2+1)%5]
        elif y1 == y2:
            ctext += matrix[(x1+1)%5][y1] + matrix[(x2+1)%5][y2]
        else:
            ctext += matrix[x1][y2] + matrix[x2][y1]
    print("The cipher text is : ", ctext)

def playfair_cipher_decryption():
    ctext = input("Enter the cipher text : ")
    key = input("Enter the keyword : ")
    k = 0
    matrix = [[' ' for i in range(5)] for j in range(5)]

    for i in range(5):
        for j in range(5):
            if k < len(key):
                matrix[i][j] = key[k]
                k += 1
            else:
                break
    for i in range(26):
        if chr(65 + i) not in key and chr(65 + i) != 'J':
            matrix[i//5][i%5] = chr(65 + i)

    ptext = ""
    for i in range(0, len(ctext), 2):
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        for j in range(5):
            for k in range(5):
                if matrix[j][k] == ctext[i]:
                    x1, y1 = j, k
                if matrix[j][k] == ctext[i+1]:
                    x2, y2 = j, k

        if x1 == x2:
            ptext += matrix[x1][(y1-1)%5] + matrix[x2][(y2-1)%5]
        elif y1 == y2:
            ptext += matrix[(x1-1)%5][y1] + matrix[(x2-1)%5][y2]
        else:
            ptext += matrix[x1][y2] + matrix[x2][y1]
    ptext = ptext.replace('J', 'I')
    print("The plain text is : ", ptext)

def hill_cipher_encryption():
    ptext = input("Enter the plain text : ")
    ptext.upper()
    key = input("Enter the 3x3 matrix key : ")
    key_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    k = 0
    for i in range(3):
        for j in range(3):
            key_matrix[i][j] = ord(key[k])-65
            k += 1

    ptext = ptext.replace(' ', '')
    if len(ptext) % 3 != 0:
        for i in range(3-(len(ptext) % 3)):
            ptext += 'X'

    ctext = ""
    for i in range(0, len(ptext), 3):
        x = [0, 0, 0]
        for j in range(3):
            x[j] = ord(ptext[i+j]) - 65

        result = [0, 0, 0]
        for j in range(0,3):
            for k in range(0,3):
                result[j] += key_matrix[j][k] * x[k]
        print(result)
        for j in range(3):
            ctext += chr((result[j] % 26) + 65)
    print("The cipher text is : ", ctext)
    print('')

def hill_cipher_decryption():
    ctext = input("Enter the cipher text : ")
    ctext.upper()
    key = input("Enter the 3x3 matrix key : ")
    key_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    k = 0
    for i in range(3):
        for j in range(3):
            key_matrix[i][j] = ord(key[k])-65
            k += 1

    inverse_key = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    determinant = 0
    for i in range(3):
        determinant += (key_matrix[0][i] * (key_matrix[1][(i + 1) % 3] * key_matrix[2][(i + 2) % 3] - key_matrix[1][(i + 2) % 3] * key_matrix[2][(i + 1) % 3]))
    if(determinant==0):
        print('Inverse does not exist for the matrix')
        return 0
    determinant = pow(determinant,11) % 26
    inverse_key[0][0] = (((key_matrix[1][1] * key_matrix[2][2] - key_matrix[2][1] * key_matrix[1][2]))*25)%26
    inverse_key[1][0] = ((-(key_matrix[1][0] * key_matrix[2][2] - key_matrix[2][0] * key_matrix[1][2]))*25)%26
    inverse_key[2][0] = (((key_matrix[1][0] * key_matrix[2][1] - key_matrix[2][0] * key_matrix[1][1]))*25)%26
    inverse_key[0][1] = ((-(key_matrix[0][1] * key_matrix[2][2] - key_matrix[2][1] * key_matrix[0][2]))*25)%26
    inverse_key[1][1] = (((key_matrix[0][0] * key_matrix[2][2] - key_matrix[2][0] * key_matrix[0][2]))*25)%26
    inverse_key[2][1] = ((-(key_matrix[0][0] * key_matrix[2][1] - key_matrix[2][0] * key_matrix[0][1]))*25)%26
    inverse_key[0][2] = (((key_matrix[0][1] * key_matrix[1][2] - key_matrix[1][1] * key_matrix[0][2]))*25)%26
    inverse_key[1][2] = ((-(key_matrix[0][0] * key_matrix[1][2] - key_matrix[1][0] * key_matrix[0][2]))*25)%26
    inverse_key[2][2] = (((key_matrix[0][0] * key_matrix[1][1] - key_matrix[1][0] * key_matrix[0][1]))*25)%26
    ptext = ""
    for i in range(0, len(ctext), 3):
        x = [0, 0, 0]
        for j in range(3):
            x[j] = ord(ctext[i+j]) - 65

        result = [0, 0, 0]
        for j in range(3):
            for k in range(3):
                result[j] += inverse_key[j][k] * x[k]
        for j in range(3):
            ptext += chr((result[j] % 26) + 65)
    print("The plain text is : ", ptext)

while True:
    choice = menu()
    if choice == 1:
        print("CAESAR CIPHER")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            caesar_cipher_encryption()
        elif choice == 2:
            caesar_cipher_decryption()
    elif choice == 2:
        print("PLAYFAIR CIPHER")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            playfair_cipher_encryption()
        elif choice == 2:
            playfair_cipher_decryption()
    elif choice == 3:
        print("HILL CIPHER")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            hill_cipher_encryption()
        elif choice == 2:
            a=hill_cipher_decryption()
    elif choice == 4:
        break