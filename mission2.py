# Missão 2: O Sistema Eleitoral Secreto 📝 
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

def aluno_votante():
    idade_usuario = int(input("Qual a sua idade em anos? "))

    if idade_usuario >= 16:
        print("Vote consciente!")
    else:
        print("Que pena! É necessário ter 16 anos para votar.")

aluno_votante()