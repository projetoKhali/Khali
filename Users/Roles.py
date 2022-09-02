
# Representa uma Função,
class Role:
    name:str = ""
    permissions = None
    def __init__(self, n, p):
        self.name = n
        self.permissions = p
