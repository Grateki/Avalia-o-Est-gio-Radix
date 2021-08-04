n_de_testes = int(input(''))
for _ in range(n_de_testes):
    linha = input('')
    s,c = linha.split()
    i = 0
    contador = 0

    if c.isalpha() and len(c)==1:
        while(i<len(s)):
            if(s[i] == c):
                contador = contador + 1
            i = i + 1
        frenquencia = {letra : s.count(letra) for letra in set(s)}
        print (f'{s}{str(frenquencia)}')
        print(contador)

    elif c.isdigit():
        print("consulta inválida")
        
    elif (len(c))>1:
        print("consulta inválida")


""" Inicialmente, o código solicita as informações de input. criei uma condicional 
para verificar se c está contido no intervalo de a a z e estabeleci que a leitura seria realizado apenas caso o tamanho de c=1. Criei uma outra 
condição para alocar os valores do caracter do input dentro de um contador. Após, realizanfo os testes para verificar se possui números contidos em c, e
se c é maior que 1."""


