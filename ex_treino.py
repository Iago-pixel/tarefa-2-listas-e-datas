import datetime as dt

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.id = id
        self.data = data
        self.distancia = distancia
        self.tempo = tempo

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def distancia(self):
        return self.__distancia

    @property
    def tempo(self):
        return self.__tempo

    @id.setter
    def id(self, id):
        if id <= 0:
            raise ValueError("Id deve ser maior que zero!")
        self.__id = id

    @data.setter
    def data(self, data):
        self.__data = data

    @distancia.setter
    def distancia(self, distancia):
        if distancia <= 0:
            raise ValueError("Distancia deve ser maior que zero!")
        self.__distancia = distancia

    @tempo.setter
    def tempo(self, tempo):
        if tempo <= dt.timedelta(0):
            raise ValueError("Tempo deve ser maior que 0!")
        self.__tempo = tempo

    def pace(self):
        pace_segundos = self.tempo.total_seconds() / self.distancia
        return dt.timedelta(seconds=pace_segundos)

    def __str__(self):
        return f"Treino {self.id} do dia {self.data.strftime('%d/%m/%Y')} percorreu {self.distancia} km em {self.tempo}"


class TreinoUI:
    treinos = []
    id = 0

    @classmethod
    def main(cls):
        while True:
            opcao_selecionada = cls.menu()
            if opcao_selecionada == 1:
                cls.inserir()
                print("Treino adicionado!")
            if opcao_selecionada == 2:
                cls.listar()
            if opcao_selecionada == 3:
                cls.listar_id()
            if opcao_selecionada == 4:
                cls.atualizar()
            if opcao_selecionada == 5:
                cls.excluir()
            if opcao_selecionada == 6:
                cls.mais_rapido()
            if opcao_selecionada == 7:
                break
            input("Aperte enter para voltar ao menu.")


    @staticmethod
    def menu():
        print("MENU PRINCIPAL")
        print("1 - Inserir um novo treino")
        print("2 - Listar todos os treinos")
        print("3 - Mostrar um treino")
        print("4 - Atualizar os dados de um treino")
        print("5 - Excluir um treino")
        print("6 - Encontrar o treino mais rápido (maior velocidade)")
        print("7 - Sair")
        return int(input())

    @classmethod
    def inserir(cls):
        cls.id += 1
        id = cls.id

        print("MENU INSERIR TREINO")

        data = input("Digite a data (dd/mm/aaaa): ")
        data_dt = dt.datetime.strptime(data, "%d/%m/%Y")

        distancia = float(input("Digite a distancia em km: "))

        tempo = input("Digite o tempo (hh:mm:ss): ")
        h, m, s = map(int, tempo.split(":"))
        tempo_dt = dt.timedelta(hours=h, minutes=m, seconds=s)

        treino = Treino(id, data_dt, distancia, tempo_dt)

        cls.treinos.append(treino)

    @classmethod
    def listar(cls):
        if len(cls.treinos) == 0:
            print("Não há treinos!")
            return
        print("LISTA DE TREINOS")
        for treino in cls.treinos:
            print(treino)

    @classmethod
    def listar_id(cls):
        print("MOSTRAR TREINO")
        id = int(input("Digite o id: "))
        treinos_com_id = [treino for treino in cls.treinos if treino.id == id]
        if len(treinos_com_id) == 0:
            print("Id não encontrado!")
            return
        treino = treinos_com_id[0]
        print(f"id: {treino.id}")
        print(f"data: {treino.data.strftime('%d/%m/%Y')}")
        print(f"distancia: {treino.distancia} km")
        print(f"tempo: {treino.tempo}")

    @classmethod
    def atualizar(cls):
        print("ATUALIZAR TREINO")

        id = int(input("Digite o id: "))

        treinos_com_id = [treino for treino in cls.treinos if treino.id == id]

        if len(treinos_com_id) == 0:
            print("Id não encontrado!")
            return

        treino = treinos_com_id[0]

        data = input("Digite a data (dd/mm/aaaa): ")
        treino.data = dt.datetime.strptime(data, "%d/%m/%Y")
        
        treino.distancia = float(input("Digite a distancia em km: "))

        tempo = input("Digite o tempo (hh:mm:ss): ")
        h, m, s = map(int, tempo.split(":"))
        treino.tempo = dt.timedelta(hours=h, minutes=m, seconds=s)

        print("Treino atualizado!")

    @classmethod
    def excluir(cls):
        print("EXCLUIR TREINO")
        id = int(input("Digite o id: "))
        tamanho_anterior = len(cls.treinos)
        cls.treinos = [treino for treino in cls.treinos if treino.id != id]
        tamanho_novo = len(cls.treinos)
        if tamanho_anterior == tamanho_novo:
            print("Id não encontrado!")
        else:
            print(f"Treino {id} excluido!")

    @classmethod
    def mais_rapido(cls):
        if len(cls.treinos) == 0:
            print("Não há treinos cadastrados!")
            return
        treino_mais_rapido = cls.treinos[0]
        for treino in cls.treinos:
            if treino_mais_rapido.pace() > treino.pace():
                treino_mais_rapido = treino
        print("TREINO MAIS RÁPIDO")
        print(f"id: {treino_mais_rapido.id}")
        print(f"data: {treino_mais_rapido.data.strftime('%d/%m/%Y')}")
        print(f"distancia: {treino_mais_rapido.distancia} km")
        print(f"tempo: {treino_mais_rapido.tempo}")


TreinoUI.main()