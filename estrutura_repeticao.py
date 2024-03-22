

texto = input("informe o nome " )
VOGAIS = "AEIOU"

for letras in texto:
   if letras.upper() in VOGAIS:
      print(letras, end="")
else:
   print("acabou")


   for numero in range (1, 100 , 2):
      print(numero, end=" ")
      