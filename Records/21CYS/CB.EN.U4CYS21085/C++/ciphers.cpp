#include <iostream>
#include <string>
#include <math.h>
using namespace std;

class caesar
{
    protected:
    void caesar_cipher_encryption()
    {
        string ptext;
        cout << "Enter the plain text: ";
        cin >> ptext;

        int key;
        cout << "Enter the shift key: ";
        cin >> key;

        string ctext = "";
        for (char c : ptext)
        {
            if (c >= 'A' && c <= 'Z')
            {
                ctext += char((c + key - 'A') % 26 + 'A');
            }
            else if (c >= 'a' && c <= 'z')
            {
                ctext += char((c + key - 'a') % 26 + 'a');
            }
            else
            {
                ctext += c;
            }
        }
        cout << endl;
        cout << "The cipher text is: " << ctext << endl
             << endl;
    }

    void caesar_cipher_decryption()
    {
        string ctext;
        cout << "Enter the cipher text: ";
        cin >> ctext;

        int key;
        cout << "Enter the key: ";
        cin >> key;

        string ptext = "";
        for (char c : ctext)
        {
            if (c >= 'A' && c <= 'Z')
            {
                int pt = (c - key - 'A');
                if (pt < 0)
                {
                    ptext += char(((pt + 26)) + 'A');
                }
                else
                {
                    ptext += char((pt % 26) + 'A');
                }
            }
            else if (c >= 'a' && c <= 'z')
            {
                int pt = (c - key - 'a');
                if (pt < 0)
                {
                    ptext += char(((pt + 26)) + 'a');
                }
                else
                {
                    ptext += char((pt % 26) + 'a');
                }
            }
            else
            {
                ptext += c;
            }
        }
        cout << endl;
        cout << "The plain text is: " << ptext << endl
             << endl;
    }
};

class vigenere
{
    protected:
    void vigenere_encryption()
    {
        string key, t;
        cout << "Enter pt : ";
        cin >> t;
        cout << "Enter key : ";
        cin >> key;
        string output, k;
        for (int i = 0; i < key.length(); ++i)
        {
            if (key[i] >= 'A' && key[i] <= 'Z')
            {
                k += key[i];
            }
            else if (key[i] >= 'a' && key[i] <= 'z')
            {
                k += key[i] + 'A' - 'a';
            }
        }
        for (int i = 0, j = 0; i < t.length(); ++i)
        {
            char c = t[i];
            if (c >= 'a' && c <= 'z')
                c += 'A' - 'a';
            else if (c < 'A' || c > 'Z')
                continue;
            output += char(((c + k[j] - 130) % 26) + 'A'); // added 'A' to bring it in range of ASCII alphabet [ 65-90 | A-Z ]
            j = (j + 1) % k.length();
        }
        cout << endl;
        cout << "Cipher text : " << output << endl
             << endl;
    }
    void vigenere_decryption()
    {
        string key, t;
        cout << "Enter ct : ";
        cin >> t;
        cout << "Enter key : ";
        cin >> key;
        string output, k;
        for (int i = 0; i < key.length(); ++i)
        {
            if (key[i] >= 'A' && key[i] <= 'Z')
                k += key[i];
            else if (key[i] >= 'a' && key[i] <= 'z')
                k += key[i] + 'A' - 'a';
        }
        for (int i = 0, j = 0; i < t.length(); ++i)
        {
            char c = t[i];
            if (c >= 'a' && c <= 'z')
                c += 'A' - 'a';
            else if (c < 'A' || c > 'Z')
                continue;
            output += (c - k[j] + 26) % 26 + 'A'; // added 'A' to bring it in range of ASCII alphabet [ 65-90 | A-Z ]
            j = (j + 1) % k.length();
        }
        cout << endl;
        cout << "Plain text : " << output << endl
             << endl;
    }
};

class hill
{
    protected:
    void hill_cipher_encryption()
    {
        string ptext;
        cout << "Enter the plain text: ";
        cin >> ptext;

        for (int i = 0; i < ptext.length(); i++)
            ptext[i] = toupper(ptext[i]);

        string key;
        cout << "Enter the 3x3 matrix key: ";
        cin >> key;
        for (int i = 0; i < key.length(); i++)
            key[i] = toupper(key[i]);

        int key_matrix[3][3];
        int k = 0;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
            {
                key_matrix[i][j] = key[k] - 'A';
                k++;
            }

        ptext.erase(remove(ptext.begin(), ptext.end(), ' '), ptext.end());
        if (ptext.length() % 3 != 0)
        {
            int num = 3 - (ptext.length() % 3);
            for (int i = 0; i < num; i++)
                ptext += 'X';
        }

        string ctext = "";
        for (int i = 0; i < ptext.length(); i += 3)
        {
            int x[3] = {0, 0, 0};
            for (int j = 0; j < 3; j++)
                x[j] = ptext[i + j] - 'A';

            int result[3] = {0, 0, 0};
            for (int j = 0; j < 3; j++)
                for (int k = 0; k < 3; k++)
                    result[j] += key_matrix[j][k] * x[k];

            for (int j = 0; j < 3; j++)
                ctext += (char)((result[j] % 26) + 'A');
        }
        cout << endl;
        cout << "The cipher text is: " << ctext << endl
             << endl;
    }

