#"%" es el módulo, el residuo de una división: 7%5=2, es decir, el residuo de dividir 7 entre 5 es igual a 2.
n=30
if(n%3==0)and(n%5==0):
	print("BeepBoop")
elif(n%5==0):
	print("Boop")
elif(n%3==0):
	print("Beep")
else:
	print(n)