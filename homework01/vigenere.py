def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    k = list(keyword)
    a = list(plaintext)
    for i in range (0, len(a)):
        while len(k) < len(a):
            k.append(k[i])
            i += 1 
    for i in range (0, len(a)):
        if a[i].isalpha() == False:
            ciphertext += str(a[i])
            continue
        if a[i].istitle():
            if k[i].istitle():
                ciphertext += str(chr((ord(a[i]) + int(ord(k[i])) - int(ord("A")) - ord("A")) % 26 + ord("A")))
            else:
                ciphertext += str(chr((ord(a[i]) + int(ord(k[i])-32) - int(ord("A")) - ord("A")) % 26 + ord("A")))
        else:
            if k[i].istitle():
                ciphertext += str(chr((ord(a[i]) + int(ord(k[i])+32) - int(ord("a")) - ord("a")) % 26 + ord("a")))
            else:
                ciphertext += str(chr((ord(a[i]) + int(ord(k[i])) - int(ord("a"))  - ord("a")) % 26 + ord("a")))
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    k = list(keyword)
    a = list(ciphertext)
    for i in range (0, len(a)):
        while len(k) < len(a):
            k.append(k[i])
            i += 1 
    for i in range (0, len(a)):
        if a[i].isalpha() == False:
            plaintext += str(a[i])
            continue
        if a[i].istitle():
            if k[i].istitle():
                plaintext += str(chr((ord(a[i]) - int(ord(k[i])) - int(ord("A"))  - ord("A")) % 26 + ord("A")))
            else:
                plaintext += str(chr((ord(a[i]) -  int(ord(k[i])-32) - int(ord("A")) - ord("A")) % 26 + ord("A")))
        else:
            if k[i].istitle():
                plaintext += str(chr((ord(a[i]) - int(ord(k[i])+32) - int(ord("a")) - ord("a")) % 26 + ord("a")))
            else:
                plaintext += str(chr((ord(a[i]) - int(ord(k[i])) - int(ord("a"))  - ord("a")) % 26 + ord("a")))
    return plaintext