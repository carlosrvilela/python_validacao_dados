from documento import*
from telefones import*
from datas import*
from acessa_cep import*

# cpf = 12345678912
# cpf_valido = 15316264754
# obj_cpf = Documento.cria_documento(cpf_valido)
# print(f'CPF: {obj_cpf}')

# cnpj_valido = 62251796000102
# obj_cnpj = Documento.cria_documento(cnpj_valido)
# print(f'CNPJ: {obj_cnpj}')

# telefone = 12312345678912

# obj_telefone = Telefones(telefone)
# print(obj_telefone)

# cadastro = Datas()
# print(cadastro, cadastro.mes_cadastro(), cadastro.dia_semana())
# print(cadastro.tempo_cadastro())

cep = 74005010
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

print(objeto_cep.acessa_via_cep())