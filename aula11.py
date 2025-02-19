#ordem de execução 
#1. (n + n) operador em parenteses 
#2. ** exponenciacao 
#3. * / // % (multiplicacao, divisão, divisão de inteiros, e modulo(resto da divisão))
#4. + - (soma, subtração)

# aqui quero demonstrar o quanto a ordem de execução dos fatores altera o resultado

exemplo1 = 1 + 1 ** 5 + 5 
print(exemplo1)
# primeiro foi realizada a exponenciacao = 1, e depois a soma (1+1+5) = 7

exemplo2 = (1 + 1) ** (5 +  5) 
print(exemplo2)
# primeiro parenteses = (2) + (10) depois, potenciacao, 2**10, = 1024

exemplo3 = (1 + 1) ** 5 + 5
print(exemplo3)
# primeiro parenteses = (2) depois, potenciacao, 2**5 = 32, depois soma, 32 + 5 = 37
