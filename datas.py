from datetime import datetime, timedelta
import locale

#locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
loc = locale.getlocale()
locale.setlocale(locale.LC_TIME, loc)

class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
         
    def __str__(self):
        return self.formata_data()
    
    def mes_cadastro(self):
        # meses_do_ano = [
        #     "janeiro", "fevereiro", "março",
        #     "abril", "maio", "junho",
        #     "julho", "agosto", "setembro",
        #     "outubro", "novembro", "dezembro"
        # ]
        #return meses_do_ano[self.momento_cadastro.month-1]
        return self.momento_cadastro.strftime('%B')
    
    def dia_semana(self):
        # dias_da_semana = [
        #     "segunda", "terça",
        #     "quarta", "quinta", "sexta",
        #     "sábado", "domingo"
        # ]
        # month_name
        # return dias_da_semana[self.momento_cadastro.weekday()]
        return self.momento_cadastro.strftime('%A')
    
    def formata_data(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M:%S')
    
    def tempo_cadastro(self):
        return datetime.today() - self.momento_cadastro