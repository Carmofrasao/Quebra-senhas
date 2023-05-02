from crypt import crypt

# hash = 'Pimpolho:$y$j9T$nFwHNF0c3SCbH6ESyzSKw.$ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00:19472:0:99999:7:::'
hash = 'testeadm:$y$j9T$5LImmws2fco9AeRmLSB2j0$fYPmdqu1Q/FDiwPJgkCIW9wX76w12SNEiYAodUzafo5:19472:0:99999:7:::'

hash = hash.split(':')
salt = hash[1][0:29]

arquivo = open("rockyou.txt", "r", encoding='latin1')

lines = list(lined for line in arquivo if len(lined := line.strip()) <= 8)
for i, palavra in enumerate(lines, 1):
    palavra = palavra.strip()
    if len(palavra) > 8:
        continue
    nhash = crypt(palavra, salt=salt)

    print(f'{i}/{len(lines)} {palavra}')
    print(nhash)
    if hash[1] == nhash:
        print()
        print("Achou a senha:")
        print(palavra)
        print()
        break