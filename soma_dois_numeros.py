class SomaDoisNumeros:
    
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    
    
    def Somar(self):
        somatorio=self.num1+self.num2
        print(f"Resultado da Soma é:{somatorio}")    
    



soma1=SomaDoisNumeros(num2=10,num1=20)
soma1.Somar()    