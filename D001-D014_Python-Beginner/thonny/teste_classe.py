### Classe Pessoa
Pessoa = {}
# construtor, corresponde ao __new__ de Python
def newPessoa(nome, nascimento):
    new = {} # a nova instância
    new['nome'] = nome
    new['nascimento'] = nascimento
    return new

Pessoa['new'] = newPessoa
### Fim da definição de classe

# Ou seja, agora se queremos criar uma nova instância, fazemos:
hank = Pessoa['new']('Hank Moody', (8, 11, 2007))

# Tudo como esperado, temos os dados no dicionário
hank['nome']
hank['nascimento']