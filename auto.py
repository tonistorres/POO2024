class Auto:
    
    #construtor 
    def __init__(self,marca,modelo,placa):
        self.marca=marca
        self.modelo=modelo
        self.placa=placa
    
    
    # criando um método que imprime Ficha do Carro com Marca, Modelo e Placa
    def display(self):
        print("*************")
        print("FICHA CARRO")
        print("*************")
        print("Marca é:"+str(self.marca)) 
        print("Marca é:"+str(self.modelo))
        print("Marca é:"+str(self.placa))     
        print("*************")
        
        
#Criando um objeto do tipo Auto e passando para o construtor desse objeto 
#A marca o Modelo e a placa do carro         
carro1=Auto(marca="Fiat",modelo="Palio",placa="PO11245")

#Objeto criado agora instanciando o método que imprime a ficha do carro 
carro1.display()
        