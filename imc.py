altura = float(input('qual é sua altura? '))
peso = int(input('qual é seu peso? '))
s = peso/altura**2
print ('seu indice de massa corporal é igual a {:.2f}'.format(s))
if s > 25:
    print('voce precisa se alimentar melhor e fazer exercicios para se manter em forma')
elif s < 19:
    print('voce precisa ganhar peso, se alimente melhor')
else:
    print('Parabens seu peso esta ideal')