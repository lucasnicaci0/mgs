class Funcionario:
    def __init__(self, nome, problemas_saude, email, telefone, alergias):
        self.nome = nome
        self.problemas_saude = problemas_saude
        self.email = email
        self.telefone = telefone
        self.alergias = alergias

    def __str__(self):
        return f"Nome: {self.nome}\nProblemas de Saúde: {self.problemas_saude}\nEmail: {self.email}\nTelefone: {self.telefone}\nAlergias: {self.alergias}\n"


class OrganizacaoFuncionarios:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Não há funcionários cadastrados.")
        else:
            print("Funcionários:")
            for funcionario in self.funcionarios:
                print(funcionario)
  

# Exemplo de utilização:

# Criando uma organização de funcionários
organizacao = OrganizacaoFuncionarios()

# Adicionando funcionários
funcionario1 = Funcionario("João Silva", "Nenhum", "joao@email.com", "(61) 9999-8888", "Pólen")
funcionario2 = Funcionario("Maria Souza", "Problemas respiratórios", "maria@email.com", "(61) 9888-7777", "Frutos do mar")
funcionario3 = Funcionario("Pedro Oliveira", "Nenhum", "pedro@email.com", "(61) 9777-6666", "Nenhuma")

organizacao.adicionar_funcionario(funcionario1)
organizacao.adicionar_funcionario(funcionario2)
organizacao.adicionar_funcionario(funcionario3)

# Listando os funcionários
organizacao.listar_funcionarios()
