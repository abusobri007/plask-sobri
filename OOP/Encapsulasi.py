class Hero:
      def __init__(self,name,healty,attcakPower):
            self.__name = name
            self.__healty = healty
            self.__attackPower = attcakPower
      #getter
      def getName(self):
            return self.__name
      def gethealty(self):
            return self.__healty
      #setter
      def diserang(self,serangPower):
            self.__healty -= serangPower
      def setattack(self,nilaibaru):
            self.__attackPower = nilaibaru
#awal dari sebuah game
hanabi = Hero("hanabi",60,6)
#game berjalan
print(hanabi.getName)
print(hanabi.gethealty)
hanabi.diserang(10)
print(hanabi.gethealty())