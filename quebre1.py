import hashlib

chave = 'e8d95a51f3af4a3b134bf6bb680a213a'

arquivo = open("dicionario.txt", "rb")

bytes = arquivo.readlines()

for palavra in bytes:
    palavra = palavra[0:5]
    hash = hashlib.md5(palavra).hexdigest()

    if(chave == hash):
        print("achou")
        print(palavra)
        break
