# 5) Escreva um programa que inverta os caracteres de um string.

str= input("Digite uma palavra: ")

length_str=len(str)

sliced_str=str[length_str::-1] 
print ("Caracteres invertidos:",sliced_str)