import re


OMs=[
    'GAP(?:.)GL','GRUPAMENTO DE APOIO DO GALE*O', 'GAPGL',
    'PAMA(.)GL','PARQUE DE MATERIAL AERONÁUTICO DO GALE(?:.)O',  
    'BAGL','BASE AÉREA DO GALEAO','BAGL*ANTIGA'
    'CMRJ','COL*GIO MILITAR DO RIO DE JANEIRO',
    '1(?:.)CJM','PRIMEIRA CIRCUNSCRI*O JUDICI*RIA MILITAR','1CJM'
    ' 1(?:.)/2(?:.)GT','PRIMEIRO ESQUADRÃO DO SEGUNDO GRUPO DE TRANSPORTE','2/2 GT'
    ' 1*GCC','PRIMEIRO GRUPO DE COMUNICA*ES E CONTROLE',
    ' 1*/*1 GT','PRIMEIRO ESQUADRÃO DO PRIMEIRO GRUPO DE TRANSPORTE',
    ' 2*/2* GT','SEGUNDO ESQUADR*O DO SEGUNDO GRUPO DE TRANSPORTE',
   ]

busca = 'GAP GL PAMA-GL PAMAGL pamagl pama gl 1 /2 GT, 2/2 GT'
for i in range(len(OMs)):
    if re.findall(OMs[i], busca.upper()):
        print('Foi encontrada a palavra: ', OMs[i])
    else: print('Não foi encontrada a palavra: ')


