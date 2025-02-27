"""
trénink 17 (classes, instances):
vytvoř továrnu na výrobu robotů = class Robot:
* robot bude mít atributy "name" a "battery" (cokoliv v rozsahu 0-100 jednotek)
* robot bude mít metodu "info", která vypíše jeho "name" a "battery" a "reach"
* robot bude mít metodu "move", která bere jako parametr číslo (km), jedna jednotka baterie vystačí na 2 km pohybu,
* pokud bude požadovaný pohyb mimo možnosti baterie, pohyb nebude umožněn (např. vytiskne "Nelze provést")
* vytvoř dvě instance této třídy


* vytvoř dvě instance této třídy






* vytvoř metodu pro získání energie (z baterie) z jiné instance třídy "Robot"
  metoda bude brát jako parametr jiný objekt a množství energie, která být z baterie získána
  o získání (a ztrátě) energie budeme informováni hlášením - s přesným množstvím získané/ztracené energie

"""


class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        
    def info(self):
        print(f"jmeno: {self.name}, baterka: {self.battery} kg, reach: {self.battery*2} cm")
    def move(self, distance):
        if self.battery < distance / 2:
            print("nedostatek baterky")
        else:
            self.battery -= distance / 2
            print(f"robot {self.name} ušel {distance} km!!!")
    def vysavac(self, enemy, kolik):
        if enemy.battery < kolik:
            kolik = enemy.battery
            enemy.battery -= kolik
            self.battery += kolik
            
    

reggin = Robot("reggin", 50)
cernousek = Robot("cernousek", 30)
reggin.info()
reggin.move(20)
reggin.info()
reggin.vysavac(cernousek)
        