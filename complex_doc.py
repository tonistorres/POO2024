# https://docs.python.org/pt-br/3/tutorial/classes.html
class Complex:
    
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


    def PrintInfo(self):
        print(f"Imagpart:{self.i}")
        print(f"Realpart:{self.r}")

x=Complex(imagpart=3.0, realpart=-4.5)
x.PrintInfo()