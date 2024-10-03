class Roupa:
    def __init__(self,marca,tamanho,cor):
        self.marca=marca
        self.tamanho=tamanho
        self.cor=cor
    
    
    
    def Display(self):
        print("***********")
        print("Ficha Roupa")
        print("***********")
        print(f"Marca:{self.marca}")
        print(f"Tamanho:{self.tamanho}")
        print(f"Cor:{self.cor}")
        
        

roupa=Roupa(cor="Branca", tamanho="M", marca="Pena")
roupa.Display()        