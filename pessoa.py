class Pessoa:
    
    def __init__(self,nome,idade,sexo,pais):
        self.nome=nome
        self.idade=idade
        self.sexo=sexo
        self.pais=pais
        
        
    def display(self):
        print("**************")
        print("FICHA PESSOA") 
        print("**************")
        print(f"Pessoa:{str(self.nome)} Idade:{str(self.idade)}")
        print(f"Sexo:{str(self.sexo)}País:{str(self.pais)}")
        print("**************")


pessoa1=Pessoa(nome="João Silva ",pais=" Brasil",sexo="Masculino ",idade=31) 
pessoa1.display()          