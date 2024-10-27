def gera_cpf():
    import random
    cpf = ''.join(random.choices('0123456789', k=9))
    cpf = '.'.join(cpf[i:i+3] for i in range(0, len(cpf), 3))
    # ENCONTRAR PRIMEIRO DÍGITO VERIFICADOR

    digito_um, decremente = 0, 10
    copia_cpf = cpf

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
            copia_cpf.remove(i)

    copia_cpf = [eval(i) for i in copia_cpf]

    digito_dois, decremente = 0, 11

    for i in range(len(copia_cpf)):
        digito_dois += copia_cpf[i]*decremente
        decremente -= 1

    digito_dois %= 11
    digito_dois = 11 - digito_dois if digito_dois >= 2 else 0
    cpf += f'{digito_dois}'
    return cpf