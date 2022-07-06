from validate_docbr import CPF as docbrCPF, CNPJ as docbrCNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError('Quantidade de dígitos incorreta!')
        
class DocCPF:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")
    
    def __str__(self):
        return self.formata()
    
    def valida(self, documento):
        return docbrCPF().validate(documento)
    
    def formata(self):
        return docbrCPF().mask(self.cpf)
    
class DocCNPJ:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")
    
    def __str__(self):
        return self.formata()
    
    def valida(self, documento):
        return docbrCNPJ().validate(documento)
    
    def formata(self):
        return docbrCNPJ().mask(self.cnpj)