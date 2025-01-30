class Pessoa:
    def __init__(self, idade, nome) -> None:
        self.nome = nome
        self.idade = idade
    
    def __repr__(self) -> str:
        return f"Pessoa({self.nome}, {self.idade})"

pessoas = [
    Pessoa(15, "Joao"),
    Pessoa(25, "Jose"),
    Pessoa(22, "Maria")
]

pessoas.sort(key=lambda p: p.idade)
print(pessoas)
