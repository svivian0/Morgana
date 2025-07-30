## IMPORTAÇÕES
import datetime as dt
##

class Morgana:
    def __init__(self):
        pass

    def catarDataHora(self):
        self.datahora=dt.datetime.now()

    def hora(self):
        hora=self.datahora.strftime("%H:%M")
        print(f"A hora é: {hora}")
    
    def diaSemana(self):
        diasemana=self.datahora.strftime("%A")
        print(f"Hoje é: {diasemana}")

    def DiaMesAno(self):
        dia=self.datahora.strftime("%d")
        mes=self.datahora.strftime("%m")
        ano=self.datahora.strftime("%Y")
        print(f"Hoje é dia: {dia}, do mês: {mes}, do ano: {ano}")
if __name__=="__main__":
    app=Morgana()
    app.catarDataHora()
