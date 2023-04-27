from crypt import crypt

hash = 'Pimpolho:$y$j9T$nFwHNF0c3SCbH6ESyzSKw.$ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00:19472:0:99999:7:::'
# hash = 'testeadm:$y$j9T$5LImmws2fco9AeRmLSB2j0$fYPmdqu1Q/FDiwPJgkCIW9wX76w12SNEiYAodUzafo5:19472:0:99999:7:::'

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
    nhash = crypt(palavra, salt=salt)

    print(palavra)
    print(nhash)
    if hash[1] == nhash:
        print()
        print("Achou a senha:")
        print(palavra)
        print()
        break