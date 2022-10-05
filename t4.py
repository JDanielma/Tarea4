import math
a = float(input("a"))
b = float(input("b"))
n = float(input("n"))
h = (b-a)/n
x = 2

def primera (x):
	return (pow(math.e,pow(x,2)))
def segunda(x):
	return (1 + pow(math.e,(-1 * x))*math.sin(4*x))
def tercera(x):
	return (math.sin(math.pi*x))
def cuarta(x):
	return (1 + pow(math.e,(-1 * x))*math.cos(4*x))
def quinta(x):
	return (math.sin(math.sqrt(x)))
sum3 = 0
sum2 = 0
# for i in range (1,int(n)):
# 	if i % 3 != 0:
# 		xi = a+(i*h)
# 		
# 		sum3= sum3 + primera(xi)
# sum3 = 3 * sum3
# 
# for j in range (1,int((n/3))):	
# 	sum2= sum2 + primera(a+(3*j*h))
# sum2 = 2 * sum2

for i in range (1,int(n)):
	if i % 3 != 0:
		xi = a+(i*h)
		
		sum3= sum3 + segunda(xi)
sum3 = 3 * sum3

for j in range (1,int((n/3))):	
	sum2= sum2 + segunda(a+(3*j*h))
sum2 = 2 * sum2


simp = (3/8)*h*(segunda(a) + sum3 + sum2 + segunda(b))
print(simp)



#print(primera(x))
#print(segunda(x))
#print(tercera(x))
#print(cuarta(x))
#print(quinta(x))


 	
