class UrnaEletronica:
    def __init__(self):
        self.candidatos = [{"nome_candidato": "João", "partido": "A"},
                           {"nome_candidato": "Lucas", "partido": "B"},
                           {"nome_candidato": "Zé", "partido": "C"},
                           {"nome_candidato": "Nando", "partido": "D"},]


    def exibe_candidatos(self):
        for candidato in self.candidatos:
            print(f'Nome do candidato: {candidato["nome_candidato"]:<20} Partido: {candidato["partido"]:<10}')


    def adicionar_novo_candidato(self, nome_candidato, partido):
        self.candidatos.append({"nome_candidato": nome_candidato, "partido" : partido})

            
    def remove_ultimo_candidato(self):
        self.candidatos.pop()


    def atualizar_candidato(self, indice_candidato, chave, valor):
        try:
            self.candidatos[indice_candidato][chave] = valor
        except Exception as e:
            print(e)
            print(f"{indice_candidato} é um índice de candidato inválido!")


urna = UrnaEletronica()
urna.exibe_candidatos()
urna.adicionar_novo_candidato("Lú", "D")
print("====================================")
urna.exibe_candidatos()
urna.remove_ultimo_candidato()
print("====================================")
urna.exibe_candidatos()
print("====================================")
urna.atualizar_candidato(0, "nome_candidato", "João Hernesto")
urna.atualizar_candidato(0, "partido", "Honesto")
urna.exibe_candidatos()
print("====================================")
urna.atualizar_candidato(33, "partido", "Honesto")
urna.exibe_candidatos()
