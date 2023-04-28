from crypt import crypt

# hash = 'Pimpolho:$y$j9T$nFwHNF0c3SCbH6ESyzSKw.$ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00:19472:0:99999:7:::'
hash = 'testeadm:$y$j9T$5LImmws2fco9AeRmLSB2j0$fYPmdqu1Q/FDiwPJgkCIW9wX76w12SNEiYAodUzafo5:19472:0:99999:7:::'

hash = hash.split(':')
salt = hash[1][0:29]

arquivo = open("dicionario.txt", "r", encoding='utf-8')

bytes = arquivo.readlines()

for palavra in bytes:
    for i in range(0,10):
        palavra = palavra[0:-1]+f'{i}'
        nhash = crypt(palavra, salt=salt)

        print(palavra)
        print(nhash)
        if hash[1] == nhash:
            print()
            print("Achou a senha:")
            print(palavra)
            print()
            break