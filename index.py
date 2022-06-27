#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. US$1,00=R$5,23
v =float(input('Quantos reais você tem? R$'))
d =float(v/5.23)
print('Com R${:.2f} você pode comprar US${:.2f}' .format(v, d))