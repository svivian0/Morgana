## IMPORTAÇÕES
import datetime as dt
##

class Morgana:
    def __init__(self):
        pass

    def hora(self):
        agora=dt.datetime.now()
        hora=agora.strftime("%H:%M")
        print(f"A hora é: {hora}")

if __name__=="__main__":
    app=Morgana()