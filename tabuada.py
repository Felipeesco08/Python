n = int(input('Digite o numero da tabuada:'))
ni = int(input('Digite o numero de inicio da tabuada:'))
nf = int(input('Digite o numero final da tabuada:'))
x = nf + 1

while ni<x:
 m = n*ni
 print(f'{n} x {ni} = {m}')
 ni +=1
