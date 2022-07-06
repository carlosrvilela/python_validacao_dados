from documento import*

cpf = 12345678912
cpf_valido = 15316264754
obj_cpf = Documento.cria_documento(cpf_valido)
print(f'CPF: {obj_cpf}')

cnpj_valido = 62251796000102
obj_cnpj = Documento.cria_documento(cnpj_valido)
print(f'CNPJ: {obj_cnpj}')