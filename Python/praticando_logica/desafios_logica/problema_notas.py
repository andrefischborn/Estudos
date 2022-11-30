'''
Problema "notas"
Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
mensagem "REPROVADO", conforme exemplos.
    Exemplo 1:
        Digite a primeira nota: 45.5
        Digite a segunda nota: 31.3
        NOTA FINAL = 76.8
    Exemplo 2:
       Digite a primeira nota: 34.0
        Digite a segunda nota: 23.5
        NOTA FINAL = 57.5
        REPROVADO
'''
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
media_final = (nota1 + nota2)

def media():
    if media_final >= 60.0:
        print(f'NOTA FINAL %.2f' % (media_final))   
        print('APROVADO!')
    else:
        print(f'NOTA FINAL %.2f' % (media_final))
        print('REPROVADO!')


media()