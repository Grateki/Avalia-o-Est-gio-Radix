n_de_testes = int(input(''))
for _ in range(n_de_testes):
	fibseq = [1,1]
	i = 0
	num = int(input(''))
	while num > len(fibseq):
		fibseq.append(fibseq[i] + fibseq[i+1])
		i+=1

	print (f'Fib({num}) = {fibseq[num-1]}')


"""Fibonacci é uma sequência de números, onde a sequência inicia com 0 e 1, e os números
 seguintes serão a soma dos dois números anteriores. Inicialmente, o código solicita a
 informação de input. Comparo com o referencial e faço a soma, printando o valor referente
 aquele numero na sequencia de Fibonacci na tela."""