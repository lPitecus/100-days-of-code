from turtle import Turtle, Screen

# Na variável tortuguita, atribui-se a ela uma Class chamada Turtle()
# Uma Class é um modelo que junta variáveis e funções específicas desse modelo.
# Objetos podem ser criados a partir desse modelo

# atribuindo a classe a uma variável = criando um objeto
tortuguita = Turtle()

# mudando a uma das características do objeto com um método() (method)
tortuguita.shape("turtle")

# criando outro objeto a partir de outra classe
minha_tela = Screen()


print(minha_tela.canvheight)
print(minha_tela.canvwidth)
minha_tela.exitonclick()

# Importando a classe "PrettyTable" da biblioteca "prettytable"
from prettytable import PrettyTable

# Criando um objeto a partir a Classe
table = PrettyTable()


# Usando uma função dentro da Classe (método) para adicionar uma coluna
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# Usando um método para adicionar mais uma coluna
table.add_column("Type", ["Electric", "Water", "Fire"])

# Mudando uma propriedade (property) do objeto atribuindo ela a outro valor.
# Esses valores que podem ser atribuídos estão na documentação da biblioteca.
table.align = "c"
# Mudando a propriedade do cabeçalho para deixar todas as letras maiúsculas.
table.header_style = "upper"
print(table)
