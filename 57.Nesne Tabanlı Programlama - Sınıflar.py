class araba():
    model = "Renault"
    renk = "Gümüş"
    beygirGücü = 110
    silindir = 4

araba1 = araba()
araba2 = araba()
print(araba1.model)
print(araba2.model)

class araba():
    def __init__(self,model,renk,beygirGücü,silindir):
        self.model = model
        self.renk = renk
        self.beygirGücü = beygirGücü
        self.silindir = silindir

araba1 = araba("Renault","Gümüş",110,4)
araba2 = araba("Peugeot","Beyaz",90,4)
print(araba1.model)
print(araba2.model)
