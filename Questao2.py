n_de_testes = int(input(''))
for _ in range(n_de_testes):
    elementos_matriz = int(input(''))
    print('Matrix',elementos_matriz,'X',elementos_matriz)
    desenha_matriz = [0] * elementos_matriz
    desenha_matriz = [[0] * i + [1] + [0] * (elementos_matriz - i - 1) for i in range(elementos_matriz)]
    for linha in desenha_matriz:
        
        print(''.join([str(elemento) for elemento in linha]))
        
        
        """ Inicialmente, o código solicita as informações de input. Posteriormente, 
        traço o desenho da matriz quadrada com a informação do input, sendo que matrizes
        quadradas possuem a mesma quantidade de linhas e colunas. O código estabelece escrever
        o número 1 na posição da linha de acordo com o número da linha, formando a diagonal."""

