class Buid():
      name = None
      room =[]

      def create_room (self,room):
            self.room.append(room)

      def remove_roam(self,room):
            self.room.append(room)

      def List_room(self):
            print(f"Ruangan dalam bangunan {self.name} : {self.room}")



class Room():
      name = None
      color = None

      def __repr__(self):
          return self.name


itec = Buid()
itec.name = "ITEC"
itec.List_room()

r1 = Room()
r1.name = "instagram"
r1.color = "pink"

