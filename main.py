# Programa que gera CPFs
# 19/10/2024 (backend)
# 26/10/2024 (frontend)

import random
import regioes_fiscais as regioes

# gera os oito primeiros caracteres do cpf
cpf = ''.join(random.choices('0123456789', k=8))

# adiciona pontos ao cpf
cpf = '.'.join(cpf[i:i+3] for i in range(0, len(cpf), 3)) + \
    str(regioes.regiao_fiscal)

# ENCONTRAR PRIMEIRO DÍGITO VERIFICADOR

digito_um, decremente = 0, 10
copia_cpf = cpf

# obtém valores dentro do objeto map e coloca-os em uma lista
cpf = [numero for numero in map(int, cpf.replace('.','').replace('-', ''))]

for i in range(len(cpf)):
    digito_um += cpf[i]*decremente
    decremente -= 1

digito_um %= 11
digito_um = 11 - digito_um if digito_um >= 2 else 0

copia_cpf += f'-{digito_um}'

# ENCONTRAR SEGUNDO DÍGITO VERIFICADOR

cpf = copia_cpf; copia_cpf = list(copia_cpf)

for i in copia_cpf:
    if i.isdigit() == False:
        copia_cpf.remove(i) # remove os caracteres '.' e '-'

copia_cpf = [eval(i) for i in copia_cpf] # transforma elementos da lista em int

digito_dois, decremente = 0, 11

for i in range(len(copia_cpf)):
    digito_dois += copia_cpf[i]*decremente
    decremente -= 1

digito_dois %= 11
digito_dois = 11 - digito_dois if digito_dois >= 2 else 0

cpf += f'{digito_dois}'

print(cpf)