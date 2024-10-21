import sys


def get_vigenere_sq(alphabet):
    rows = []
    for i in range(len(alphabet)):
        if i == 0:
            row = ' ' + alphabet[i:] + alphabet[:i]
            rows.append(list(row))
        row = alphabet[i] + alphabet[i:] + alphabet[:i]
        rows.append(list(row))
    return rows

def better_vigenere(rows):
    for i, row in enumerate(rows):
        print('|', end= '')  #first option
        print(' | '.join(row))
        print(' |')
        if i == 0:
            print('---')

def letter_index(letter, alphabet):
    letter = letter.lower()
    for i, l in enumerate(alphabet.lower()):
        if l == letter:
            return i
    return -1

def index_letter(index, alphabet):
    if 0 < index:
        return alphabet[index]
    elif index < len(alphabet):
        return alphabet[index]
    return -1

def vigenere_index(key, plaintext, alphabet):
    plain_l = letter_index(plaintext, alphabet)
    key_w = letter_index(key, alphabet)
    ciphertext = (plain_l + key_w) % len(alphabet)
    return index_letter(ciphertext, alphabet)

def encrypt(key, plaintext, alphabet):
    ciphertext = []
    k_len = len(key)
    for i, l in enumerate(plaintext):
        ciphertext.append(vigenere_index(key[i%k_len], l, alphabet))
    return ''.join(ciphertext)

def undo_vigenere_index(key, cipher_letter, alphabet):
    cipher_char = letter_index(cipher_letter, alphabet)
    key_char = letter_index(key, alphabet)
    plain_text = (cipher_char - key_char + len(alphabet)) % len(alphabet)
    return index_letter(plain_text, alphabet)

def decrypt(key, cipher_letter, alphabet):
    plaintext = []
    k_len = len(key)
    for i, l in enumerate(cipher_letter):
        plaintext.append(undo_vigenere_index(key[i%k_len], l, alphabet))
    return ''.join(plaintext)

def instructions(menu, skip):
    while True:
        for i in range(len(menu) - skip):
            print(menu[i][0])
        try:
            choose = int(input('choose what you wish to do: '))
            if choose in menu[-1]:
                choose -= 1
                if menu[choose][3] is not None:
                    menu[choose][3].append(menu[choose][1](*menu[choose][2]))
                else:
                    menu[choose][1](*menu[choose][2])
            else:
                raise ValueError
        except ValueError:
            print("Improper choice. Please select one of the following: " + str(menu[-1]))

def encrypt_menu(key,alphabet):
    plaintext = input('please introduce what you want to encrypt: ')
    return encrypt(key, plaintext, alphabet)

def decrypt_menu(key, alphabet, encrypted_list):
    for ciphertext in encrypted_list:
        print(decrypt(key, ciphertext, alphabet))

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #vig_list = get_vigenere_sq(alphabet)
    #print(vig_list)
    encrypt_list = []
    key = 'world'
    menu = [
        ['1- Encrypt', encrypt_menu, [key, alphabet], encrypt_list],
        ['2- Decrypt', decrypt_menu, [key, alphabet, encrypt_list], None],
        ['3- Quit', sys.exit, [0], None],
        [1, 2, 3]
    ]
    print(instructions(menu, 1))


if __name__ == '__main__':
    main()

key = input('insert the keyword desired: ')
plaintext = input('please introduce your plaintext: ')