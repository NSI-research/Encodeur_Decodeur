import time

alphabet = [
    'M',
    'n',
    '!',
    'è',
    '6',
    '(',
    't',
    '4',
    'S',
    'v',
    'A',
    'N',
    'b',
    'F',
    'g',
    'K',
    'd',
    ',',
    ':',
    'z',
    'D',
    'T',
    's',
    'V',
    '5',
    'J',
    'p',
    'j',
    '9',
    'à',
    ';',
    '&',
    '/',
    'h',
    'c',
    'u',
    '.',
    'm',
    'C',
    'U',
    'i',
    'o',
    '?',
    '0',
    ')',
    '7',
    'y',
    'H',
    'Z',
    'a',
    'R',
    'r',
    '3',
    'W',
    'Y',
    'O',
    'L',
    'é',
    'E',
    'f',
    '1',
    '2',
    ' ',
    'P',
    'l',
    'x',
    'Q',
    'ù',
    '8',
    'e',
    'q',
    'X',
    'G',
    'w',
    'k',
    'B',
    'I',
    "'",
    'ç'
]

def encode(x, x2):
    r = ""
    for i in x:
        if alphabet.index(i) >= (79 - x2):
            j = alphabet.index(i) + (x2 - 79)
            r += alphabet[j]
        else:
            j = alphabet.index(i) + x2
            r += alphabet[j]
    print(f"Votre message encoder avec la clé {x2} est :\n\n{r}\n")
    time.sleep(0.1)

def decode(x, x2):
    r = ""
    for i in x:
        if alphabet.index(i) < x2:
            j = alphabet.index(i) + (79 - x2)
            r += alphabet[j]
        else:
            j = alphabet.index(i) - x2
            r += alphabet[j]
    print(f"Votre message décodé avec la clé {x2} est :\n\n{r}")
    time.sleep(0.1)


w = 2

while w != "Non" and w != "non":
    q = input("\nA encoder ou décoder ? Dites 1 ou 2 : ")
    if q == "1":
        x = input("Donnez un message à encoder : ")
        x2 = int(input("Avec quelle clé ? Donnez un nombre entier natuel : "))
        encode(x, x2)
        w = input("Souhaitez-vous recommencer ?")
    elif q == "2":
        x = input("Donnez un message à décoder : ")
        x2 = int(input("Avec quelle clé ? Donnez son nombre entier natuel : "))
        decode(x, x2)
        w = input("Souhaitez-vous recommencer ?")