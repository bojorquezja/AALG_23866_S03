# Haz una lista intencional para devolverme los números múltiplos de 3 
# a partir del 4 hasta el 20. [6,9,12,15,18]


a = [3*x for x in range(2,7,1)] 
print(a)

b = [x for x in range(4, 21) if x % 3 == 0] 
print(b)
