import datetime as dt


class PlayList:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @id.setter
    def id(self, id):
        if id <= 0:
            raise ValueError("Id deve ser maior que zero!")
        self.__id = id

    @nome.setter
    def nome(self, nome):
        if nome == "":
            raise ValueError("Nome é obrigatório!")
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    def tempo_total(self):
        ids_das_musicas = [playlist_item.id_musica for playlist_item in UI.playlist_itens if playlist_item.id_playlist == self.id]
        duracoes_musicas = [musica.duracao for musica in UI.musicas if musica.id in ids_das_musicas]
        duracao_total = dt.timedelta(0)
        for duracao in duracoes_musicas:
            duracao_total = duracao_total + duracao
        return duracao_total

    def __str__(self):
        return f"{self.nome}({self.id}): {self.descricao}"


class Musica:
    def __init__(self, id, titulo, artista, album, duracao):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def album(self):
        return self.__album

    @property
    def duracao(self):
        return self.__duracao

    @id.setter
    def id(self, id):
        if id <= 0:
            raise ValueError("Id deve ser maior que 0!")
        self.__id = id

    @titulo.setter
    def titulo(self, titulo):
        if titulo == "":
            raise ValueError("Título é obrigatório!")
        self.__titulo = titulo

    @artista.setter
    def artista(self, artista):
        if artista == "":
            raise ValueError("Artista é obrigatório!")
        self.__artista = artista

    @album.setter
    def album(self, album):
        if album == "":
            raise ValueError("Album é obrigatório!")
        self.__album = album

    @duracao.setter
    def duracao(self, duracao):
        if dt.timedelta(0) >= duracao:
            raise ValueError("Duração deve ser maior que 0!")
        self.__duracao = duracao

    def __str__(self):
        return f"id: {self.id}; titulo: {self.titulo}; artista: {self.artista}; album: {self.album}; duração: {self.duracao}"


class PlayListItem:
    def __init__(self, id, id_playlist, id_musica, data_inclusao, sequencia):
        self.id = id
        self.id_playlist = id_playlist
        self.id_musica = id_musica
        self.data_inclusao = data_inclusao
        self.sequencia = sequencia

    @property
    def id(self):
        return self.__id

    @property
    def id_playlist(self):
        return self.__id_playlist

    @property
    def id_musica(self):
        return self.__id_musica

    @property
    def data_inclusao(self):
        return self.__data_inclusao

    @property
    def sequencia(self):
        return self.__sequencia

    @id.setter
    def id(self, id):
        if id <= 0:
            raise ValueError("Id deve ser maior que 0!")
        self.__id = id

    @id_playlist.setter
    def id_playlist(self, id_playlist):
        if id_playlist <= 0:
            raise ValueError("Id da playlist deve ser maior que 0!")
        self.__id_playlist = id_playlist

    @id_musica.setter
    def id_musica(self, id_musica):
        if id_musica <= 0:
            raise ValueError("Id da música deve ser maior que 0!")
        self.__id_musica = id_musica

    @data_inclusao.setter
    def data_inclusao(self, data_inclusao):
        self.__data_inclusao = data_inclusao

    @sequencia.setter
    def sequencia(self, sequencia):
        if sequencia <= 0:
            raise ValueError("Sequência deve ser maior que 0!")
        self.__sequencia = sequencia

    def __str__(self):
        data = self.data_inclusao.strftime("%d/%m/%Y")
        return f"id: {self.id}; id_playlist: {self.id_playlist}; id_musica: {self.id_musica}; data_inclusao: {data}; sequencia: {self.sequencia}."


