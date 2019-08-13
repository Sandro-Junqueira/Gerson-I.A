prato1 = str('Prato 1: Arroz com Bife  R$:17,00')
prato2 = str('Prato 2: Macarrão bolonhesa  R$:12,00')
prato3 = str('Prato 3: Nhoque bolonhesa  R$:13,00')
prato4 = str('Prato 4: Strogonoff  R$:15,00')
prato5 = str('Prato 5: Escondidinho de Carne  R$:11,00')
prato6 = str('Prato 6: Escondidinho de Frango  R$:10,00')
prato7 = str('Prato 7: Sopa de Ervilha  R$:8,00')
prato8 = str('Prato 8: Salada do Chefe  R$:5,00')

print('\nOlá, bem vindo ao nosso restaurante. Eu me chamo Gerson')

from time import sleep 
for contagem in range(0,1):
    sleep(1)
    nmcliente = str(input('\nComo o(a) senhor(a) se chama? '))

print('\nSeja muito bem vindo', nmcliente,)

pergunta1 = str(input('\nJá conhece a nossa casa? '))

if pergunta1.upper() == 'NÃO':
    cardapio = str(input('\nGostaria então de ver nosso cardapio? '))
    if cardapio.upper() == 'SIM':
        print('\nAqui está nosso cardapio')
        print( '\n',prato1, '\n',prato2, '\n',prato3, '\n',prato4,
         '\n',prato5, '\n',prato6, '\n',prato7, '\n',prato8)
    
    pergunta2 = str(input('\nJá se decidiu? '))
    if pergunta2.upper() == 'SIM':
        anotarpedi = str(input('\nPoderia anotar seu pedido? '))
        if anotarpedi.upper() == 'SIM':
            pedido2 = str(input('\n'))
            if pedido2.upper() == 'VOU QUERER O PRATO 1':
                print('\nTudo bem, seu pedido já está sendo preparado!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 2':
                print('\nOK, irei preparar esse!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 3':
                print('\nCerto, vou prepara-lo imediadamente!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 4':
                print('\nAmante de Strogoff né? Vou mandar prepar!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 5':
                print('\nPerfeito, já está fazendo!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 6':
                print('\nOtima escolha!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 7':
                print('\nUma sopa saindo!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 8':
                print('\nOk, a iguraria do Chefe então!')
            
    elif pergunta2.upper() == 'NÃO':
        print('\nOk, assim que se decidir pode me chamar!')
        pedido6 = str(input('\n'))
        if pedido6.upper() == 'PODE ANOTAR MEU PEDIDO?':
            print('\nPosso sim, qual seria?')

            pedido7 = str(input('\n'))
            if pedido7.upper() == 'VOU QUERER O PRATO 1':
                print('\nTudo bem, seu pedido já está sendo preparado!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 2':
                print('\nOK, irei preparar esse!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 3':
                print('\nCerto, vou prepara-lo imediadamente!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 4':
                print('\nAmante de Strogoff né? Vou mandar prepar!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 5':
                print('\nPerfeito, já está fazendo!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 6':
                print('\nOtima escolha!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 7':
                print('\nUma sopa saindo!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 8':
                print('\nOk, a iguraria do Chefe então!')

        

elif pergunta1.upper() == 'SIM':
    pedido1 = str(input('\nPosso anotar seu pedido? '))
    if pedido1.upper() == 'SIM':
        pedido3 = str(input('\n'))
        if pedido3.upper() == 'VOU QUERER O PRATO 1':
            print('\nTudo bem, seu pedido já está sendo preparado!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 2':
            print('\nOK, irei preparar esse!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 3':
            print('\nCerto, vou prepara-lo imediadamente!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 4':
            print('\nAmante de Strogoff né? Vou mandar prepar!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 5':
            print('\nPerfeito, já está fazendo!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 6':
            print('\nOtima escolha!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 7':
            print('\nUma sopa saindo!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 8':
            print('\nOk, a iguraria do Chefe então!')
            
    elif pedido1.upper() == 'AINDA NÃO':
        print('\nOk, retornarei mais tarde')

        pedido4 = str(input('\n'))
        if pedido4.upper() == 'PODE ANOTAR MEU PEDIDO?':
            print('\nPosso sim, qual seria?')
            
            pedido5 = str(input('\n'))
            if pedido5.upper() == 'VOU QUERER O PRATO 1':
                print('\nTudo bem, seu pedido já está sendo preparado!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 2':
                print('\nOK, irei preparar esse!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 3':
                print('\nCerto, vou prepara-lo imediadamente!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 4':
                print('\nAmante de Strogoff né? Vou mandar prepar!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 5':
                print('\nPerfeito, já está fazendo!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 6':
                print('\nOtima escolha!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 7':
                print('\nUma sopa saindo!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 8':
                print('\nOk, a iguraria do Chefe então!')

from time import sleep 
print('\nPreparando pedido')
sleep(2)
print('Preparando pedido.')
sleep(2)
print('Preparando pedido..')
sleep(2)
print('Preparando pedido...')
sleep(2)
print('Finalizando pedido')
sleep(2)
print('Finalizando pedido.')
sleep(2)
print('Finalizando pedido..')
sleep(2)
print('Finalizando pedido...')
sleep(4)

print('\nSeu pedido está pronto, tenha um bom apetite!')