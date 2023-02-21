#include <iostream>
using namespace std;

//This function will display the main menu
void showMenu(){
    cout << "Welcome to the Classical Ciphers Menu" << endl;
    cout << "1. Caesar Cipher" << endl;
    cout << "2. Vigenere Cipher" << endl;
    cout << "3. Exit" << endl;
}

//This function will handle the caesar cipher operation
void caesarCipher(){
    int shift;
    string plainText;

    cout << "Enter the plain text: ";
    cin >> plainText;
    cout << "Enter the shift: ";
    cin >> shift;

    string encryptedText = "";
    for (int i = 0; i < plainText.length(); i++) {
        char ch = plainText[i];
        if (ch >= 'a' && ch <= 'z') {
            ch = ch + shift;
            if (ch > 'z') {
                ch = ch - 'z' + 'a' - 1;
            }
            encryptedText = encryptedText + ch;
        } else if (ch >= 'A' && ch <= 'Z') {
            ch = ch + shift;
            if (ch > 'Z') {
                ch = ch - 'Z' + 'A' - 1;
            }
            encryptedText = encryptedText + ch;
        } else {
            encryptedText = encryptedText + ch;
        }
    }
    cout << "Encrypted text: " << encryptedText << endl;
}

//This function will handle the decrypt operation
void decrypt(){
    int shift;
    string encryptedText;

    cout << "Enter the encrypted text: ";
    cin >> encryptedText;
    cout << "Enter the shift: ";
    cin >> shift;

    string decryptedText = "";
    for (int i = 0; i < encryptedText.length(); i++) {
        char ch = encryptedText[i];
        if (ch >= 'a' && ch <= 'z') {
            ch = ch - shift;
            if (ch < 'a') {
                ch = ch + 'z' - 'a' + 1;
            }
            decryptedText = decryptedText + ch;
        } else if (ch >= 'A' && ch <= 'Z') {
            ch = ch - shift;
            if (ch < 'A') {
                ch = ch + 'Z' - 'A' + 1;
            }
            decryptedText = decryptedText + ch;
        } else {
            decryptedText = decryptedText + ch;
        }
    }
    cout << "Decrypted text: " << decryptedText << endl;
}

//This function will handle the vigenere cipher operation
void vigenereCipher(){
    string plainText;
    string key;

    cout << "Enter the plain text: ";
    cin >> plainText;
    cout << "Enter the key: ";
    cin >> key;

    string encryptedText = "";
    for (int i = 0, j = 0; i < plainText.length(); i++) {
        char ch = plainText[i];
        if (ch >= 'a' && ch <= 'z') {
            ch = ch + (key[j] - 'a');
            if (ch > 'z') {
                ch = ch - 'z' + 'a' - 1;
            }
            encryptedText = encryptedText + ch;
            j = (j + 1) % key.length();
        } else if (ch >= 'A' && ch <= 'Z') {
            ch = ch + (key[j] - 'A');
            if (ch > 'Z') {
                ch = ch - 'Z' + 'A' - 1;
            }
            encryptedText = encryptedText + ch;
            j = (j + 1) % key.length();
        } else {
            encryptedText = encryptedText + ch;
        }
    }
    cout << "Encrypted text: " << encryptedText << endl;
}

int main()
{
    int choice;
    do {
        showMenu();
        cout << "Enter your choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                caesarCipher();
                break;
            case 2:
                vigenereCipher();
                break;
            case 3:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice!" << endl;
                break;
        }
    } while (choice != 3);
    return 0;
}