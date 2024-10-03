# https://docs.python.org/pt-br/3/tutorial/classes.html
class MinhaClasse:
    """Um exemplo de classe simples"""
    CONSTA_NUMBER = 12345

    def f(self):
        return 'olá mundo'
    
    def naoprecisaexecutarmetodoimediatamente(self):
        print("podemos colocar um métdo num objeto para executar depois")

""""
Para instanciar uma classe, usa-se a mesma sintaxe de
invocar uma função. Apenas finja que o objeto classe do
exemplo é uma função sem parâmetros, que devolve uma 
nova instância da classe. Por exemplo (presumindo a
classe acima)
"""    
# O objeto xRepresentaMinhaClasse recebe MinhaClasse
# A partir desse momento tem toda Minha classe contido nele 
# Ele representa a propria instância MinhaClasse  
xRepresentaMinhaClasse = MinhaClasse()


print(f"--------------------------------")
print(f"Por meio do Objeto xRepresentaMinhaClasse")
print(f"Irei fazer referecia ao [método f]  contido")
print(f"na Instância (classe) MinhaClasse")
print(f"--------------------------------")    
print()
print(xRepresentaMinhaClasse.f())
print()
print(f"--------------------------------")
print("Variaveies de Instância - Irei  adicionar")
print("Dentro de MinhaClasse um contador e atri-")
print("buir um valor a Ele de forma dinâmica em ")
print("Tempo de Execução, sem que ela exista ")
print("Dentro da Classe Original")
print(f"--------------------------------")
print()
xRepresentaMinhaClasse.contador=1
while xRepresentaMinhaClasse.contador < 10:
    xRepresentaMinhaClasse.contador = xRepresentaMinhaClasse.contador * 2
print(xRepresentaMinhaClasse.contador)
del xRepresentaMinhaClasse.contador
print()
print("Agora Imprimindo  uma constante Number ")
print("que existe dento de Minha Classe ")
print()
xRepresentaMinhaClasse.CONSTA_NUMBER
xRepresentaMinhaClasse.CONSTA_NUMBER=21111979
print(xRepresentaMinhaClasse.CONSTA_NUMBER)
print()
print("")

