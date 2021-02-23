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
    n = len(k)
    a = list(plaintext)
    b = len(a)
    for i in range (0, b):
        while n < b:
            k.append(k[i])
            n += 1 
            i += 1 
    for i in range (0, b):
        if a[i].isalpha() == False:
            ciphertext += str(a[i])
            continue
        if a[i].istitle():
            if k[i].istitle():
                shift = int(ord(k[i])) - int(ord("A")) 
                ciphertext += str(chr((ord(a[i]) + shift - ord("A")) % 26 + ord("A"))) 
            else:
                shift = int(ord(k[i])-32) - int(ord("A"))
                ciphertext += str(chr((ord(a[i]) + shift - ord("A")) % 26 + ord("A"))) 
        else:
            if k[i].istitle():
                shift = int(ord(k[i])+32) - int(ord("a"))
                ciphertext += str(chr((ord(a[i]) + shift - ord("a")) % 26 + ord("a")))
            else:
                shift = int(ord(k[i])) - int(ord("a")) 
                ciphertext += str(chr((ord(a[i]) + shift - ord("a")) % 26 + ord("a")))
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
    n = len(k)
    a = list(ciphertext)
    b = len(a)
    for i in range (0, b):
        while n < b:
            k.append(k[i])
            n += 1 
            i += 1 
    for i in range (0, b):
        if a[i].isalpha() == False:
            plaintext += str(a[i])
            continue
        if a[i].istitle():
            if k[i].istitle():
                shift = int(ord(k[i])) - int(ord("A")) 
                plaintext += str(chr((ord(a[i]) - shift - ord("A")) % 26 + ord("A"))) 
            else:
                shift = int(ord(k[i])-32) - int(ord("A"))
                plaintext += str(chr((ord(a[i]) - shift - ord("A")) % 26 + ord("A"))) 
        else:
            if k[i].istitle():
                shift = int(ord(k[i])+32) - int(ord("a"))
                plaintext += str(chr((ord(a[i]) - shift - ord("a")) % 26 + ord("a")))
            else:
                shift = int(ord(k[i])) - int(ord("a")) 
                plaintext += str(chr((ord(a[i]) - shift - ord("a")) % 26 + ord("a")))
    return plaintext
