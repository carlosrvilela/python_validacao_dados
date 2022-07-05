from validate_docbr import CPF as docbrCPF
class CPF:
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.CPF_valido(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido!")
        
    def __str__(self):
        return self.formata_CPF()
    
    def CPF_valido(self, cpf):
        tamanho_valido = True if len(cpf) == 11 else False
        if tamanho_valido is False:
            raise ValueError("CPF com tamanho inválido!")
        else:
            return docbrCPF().validate(cpf)
    
    def formata_CPF(self):
        # fatia_1, fatia_2, fatia_3, fatia_4 = self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11]
        # return f'{fatia_1}.{fatia_2}.{fatia_3}-{fatia_4}'
        return docbrCPF().mask(self.cpf)