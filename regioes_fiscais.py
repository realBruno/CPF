regiao_fiscal = input('Por favor, insira o estado onde o CPF deve ser gerado.' \
    + ' Ex.: SP\n')

regiao_fiscal = regiao_fiscal.upper()

regiao_1 = 'DF', 'GO', 'MS', 'MT', 'TO'
regiao_2 = 'AC', 'AM', 'AP', 'PA', 'RO', 'RR'
regiao_3 = 'CE', 'MA', 'PI'
regiao_4 = 'AL', 'PB', 'PE', 'RN'
regiao_5 = 'BA', 'SE'
regiao_6 = 'MG'
regiao_7 = 'ES', 'RJ'
regiao_8 = 'SP'
regiao_9 = 'PR', 'SC'
regiao_0 = 'RS'

if regiao_fiscal in regiao_1:
    regiao_fiscal = 1
elif regiao_fiscal in regiao_2:
    regiao_fiscal = 2
elif regiao_fiscal in regiao_3:
    regiao_fiscal = 3
elif regiao_fiscal in regiao_4:
    regiao_fiscal = 4
elif regiao_fiscal in regiao_5:
    regiao_fiscal = 5
elif regiao_fiscal in regiao_6:
    regiao_fiscal = 6
elif regiao_fiscal in regiao_7:
    regiao_fiscal = 7
elif regiao_fiscal in regiao_8:
    regiao_fiscal = 8
elif regiao_fiscal in regiao_9:
    regiao_fiscal = 9
else:
    regiao_fiscal = 0