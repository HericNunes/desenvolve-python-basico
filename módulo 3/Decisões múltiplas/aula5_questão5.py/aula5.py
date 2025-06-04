usuarios = {
    "admin": ("admin123", "Administrador"),
    "usuario1": ("senha123", "Usuário Comum"),
    "visitante1": ("guest2024", "Visitante")
}
while True:
    print("\n--- Sistema de Autenticação ---")
    login = input("Digite o nome de usuário (ou 'sair' para encerrar): ")

    if login.lower() == "sair":
        print("Encerrando o programa...")
        break

    senha = input("Digite a senha: ")
    if login in usuarios:
        senha_correta, nivel_acesso = usuarios[login]
        if senha == senha_correta:
            print(f"Login bem-sucedido! Nível de acesso: {nivel_acesso}")
        else:
            print("Erro: Usuário ou senha inválidos.")
    else:
        print("Erro: Usuário ou senha inválidos.")
