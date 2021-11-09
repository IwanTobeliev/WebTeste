class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Ponto(2 , 8)
print(p.x)
print(p.y)

class Voo():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.passageiros = []

    def add_passageiro(self, nome):
        if not self.assentos():
            return False
        self.passageiros.append(nome)
        return True

    def assentos(self):
        return self.capacidade - len(self.passageiros)

voo = Voo(3)
capivara = ["cap", "capy", "capivarias", "capivarinhas"]
for i in capivara:
    if voo.add_passageiro(i):
        print(f"capivara {i} adicionada ao voo com sucesso")
    else:
        print(f"sem assentos disponíveis para {i}")
