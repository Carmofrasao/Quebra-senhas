# Quebra senhas

## Exercício 1:

### Escreva um programa que a quebre usando força bruta, considerando palavras de 5 caracteres e meça o tempo

* Senha: 
    * senha
* Tempo:
    * real	0m0,337s
    * user	0m0,295s
    * sys	0m0,041s

## Exercício 2:
https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
### Qual porção é o SALT e qual a senha? Que função é usada?
* Senha 1:
    * $y$j9T$nFwHNF0c3SCbH6ESyzSKw.
    * abacate
    * yescript
    * Tempo: Instantâneo 

* Senha 2:
    * $y$j9T$5LImmws2fco9AeRmLSB2j0
    * 123admin
    * yescript
    * Tempo: 4,6 horas

### Como gerar esse tipo de senha no Linux (em detalhes)?
* Crie uma string com caracteres aleatórios;
* Crie a senha desejada;
* Concatene a string com a senha;
* Criptografe com o algoritmo yescript.

### Quebre as duas senhas e explique o processo

Visto que ja temos a hash da senha e o salt, usando um dicionario, foi concatenado o salt sobre cada palavra e essa string foi criptografada usando yescript, assim para cada string gerada, foi feita a comparação com a hash original.