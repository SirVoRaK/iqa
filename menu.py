from colors import Colors

def input_int_ranged(msg, min = 0, max = None):
    try:
        value = int(input(msg))
        if (max != None and value > max) or value < min:
            raise ValueError
        return value
    except ValueError:
        Colors.print("Valor inválido!", Colors.RED)
        return input_int_ranged(msg, min, max)
def input_int_list_ranged(msg, list):
    try:
        value = int(input(msg))
        if value not in list:
            raise ValueError
        return value
    except ValueError:
        print("Valor inválido!")
        return input_int_list_ranged(msg, list)

class Menu:
    options = [
        "Adicionar",
        "Alterar",
        "Excluir",
        "Classificar",
        "Sair"
    ]
    iqa = None
    def __init__(self, iqa):
        self.iqa = iqa

    def divisor(self):
        print(Colors.PINK+("-"*30)+Colors.RESET)

    def show(self):
        self.divisor()
        for i in range(len(self.options)):
            print(f"{Colors.GREEN}{i + 1}.{Colors.RESET} {self.options[i]}")
        print()

        selected = input_int_ranged("Selecione uma opção: ", 1, len(self.options))
        return selected

    def run(self, selected):
        self.divisor()
        print()
        index = selected - 1
        func = getattr(self.iqa, f"option_{self.options[index].lower()}")
        func()

