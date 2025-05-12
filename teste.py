from datetime import datetime
atual = datetime.today().year
usuario = int(input('Digite seu ano de nascimento: '))
idade = atual - usuario
print(f'Você tem {idade} anos.')
