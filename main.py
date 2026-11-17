from SQL import alunos, verificacao_aluno, verificacao_senha
#Importa do arquivo SQL.py três coisas: a lista alunos (os dados) e as funções verificacao_aluno e verificacao_senha.
from media import  calculo_media
#Importa a função calculo_media do arquivo media.py.

print('Olá aluno!')


while True:
#Cria o loop principal. Ele repete o programa inteiro (menu, login, média) até que o usuário escolha sair.

    print('Vamos realizar a verificação da sua  nota')
    print('Escolha uma das opções abaixo')
    print('Digite - 1 para verificar sua media')
    print('Digite - 2 para sair')

    while True:
    #Loop interno que só termina quando o usuário digitar uma opção válida.

        digito = input('Opção: ')


        try:
                digito = int(digito)
        #Tenta converter o texto para número inteiro. Por exemplo, "1" vira 1.

        except ValueError:
            print('Valor inválido. Por favor, digite novamente.')
            continue
        #Se a conversão falhar (ex.: o usuário digitou "abc")
        #O Python gera um ValueError. O except captura o erro, avisa o usuário e o continue volta ao início do loop interno para pedir de novo.

        if digito in (1, 2):
            break
        #Se o número for 1 ou 2, o break sai do loop de validação e o programa segue.
        print('Opção inexistente, escolha de 1 a 2')

    if digito == 2:
        break
    #Se escolheu 2, o break sai do loop principal e o programa termina. Se escolheu 1, continua.


    while True:
    #Repete até o usuário digitar um nome que exista.
         
        nome = input('Digite seu nome: ')

        resultado_nome = (verificacao_aluno(alunos, nome))
        #Chama a função que procura o nome na lista alunos. Ela devolve o dicionário do aluno se achar, ou None se não achar.

        if resultado_nome is not None:
            print(f'Ola {nome}!')
            break
        #Se encontrou o aluno, cumprimenta pelo nome (a f-string insere o valor de nome no texto) e o break sai do loop do nome.
        else:
             print('Nome não encontrado')

    while True:
    #Repete até a senha estar correta.
             
        senha = input('Digite sua senha: ')
    
        resultado_senha = (verificacao_senha(resultado_nome, senha))
        #Chama a função que confere a senha do aluno encontrado. Ela converte a senha para int e compara. Devolve o aluno se estiver certa, ou None se estiver errada.
    
        if resultado_senha is not None:
            print('Senha valida!')
            print('Acesso autorizado!')
            break
        #Se a senha estiver certa, mostra as mensagens e sai do loop.
        else:
            print('Senha invalida!')

    notas = resultado_senha['notas']
    #Pega do dicionário do aluno a lista de notas.

    media = calculo_media(notas)
    #Chama a função que soma as notas, divide pela quantidade

    print(f'Notas: {notas}')
    print(f'Média: {media}')
    print('Verificação finalizada!\n')
        