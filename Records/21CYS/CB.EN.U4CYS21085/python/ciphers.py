

class caesar:
    def caesar_cipher_encryption(self):
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


    def caesar_cipher_decryption(self):
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

class vigenere:
    def vigenere_encrypt(self):
        key = input("Enter the key: ")
        if(key.isdigit()==True):
            return 0;
        plaintext = input("Enter the plain text: ")
        ciphertext = ""
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext]
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext

    def vigenere_decrypt(self):
        ciphertext = input("Enter the cipher text: ")
        key = input("Enter the key: ")
        if(key.isdigit()==True):
            return 0;
        plaintext = ""
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        ciphertext_int = [ord(i) for i in ciphertext]
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext

class hill:
    def hill_cipher_encryption(self):
        ptext = input("Enter the plain text : ")
        ptext = ptext.upper()
        key = input("Enter the 3x3 matrix key : ")
        key = key.upper()
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
            for j in range(3):
                ctext += chr((result[j] % 26) + 65)
        print("The cipher text is : ", ctext)

    def hill_cipher_decryption(self):
        ctext = input("Enter the cipher text : ")
        ctext = ctext.upper()
        key = input("Enter the 3x3 matrix key : ")
        key = key.upper()
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
            print('Given matrix does not have inverse')
            return 0
        determinant = pow(determinant,11) % 26
        inverse_key[0][0] = (((key_matrix[1][1] * key_matrix[2][2] - key_matrix[2][1] * key_matrix[1][2]))*determinant)%26
        inverse_key[1][0] = ((-(key_matrix[1][0] * key_matrix[2][2] - key_matrix[2][0] * key_matrix[1][2]))*determinant)%26
        inverse_key[2][0] = (((key_matrix[1][0] * key_matrix[2][1] - key_matrix[2][0] * key_matrix[1][1]))*determinant)%26
        inverse_key[0][1] = ((-(key_matrix[0][1] * key_matrix[2][2] - key_matrix[2][1] * key_matrix[0][2]))*determinant)%26
        inverse_key[1][1] = (((key_matrix[0][0] * key_matrix[2][2] - key_matrix[2][0] * key_matrix[0][2]))*determinant)%26
        inverse_key[2][1] = ((-(key_matrix[0][0] * key_matrix[2][1] - key_matrix[2][0] * key_matrix[0][1]))*determinant)%26
        inverse_key[0][2] = (((key_matrix[0][1] * key_matrix[1][2] - key_matrix[1][1] * key_matrix[0][2]))*determinant)%26
        inverse_key[1][2] = ((-(key_matrix[0][0] * key_matrix[1][2] - key_matrix[1][0] * key_matrix[0][2]))*determinant)%26
        inverse_key[2][2] = (((key_matrix[0][0] * key_matrix[1][1] - key_matrix[1][0] * key_matrix[0][1]))*determinant)%26
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

class affine:
    def encryptAffine(self):
        print('Enter the plaintext : ')
        plainText = input()
        print('Enter key a : ')
        a = int(input())
        print('Enter key b : ')
        b = int(input())
        cipherText = ""
        for i in range(len(plainText)):
            # convert to uppercase
            if 'a' <= plainText[i] <= 'z':
                plainText = plainText.upper()
            # Encryption formula
            x = (a * (ord(plainText[i]) - 65) + b) % 26
            # convert to lowercase
            cipherText += chr(x + 65)
        return cipherText

    def decryptAffine(self):
        print('Enter the ciphertext : ')
        cipherText = input()
        print('Enter key a : ')
        a = int(input())
        print('Enter key b : ')
        b = int(input())
    
        plainText = ""
        # Calculating the modular inverse of a
        a_inv = 0
        flag = 0
        for i in range(26):
            flag = (a * i) % 26
            # Check if (a*i)%26 == 1, then i will be the modular inverse of a
            if flag == 1:
                a_inv = i
        # Decryption formula
        for i in range(len(cipherText)):
            # convert to uppercase
            if 'a' <= cipherText[i] <= 'z':
                cipherText = cipherText.upper()
            x = (a_inv * (ord(cipherText[i]) + 65 - b)) % 26
            # convert to lowercase
            plainText += chr(x + 65)
        return plainText

class form(caesar, vigenere, hill, affine):
    def inp(self):
        temp = 1
        while temp:
            print("Choose the cipher scheme you want:")
            print("1. Caesar Cipher")
            print("2. Vigenere Cipher")
            print("3. Affine Cipher")
            print("4. Hill Cipher")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("CAESAR CIPHER")
                print("1. Encrypt")
                print("2. Decrypt")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print('')
                    caesar.caesar_cipher_encryption(self)
                    print('')
                elif choice == 2:
                    print('')
                    caesar.caesar_cipher_decryption(self)
                    print('')

            elif choice == 2:
                print("VIGENERE CIPHER")
                print("1. Encrypt")
                print("2. Decrypt")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print('')
                    ciphertext = vigenere.vigenere_encrypt(self)
                    print("The cipher text is: ",ciphertext)
                    print('')
            
                elif choice == 2:
                    print('')
                    decrypted = vigenere.vigenere_decrypt(self)
                    print("The plain text is: ",decrypted)
                    print('')

            elif choice == 3:
                print("AFFINE CIPHER")
                print("1. Encrypt")
                print("2. Decrypt")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print('')
                    ciphertext = affine.encryptAffine(self)
                    print("The cipher text is: ",ciphertext)
                    print('')

                elif choice == 2:
                    print('')
                    decrypted = affine.decryptAffine(self)
                    print('The plain text is : ',decrypted)
                    print('')
            
            elif choice == 4:
                print("HILL CIPHER")
                print("1. Encrypt")
                print("2. Decrypt")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print('')
                    hill.hill_cipher_encryption(self)
                    print('')
            
                elif choice == 2:
                    print('')
                    hill.hill_cipher_decryption(self)
                    print('')
            else:
                print('')
                print('Exiting...')
                temp = 0
            
A = form()
A.inp()
