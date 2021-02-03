import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for s in range(len(plaintext)):
        if ord('a') <= ord(plaintext[s]) <= ord('z'):
            ciphertext += chr(((ord(plaintext[s]) - ord('a') + shift) % 26) + ord('a'))
        elif ord('A') <= ord(plaintext[s]) <= ord('Z'):
            ciphertext += chr(((ord(plaintext[s]) - ord('A') + shift) % 26) + ord('A'))
        else:
            ciphertext += plaintext[s]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for s in range(len(ciphertext)):
        if ord('a') <=  ord(ciphertext[s]) <= ord('z'):
            plaintext += chr(((ord(ciphertext[s]) - ord('a') - shift) % 26) + ord('a'))
        elif ord('A') <= ord(ciphertext[s]) <= ord('Z'):
            plaintext += chr(((ord(ciphertext[s]) - ord('A') - shift) % 26) + ord('A'))
        else:
            plaintext += ciphertext[s]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    for text in ciphertext.split():
        for i in range(0,26):
            decrypt_word = decrypt_caesar(text, i)
            if decrypt_word in dictionary:
                best_shift = i
    return best_shift
