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
        #print(f"| {' | '.join(row)} |") second option
        print('| ' + ' | '.join(row) + ' |') #third option
        if i == 0:
            print('|---' *len(row) + '|')

def letter_index(letter, alphabet):
    letter = letter.lower()
    for i, l in enumerate(alphabet.lower()):
        if i == letter:
            return l
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
    ciphertext = list((plain_l + key_w) % len(alphabet))
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
    plain_text = list((cipher_char - key_char + len(alphabet)) % len(alphabet))
    return index_letter(plain_text, alphabet)

def decrypt(key, cipher_letter, alphabet):
    plaintext = []
    k_len = len(key)
    for i, l in enumerate(cipher_letter):
        plaintext.append(undo_vigenere_index(key[i%k_len], l, alphabet))
    return ''.join(plaintext)

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vig_list = get_vigenere_sq(alphabet)
    better_vigenere(vig_list)

if __name__ == '__main__':
    main()