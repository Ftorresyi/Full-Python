#Testes de Regex feitos no site https://regex101.com/

import re

# o operador .  -> (ponto) significa qq ocorrência de qq caracter
# o operador {}  -> (chaves) especifica o intervalo de ocorrencias do operador do seu lado esquerdo.
# o operador () -> (parenteses) serve para agrupar os operadores e formar um grupo de matches.
# o operador |  -> (pipe) especifica que pode ser um dos dois caracteres que estiverem ao lado do pipe.
# o operador \X -> é a mesma coisa que escrever (?:.), que localizará qualquer caracter naquele espaço.
# EX: '.{0,2}' diz q eu posso ter de 0 e 2 ocorrências de qq caracter naquele espaço.
# EX: '1|2' diz que naquela posição pode sempre ocorrer ou o numero 1 ou o numero 2

# a flag /g  ->(global) diz para buscar todas as ocorrencias do padrão (nao retorna após o primeiro match)
# a flag /i  ->(insensitive) diz que é insensível a letras maiúsculas ou minusculas.
# EX: 1|2(:?..)\s1|2(:?..) /gi -> buscará no texto todas as ocorrencias desse padrão sem se importar com maiusculas ou minusculas

#'1|2(:?..)\s1|2(:?..)\sGT'   -> engloba as OMs: '1/1 GT, 1/2 GT, 2/2 GT'
#'1(?:.{0,2})CJM'  -> engloba todas as formas de escrever 1 CJM, 1CJM, 1* CJM, etc..

OMs=[r'1|2(:?.{0,3})1|2(:?.{0,3})GT/gi', r'PRIMEIRO DO SEGUNDO GRUPO DE TRANSPORTE/gi', 
    r'PRIMEIRO DO PRIMEIRO GRUPO DE TRANSPORTE/gi', r'SEGUNDO DO SEGUNDO GRUPO DE TRANSPORTE/gi',

    r'1(?:.{0,2})CJM/gi', r'PRIMEIRA CIRCUNSCRI\\X{2}O JUDICI\\XRIA MILITAR/gi',

    r'GAP(?:.{0,2})GL/gi', r'GRUPAMENTO DE APOIO DO GALE\\XO/gi',
    r'PAMA(?:.{0,2})GL/gi', r'PARQUE DE MATERIAL AERONÁUTICO DO GALE(?:.)O/gi',  
    r'BAGL/gi', r'BASE A\\XREA DO GALEAO', r'BAGL(?:.{0,2})ANTIGA'
    r'CMRJ/gi',r'COL\\XGIO MILITAR DO RIO DE JANEIRO/gi',
    r'1(?:.{0,2})CJM/gi', r'PRIMEIRA CIRCUNSCRI\\X{2}O JUDICI\\XRIA MILITAR/gi',
    r'1(?:.{0,2})GCC/gi', r'PRIMEIRO GRUPO DE COMUNICA\\X{2}ES E CONTROLE/gi',
   ]

#Testando as busca das Palavras: 

texto= 'GAP GL PAMA-GL PAMAGL pamagl pama gl 1 /2 GT, 2/2 GT'
space = r'\\s'
pal=[]
for i in range(len(OMs)):
    if re.findall(OMs[i], texto.upper()):
        print('Foi encontrada a palavra: ', OMs[i])
    else: print('Não foi encontrada a palavra: ', i)
    """ while (texto[i] != space):
        pal=texto[i]
    print(pal) """
        

