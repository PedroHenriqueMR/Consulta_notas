alunos = [
#Cria uma variável chamada alunos que guarda uma lista.
{'nome':'Pedro', 'notas': [9,8,10], 'senha': 123},
{'nome':'Daniel', 'notas': [9,8,10], 'senha': 234},
{'nome':'Leandro', 'notas': [9,8,10], 'senha': 345},
{'nome':'Cleusa', 'notas': [9,8,10], 'senha': 456},
{'nome':'Leticia', 'notas': [9,8,10], 'senha': 567},
{'nome':'Duck', 'notas': [9,8,10], 'senha': 678},
{'nome':'Henrique', 'notas': [9,8,10], 'senha': 789},
{'nome':'Samuel', 'notas': [9,8,10], 'senha': 891},
{'nome':'Lucas', 'notas': [9,8,10], 'senha': 987},
{'nome':'Claudia', 'notas': [9,8,10], 'senha': 876},
{'nome':'Caiu', 'notas': [9,8,10], 'senha': 765}]

def verificacao_aluno(alunos, nome):
#Define uma função com dois parâmetros: a lista de alunos onde procurar e o nome digitado pelo usuário.
    for aluno in alunos:
    #Percorre a lista um aluno por vez
        if aluno['nome'] == nome:
        #Compara o nome guardado no dicionário com o nome digitado.
            return aluno
            #Se os nomes forem iguais, a função devolve o dicionário inteiro do aluno
    return None
    #Esta linha está fora do for. Só é executada se o loop terminar sem encontrar ninguém.


def verificacao_senha(aluno, senha):
#Define a função com dois parâmetros: o dicionário do aluno (já encontrado antes) e a senha digitada.
    try:
        senha = int(senha)
    #O input devolve texto, mas a senha guardada é número. Então tenta converter o que foi digitado para int.
    except ValueError:
        return None
    #Se a pessoa digitou algo que não é número, a conversão gera um ValueError.
    if aluno['senha'] == senha:
        return aluno
    #Compara a senha guardada no dicionário com a digitada. Se forem iguais, devolve o dicionário do aluno, o que significa “senha correta”.
    return None
    #Se a senha não for igual, chega aqui e devolve None