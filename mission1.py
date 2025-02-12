# Missão 1: Restaurando as Regras Escolares 📝 
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

def verificando_aprovacao():
    nota_aluno = float(input("Digite a nota do aluno: "))

    if nota_aluno >= 6:
        print("Aluno aprovado! :) ")
    else:
        print("Aluno reprovado. :( ")

verificando_aprovacao()