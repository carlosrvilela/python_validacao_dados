import re

class Telefones:
    def __init__(self, telefone):
        telefone = str(telefone)
        if self.valida_telefones(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número Invalido')
    
    def __str__(self):
        return self.formata_numero()
    
    def valida_telefones(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.fullmatch(padrao,telefone)
        if resposta:
            return True
        else:
            return False
        
    def formata_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,self.numero)
        codigo_pais = resposta.group(1)
        if resposta.group(1) is None:
            codigo_pais = '55'
        numero_formatado = f'+{codigo_pais}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
        return numero_formatado