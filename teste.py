from datetime import datetime
atual = datetime.today().year
usuario = int(input('Digite seu ano de nascimento: '))
idade = atual - usuario
print(f'Você tem {idade} anos.')
if idade >= 10:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
