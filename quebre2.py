# import hashlib
import yescrypt

hash = input()

hash = hash.split(':')

if hash[0] == "Pimpolho":
    salt = hash[1][0:29]
    crip = hash[1][29:]
elif hash[0] == "testeadm":
    salt = hash[1][0:40]
    crip = hash[1][40:]

arquivo = open("dicionario.txt", "r", encoding='utf-8')

bytes = arquivo.readlines()

for palavra in bytes:
    palavra = palavra[0:-1]
    N = 2048
    r = 8
    p = 1
    nhash = yescrypt.yescrypt_kdf_body(palavra, salt, N, r, p)
    # nhash = hashlib.sha512(pala.encode('utf-8')).hexdigest()
    print(palavra)
    print(nhash.hex())
    if crip == nhash.hex():
        print("achou")
        print(palavra)
        break