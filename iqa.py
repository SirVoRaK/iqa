from bd import get_all_amostras, get_all_columns_avarage, save_amostra, update_amostra, delete_amostra
from menu import Menu, input_int_list_ranged

def ask(msg):
    answer = input(f"{msg} (s/n): ").lower()
    if answer == "s" or answer == "n":
        return answer == "s"
    print("Resposta inválida!\n")
    return ask(msg)

description = [
    "Nenhuma restrição.",
    "Pessoas de grupos sensiveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.",
    "Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensiveis (crianças, idosos e pessoas com doengas respiratórias e cardiacas) podem apresentar efeitos mais sérios na saúde.",
    "Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saude de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardiacas).",
    "Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensiveis."
]
class Iqa:
    poluentes = []
    exit = False
    def __init__(self, poluentes):
        self.poluentes = poluentes

    def start(self):
        if self.exit:
            return self.exit

        menu = Menu(self)
        selected = menu.show()
        print()
        menu.run(selected)
        return self.exit

    def reset(self):
        for poluente in self.poluentes:
            poluente.reset()

    def print_result(self):
        worst_poluente = self.__get_worst_poluente()
        description = self.__get_description(worst_poluente.limite)
        quality = worst_poluente.quality
        iqa = worst_poluente.iqa

        print()
        print(f"Classificação: {quality}.")
        print(f"Iqa: {iqa}.")
        print(f"Efeito: {description}")

    def __get_description(self, limite):
        return description[limite]

    def __get_worst_poluente(self):
        worst_poluente = self.poluentes[0]
        for poluente in self.poluentes:
            if poluente.iqa > worst_poluente.iqa:
                worst_poluente = poluente
        return worst_poluente

    def dict_to_string(self, dict):
        return ", ".join([f"{key}: {value}" for key, value in dict.items() if key != "id"])

    def list_amostras(self):
        result = get_all_amostras()
        ids = []
        for row in result:
            row_text = self.dict_to_string(row)
            ids.append(row["id"])
            print(f"{row['id']} - {row_text}")
        return ids

    def input_poluentes(self):
        poluentes = {}
        for poluente in self.poluentes:
            poluentes[poluente.name.lower()] = poluente.input_concentracao()
        return poluentes

    def option_adicionar(self):
        print("Adicionar amostra")
        poluentes = self.input_poluentes()
        save_amostra(poluentes)
        print("Amostra adicionada com sucesso!")

    def option_alterar(self):
        print("Alterar amostra")
        ids = self.list_amostras()
        selected_id = input_int_list_ranged("\nDigite o id da amostra que deseja alterar: ", ids)
        poluentes = self.input_poluentes()
        update_amostra(selected_id, poluentes)
        print("Amostra alterada com sucesso!")

    def option_excluir(self):
        print("Excluir amostra")
        ids = self.list_amostras()
        selected_id = input_int_list_ranged("\nDigite o id da amostra que deseja excluir: ", ids)
        if not ask(f"Tem certeza que deseja excluir a amostra {selected_id}?"):
            print("Operação cancelada!")
            return
        delete_amostra(selected_id)
        print("Amostra excluída com sucesso!")

    def option_classificar(self):
        print("Classificar amostras")
        result = get_all_amostras()
        if len(result) == 0:
            print("Não há amostras cadastradas!")
            return

        avg = get_all_columns_avarage(result)
        print("\nMédia dos poluentes:")
        print(self.dict_to_string(avg))
        for poluente in self.poluentes:
            poluente.calculate_iqa(avg[poluente.name.lower()])
        self.print_result()

    def option_sair(self):
        self.exit = True
