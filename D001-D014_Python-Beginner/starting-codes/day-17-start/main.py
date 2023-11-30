class Usuario:

    # função especial do python (__init__) que pode ou não ter parâmetros(nesse caso: num, nome) e, caso tenha, recebe
    # os argumentos na criação dos objetos.
    def __init__(self, num, nome):
        self.num_id = num  # criando o atributo ".num_id" a partir do parâmetro num
        self.nome = nome  # criando o atributo ".nome" a partir do parâmetro nome
        self.num_seguidores = 0  # atributo que não depende de parâmetros do construtor
        self.num_seguindo = 0

    # criação de um método que simula uma situação em que uma pessoa segue outra pessoa
    def seguir(self, usuario_a_seguir):
        """Recebe como argumento o usuario que se deseja seguir"""
        # aumenta o atributo de número de seguidores em +1 do objeto que se deseja seguir.
        usuario_a_seguir.num_seguidores += 1
        # aumenta o atributo de número de pessoas que o próprio objeto segue em +1.
        self.num_seguindo += 1


# quando a Classe possui um construtor com parâmetros, esses devem ser passados logo durante a criação do objeto.
usuario_1 = Usuario("001", "Arthur")
usuario_2 = Usuario("002", "Carlos")

print(usuario_1.nome, usuario_2.nome)

usuario_1.seguir(usuario_2)
print(usuario_1.num_seguindo)
print(usuario_1.num_seguidores)
print(usuario_2.num_seguindo)
print(usuario_2.num_seguidores)