    int mod(int n)
    {
        if (n < 0)
        {
            return 26 + ((n) % 26);
        }
        else
        {
            return n % 26;
        }
    }

    void hill_cipher_decryption()
    {
        int i, j;
        string ctext;
        string ptext = "";
        cout << "Enter the cipher text: ";
        cin >> ctext;
        for (char &c : ctext)
            c = toupper(c); // convert to uppercase

        string key;
        cout << "Enter the 3x3 matrix key: ";
        cin >> key;
        for (int i = 0; i < key.length(); i++)
            key[i] = toupper(key[i]);

        int key_matrix[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        int k = 0;
        for (i = 0; i < 3; i++)
        {
            for (j = 0; j < 3; j++)
            {
                key_matrix[i][j] = key[k] - 'A';
                k++;
            }
        }

        cout << endl;

        int inverse_key[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        int determinant = 0;
        for (int i = 0; i < 3; i++)
        {
            if (i == 1)
            {
                int temp = (key_matrix[0][i] * (key_matrix[1][(i + 2) % 3] * key_matrix[2][(i + 1) % 3] - key_matrix[1][(i + 1) % 3] * key_matrix[2][(i + 2) % 3]));
                determinant += mod(temp * (-1));
            }
            else
            {
                determinant += mod(key_matrix[0][i] * (key_matrix[1][(i + 1) % 3] * key_matrix[2][(i + 2) % 3] - key_matrix[1][(i + 2) % 3] * key_matrix[2][(i + 1) % 3]));
            }
        }
        cout << endl;

        if (determinant == 0)
        {
            cout << "Given matrix does not have inverse" << endl;
            return;
        }
        int n = determinant;
        int determinat = (int(pow(n, 4)) % 26) * (int(pow(n, 4)) % 26) * (int(pow(n, 3)) % 26);

        inverse_key[0][0] = (((key_matrix[1][1] * key_matrix[2][2] - key_matrix[2][1] * key_matrix[1][2])) * determinant);
        inverse_key[0][0] = mod(inverse_key[0][0]);
        inverse_key[1][0] = ((-(key_matrix[1][0] * key_matrix[2][2] - key_matrix[2][0] * key_matrix[1][2])) * determinant);
        inverse_key[1][0] = mod(inverse_key[1][0]);
        inverse_key[2][0] = (((key_matrix[1][0] * key_matrix[2][1] - key_matrix[2][0] * key_matrix[1][1])) * determinant);
        inverse_key[2][0] = mod(inverse_key[2][0]);
        inverse_key[0][1] = ((-(key_matrix[0][1] * key_matrix[2][2] - key_matrix[2][1] * key_matrix[0][2])) * determinant);
        inverse_key[0][1] = mod(inverse_key[0][1]);
        inverse_key[1][1] = (((key_matrix[0][0] * key_matrix[2][2] - key_matrix[2][0] * key_matrix[0][2])) * determinant);
        inverse_key[1][1] = mod(inverse_key[1][1]);
        inverse_key[2][1] = ((-(key_matrix[0][0] * key_matrix[2][1] - key_matrix[2][0] * key_matrix[0][1])) * determinant);
        inverse_key[2][1] = mod(inverse_key[2][1]);
        inverse_key[0][2] = (((key_matrix[0][1] * key_matrix[1][2] - key_matrix[1][1] * key_matrix[0][2])) * determinant);
        inverse_key[0][2] = mod(inverse_key[0][2]);
        inverse_key[1][2] = ((-(key_matrix[0][0] * key_matrix[1][2] - key_matrix[1][0] * key_matrix[0][2])) * determinant);
        inverse_key[1][2] = mod(inverse_key[1][2]);
        inverse_key[2][2] = (((key_matrix[0][0] * key_matrix[1][1] - key_matrix[1][0] * key_matrix[0][1])) * determinant);
        inverse_key[2][2] = mod(inverse_key[2][2]);

        for (i = 0; i < ctext.length(); i += 3)
        {
            int x[3] = {0, 0, 0};
            for (j = 0; j < 3; j++)
            {
                x[j] = ctext[i + j] - 'A';
            }

            int result[3] = {0, 0, 0};
            for (j = 0; j < 3; j++)
            {
                for (k = 0; k < 3; k++)
                {
                    result[j] += inverse_key[j][k] * x[k];
                }
            }

            for (j = 0; j < 3; j++)
            {
                ptext += (char)((result[j] % 26) + 65);
            }
        }
        cout << endl;
        cout << "The plain text : " << ptext << endl
             << endl;
    }
};

class affine
{
    protected:
    void encryptAffine()
    {
        string plainText;
        int a, b;
        cout << "Enter key1 : ";
        cin >> a;
        cout << "Enter key2 : ";
        cin >> b;
        cout << "Enter plaintext : ";
        cin >> plainText;
        string cipherText = "";

        for (int i = 0; i < plainText.length(); i++)
        {
            // convert to uppercase
            if (plainText[i] >= 'a' && plainText[i] <= 'z')
            {
                plainText[i] = plainText[i] - 32;
            }

            // Encryption formula
            int x = (a * (plainText[i] - 65) + b) % 26;

            // convert to lowercase
            cipherText += (x + 65);
        }
        cout << endl;
        cout << "Cipher text : " << cipherText << endl
             << endl;
    }

    // function to compute the decryption
    void decryptAffine()
    {
        string cipherText;
        int a, b;
        cout << "Enter key1 : ";
        cin >> a;
        cout << "Enter key2 : ";
        cin >> b;
        cout << "Enter Cipher text : ";
        cin >> cipherText;
        string plainText = "";

        // Calculating the modular inverse of a
        int a_inv = 0;
        int flag = 0;
        for (int i = 0; i < 26; i++)
        {
            flag = (a * i) % 26;

            // Check if (a*i)%26 == 1, then i will be the modular inverse of a
            if (flag == 1)
            {
                a_inv = i;
            }
        }

        // Decryption formula
        for (int i = 0; i < cipherText.length(); i++)
        {
            // convert to uppercase
            if (cipherText[i] >= 'a' && cipherText[i] <= 'z')
            {
                cipherText[i] = cipherText[i] - 32;
            }

            int x = (a_inv * (cipherText[i] + 65 - b)) % 26;

            // convert to lowercase
            plainText += (x + 65);
        }
        cout << endl;
        cout << "Plain text : " << plainText << endl
             << endl;
    }
};

class input : public caesar, public vigenere, public hill, public affine
{
    public:
    input()
    {
        int n = 1;
        while (n != 0)
        {
            cout << "Choose the cipher scheme you want:" << endl;
            cout << "1. Caesar Cipher" << endl;
            cout << "2. Vigenere Cipher" << endl;
            cout << "3. Affine Cipher" << endl;
            cout << "4. Hill Cipher" << endl;
            cout << "5. Exit" << endl;
            int choice;
            cout << "Enter your choice : ";
            cin >> choice;

            if (choice == 1)
            {
                cout << "CAESAR CIPHER" << endl;
                cout << "1. Encrypt" << endl;
                cout << "2. Decrypt" << endl;
                cout << "Enter your choice: ";
                cin >> choice;
                if (choice == 1)
                {
                    cout << endl;
                    caesar_cipher_encryption();
                }
                else if (choice == 2)
                {
                    cout << endl;
                    caesar_cipher_decryption();
                }
            }

            else if (choice == 2)
            {
                cout << "VIGENERE CIPHER" << endl;
                cout << "1. Encrypt" << endl;
                cout << "2. Decrypt" << endl;
                cout << "Enter your choice: ";
                cin >> choice;
                if (choice == 1)
                {
                    cout << endl;
                    vigenere_encryption();
                }
                else if (choice == 2)
                {
                    cout << endl;
                    vigenere_decryption();
                }
            }

            else if (choice == 3)
            {
                cout << "AFFINE CIPHER" << endl;
                cout << "1. Encrypt" << endl;
                cout << "2. Decrypt" << endl;
                cout << "Enter your choice: ";
                cin >> choice;
                if (choice == 1)
                {
                    cout << endl;
                    encryptAffine();
                }
                else if (choice == 2)
                {
                    cout << endl;
                    decryptAffine();
                }
            }

            else if (choice == 4)
            {
                cout << "HILL CIPHER" << endl;
                cout << "1. Encrypt" << endl;
                cout << "2. Decrypt" << endl;
                cout << "Enter your choice: ";
                cin >> choice;
                if (choice == 1)
                {
                    cout << endl;
                    hill_cipher_encryption();
                }
                else if (choice == 2)
                {
                    cout << endl;
                    hill_cipher_decryption();
                }
            }

            else if (choice == 5)
            {
                n = 0;
                cout << endl
                     << "Exiting..." << endl;
            }
        }
    }
    ~input()
    {
        cout<<"\n Destructor Executed\n";
    }
};

int main()
{
    input A;
    return 0;
}
//GYBNQKURP
//RAJKFHBUR