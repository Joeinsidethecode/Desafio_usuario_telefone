class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def plano(self):
        return self._plano

    @plano.setter
    def plano(self, plano):
        self._plano = plano

    def __str__(self):
        return f'Usuário {self._nome.upper()} criado com sucesso.'

nome = input('Nome do assinante: ')  
numero = input('Número de telefone (xx xxxxxxxxx): ')  
plano = input(f'Tipo de plano: \n[1] Essencial Fibra\n[2] Prata Fibra\n[3] Premium Fibra\nOpção: -->')
usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)
