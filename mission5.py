# Missão 5: Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.

# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

def verificando_senha():
    senha_correta = "Python123"
    digitando_senha = input("Digite a senha de acesso ao cofre: ")

    if digitando_senha == senha_correta:
        print("Acesso permitido!")
    else:
        print("Senha incorreta. Tente novamente.")

verificando_senha()