class Hero:
    jumlah = 0
    def __init__(self, inputname,inputHealty, inputPower, inputArmor): 
        self.name = inputname
        self.healty= inputHealty
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat hero dengan input nama " + inputname)
hero1 = Hero('panyy', 100,12,19)
print(Hero.jumlah)
hero2 = Hero('Karina', 70,78,54)
print(Hero.jumlah)
hero3 = Hero('badang',12,14,15)
print(Hero.jumlah)