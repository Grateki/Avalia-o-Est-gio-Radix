n_de_testes = int(input(''))
for _ in range(n_de_testes):

    s = str(input(''))
    def palindromo_longo(palavra):
        palavra = palavra.upper()
        parte_longa = ""
        tem_palindromo = False
        for i in range(len(palavra)):
            for j in range(0, i):
                parte = palavra[j:i + 1]
                if parte == parte[::-1]:
                    tem_palindromo = True
                    if len(parte) > len(parte_longa):
                        parte_longa = parte 
        if not tem_palindromo:
            return "Sem resultados"
        return parte_longa
    if s.isalpha():
        print(palindromo_longo(s))
    elif s.isalnum():
        print("Entrada invalida")


""""Inicialmente, solicita as informações de input, 
criei uma variável para testar posteriormente a presença ou
ausência de palíndromo como true/false. Faço a checagem do meio 
até as bordas para determinar o maior palídromo da substring, 
caso não haja, retorna sem resultados, caso acha faz os testes 
para caracteres contidos em a a z e posteriomente entrada numerica."""
       
    
            
                       