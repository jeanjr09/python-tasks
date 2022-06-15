# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
#    (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
#    ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#    IMPORTANTE:
#    Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


fibo = [1,1]
i = 0
num = int(input("Digite um número inteiro: "))

while num > len(fibo):
	fibo.append(fibo[i] + fibo[i+1])
	i+=1


print ('Fibonacci(%d): %d' %(num,fibo[num-1]))

if num in fibo:
    print("Este número pertence a sequência de Fibonacci")
else:
    print("Este número não pertence a sequência de Fibonacci")