print("Dame tu edad")
age=input()
int(age)
if(int(age)<18):
	print("Eres menor de edad")
else:
	print("Eres mayor de edad")

if(int(age)<18):
	if(int(age)==1):
		print("Con",age,"año, eres menor de edad")
	else:
		print("Con",age,"años, eres menor de edad")
else:
	print("Con",age,"años, eres mayor de edad")

if(int(age)==1):
	print("Con",age,"año, eres menor de edad")
elif(int(age)<18):
	print("Con",age,"años, eres menor de edad")
else:
	print("Con",age,"años, eres mayor de edad")

