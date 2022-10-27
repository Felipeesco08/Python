n1 = int(input('numero ='))
n2 = int(input('numero ='))

soma = n1 +n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2

od = str(input('Operação desejada ='))

if od == '+':
 print(soma)
elif od == '-':
 print(sub)
elif od == '*':
 print(multi)
elif od == '/':
 print(div)
else:
 print('categoria inválida')