class UI:
    playlists = []
    musicas = []
    playlist_itens = []
    id_playlist = 0
    id_musica = 0
    id_playlist_item = 0

    @classmethod
    def main(cls):
        while True:
            opcao_selecionada = cls.menu()
            if opcao_selecionada == 1:
                cls.inserir_playlist()
            if opcao_selecionada == 2:
                cls.inserir_musica()
            if opcao_selecionada == 3:
                cls.inserir_musica_em_playlist()
            if opcao_selecionada == 4:
                cls.listar_playlists()
            if opcao_selecionada == 5:
                cls.listar_musicas()
            if opcao_selecionada == 6:
                cls.mostrar_playlist()
            if opcao_selecionada == 7:
                cls.mostrar_musica()
            if opcao_selecionada == 8:
                cls.atualizar_playlist()
            if opcao_selecionada == 9:
                cls.atualizar_musica()
            if opcao_selecionada == 10:
                cls.excluir_playlist()
            if opcao_selecionada == 11:
                cls.excluir_musica()
            if opcao_selecionada == 12:
                cls.remover_música_de_playlist()
            if opcao_selecionada == 13:
                break
            input("Aperte enter para voltar ao menu.")


    @staticmethod
    def menu():
        print("MENU PRINCIPAL")
        print("1 - Inserir uma nova playlist")
        print("2 - Inserir uma nova música")
        print("3 - Inserir uma música em uma playlist")
        print("4 - Listar todas as playlists")
        print("5 - Listar todas as músicas")
        print("6 - Mostrar uma playlist")
        print("7 - Mostrar uma música")
        print("8 - Atualizar dados de uma playlist")
        print("9 - Atualizar dados de uma música")
        print("10 - Excluir uma playlist")
        print("11 - Excluir uma música")
        print("12 - Remover uma música de uma playlist")
        print("13 - Sair")
        return int(input())

    @classmethod
    def inserir_playlist(cls):
        cls.id_playlist += 1
        id = cls.id_playlist

        print("MENU INSERIR PLAYLIST")

        nome = input("Digite o nome da playlist: ")
        descricao = input("Digite uma descrição (Opcional): ")

        playlist = PlayList(id, nome, descricao)
        cls.playlists.append(playlist)

        print("Playlist adicionada!")

    @classmethod
    def inserir_musica(cls):
        cls.id_musica += 1
        id = cls.id_musica

        print("MENU INSERIR MÚSICA")

        titulo = input("Digite o título da música: ")
        artista = input("Digite o nome do artista: ")
        album = input("Digite o nome do álbum: ")
        duracao = input("Digite o tempo da música (mm:ss): ")

        m, s = map(int, duracao.split(":"))
        duracao_dt = dt.timedelta(minutes=m, seconds=s)

        musica = Musica(id, titulo, artista, album, duracao_dt)
        cls.musicas.append(musica)

        print("Música adicionada!")

    @classmethod
    def inserir_musica_em_playlist(cls):
        cls.id_playlist_item += 1
        id = cls.id_playlist_item

        print("INSERIR MÚSICA EM PLAYLIST")

        id_playlist = int(input("Digite o id da playlist: "))
        id_musica = int(input("Digite o id da música: "))
        data_inclusao = dt.datetime.now()

        itens_da_playlist = [item for item in cls.playlist_itens if item.id_playlist == id_playlist]
        sequencia = len(itens_da_playlist) + 1

        playlist_item = PlayListItem(id, id_playlist, id_musica, data_inclusao, sequencia)
        cls.playlist_itens.append(playlist_item)

        print("Música inserida na playlist selecionada!")

    @classmethod
    def listar_playlists(cls):
        print("LISTA DE PLAYLISTS")
        for playlist in cls.playlists:
            print(f"{playlist.id} - {playlist.nome}")

    @classmethod
    def listar_musicas(cls):
        print("LISTA DE MÚSICAS")
        for musica in cls.musicas:
            print(musica)

    @classmethod
    def mostrar_playlist(cls):
        print("MOSTRAR PLAYLIST")

        id = int(input("Digite o id da playlist: "))
        playlists_com_id = [playlist for playlist in cls.playlists if playlist.id == id]

        if len(playlists_com_id) == 0:
            print("Playlist não encontrada!")
            return

        playlist = playlists_com_id[0]

        print(playlist)
        print(f"Tempo total: {playlist.tempo_total()}")

        ids_das_musicas = [item.id_musica for item in cls.playlist_itens if item.id_playlist == id]

        if len(ids_das_musicas) != 0:
            musicas_da_playlist = [musica for musica in cls.musicas if musica.id in ids_das_musicas]
            print("Músicas: ")
            for musica in musicas_da_playlist:
                print(musica)

    @classmethod
    def mostrar_musica(cls):
        print("MOSTRAR MÚSICA")

        id = int(input("Digite o id da música: "))

        musicas_com_id = [musica for musica in cls.musicas if musica.id == id]

        if len(musicas_com_id) == 0:
            print("Música não encontrada!")
            return

        musica = musicas_com_id[0]

        print(f"id: {musica.id}")
        print(f"título: {musica.titulo}")
        print(f"artista: {musica.artista}")
        print(f"álbum: {musica.album}")
        print(f"duração: {musica.duracao}")

    @classmethod
    def atualizar_playlist(cls):
        print("ATUALIZAR PLAYLIST")

        id = int(input("Digite o id da playlist: "))

        playlists_com_id = [playlist for playlist in cls.playlists if playlist.id == id]

        if len(playlists_com_id) == 0:
            print("Playlist não encontrada!")
            return

        playlist = playlists_com_id[0]

        playlist.nome = input("Digite o nome da playlist: ")
        playlist.descricao = input("Digite a descrição da playlist (opcional): ")

        print("Playlist atualizada!")

    @classmethod
    def atualizar_musica(cls):
        print("ATUALIZAR MÚSICA")

        id = int(input("Digite o id da playlist: "))

        musicas_com_id = [musica for musica in cls.musicas if musica.id == id]

        if len(musicas_com_id) == 0:
            print("Música não encontrada!")
            return

        musica = musicas_com_id[0]

        musica.titulo = input("Digite o título da música: ")
        musica.artista = input("Digite o artista da música: ")
        musica.album = input("Digite o álbum da música: ")
        duracao = input("Digite o tempo da música (mm:ss): ")
        
        m, s = map(int, duracao.split(":"))
        musica.duracao = dt.timedelta(minutes=m, seconds=s)

        print("Música atualizada!")

    @classmethod
    def excluir_playlist(cls):
        print("EXCLUIR PLAYLIST")

        id = int(input("Digite o id da playlist: "))

        tamanho_antes = len(cls.playlists)
        cls.playlists = [playlist for playlist in cls.playlists if playlist.id != id]
        tamanho_depois = len(cls.playlists)

        if tamanho_antes == tamanho_depois:
            print("Playlist não encontrada!")
            return
        print("Playlist excluída")

    @classmethod
    def excluir_musica(cls):
        print("EXCLUIR MÚSICA")

        id = int(input("Digite o id da música: "))

        tamanho_antes = len(cls.musicas)
        cls.musicas = [musica for musica in cls.musicas if musica.id != id]
        tamanho_depois = len(cls.musicas)

        if tamanho_antes == tamanho_depois:
            print("Música não encontrada!")
            return
        print("Música excluída")

    @classmethod
    def remover_música_de_playlist(cls):
        print("REMOVER MÚSICA DE PLAYLIST")

        id_playlist = int(input("Digite o id da playlist: "))
        id_musica = int(input("Digite o id da música: "))

        tamanho_antes = len(cls.playlist_itens)
        cls.playlist_itens = [playlist_item for playlist_item in cls.playlist_itens if not(playlist_item.id_playlist == id_playlist and playlist_item.id_musica == id_musica)]
        tamanho_depois = len(cls.playlist_itens)

        if tamanho_antes == tamanho_depois:
            print("Relaçao playlist/música não encontrada!")
            return
        print("Música removida da playlist")


UI.main()