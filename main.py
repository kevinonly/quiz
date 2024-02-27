lista_pergunta = ['Qual a capital da Espanha?',
                  'Qual o maior país do planeta?',
                  'Qual país fica tokyo?',
                  'Qual país é famoso por chocolate?',
                  'Em qual país se localiza o Rio amazonas?',
                  'Qual a capital da Inglaterra?',
                  'País conhecidos pelas grandes pirâmides?',
                  'Qual país a capital é Roma?']

lista_resposta = ['madrid', 'rússia', 'japão', 'suiça', 'brasil', 'londres', 'egito', 'itália']

c = 0
pt = 0

while True:
    if c <= 7:
        print(lista_pergunta[c])
        for contagem in range(0,3):
            resposta = str(input('-> '))
            if resposta.lower() == lista_resposta[c]:
                print('certo! +1 pt')
                pt += 1
                c += 1
                break
            elif contagem == 2:
                c += 1
            else:
                print('errado\n')
                resposta = ''
    else:
        if pt <= 3:
            print(f'Quem sabe uma nova tentativa, pontuação: {pt}')
        elif 7 > pt >= 4:
            print(f'Boa pontuação, {pt} pontos!')
        else:
            print(f'\nUau, {pt} pontos? Incrível!')
        break
