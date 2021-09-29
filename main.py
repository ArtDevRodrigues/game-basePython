from game import *
from random import *
# elementos e seus ids
# 1-fogo
# 2-agua
# 3-terra
# 4-ar
p1 = Player("P1","Guerreiro","Masculino","Indiano")
ws1 = [
   #Weapon(id ,element     ,price          ,rarity      ,strength       ,speed), 
    Weapon( 1 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"espada"),
    Weapon( 2 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"machado"),
    Weapon( 3 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"clava"),
    Weapon( 4 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"massa"),
    Weapon( 5 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"adaga")
    ]
p2 = Player("P2","Guerreiro","Masculino","Australiano")
ws2 = [
   #Weapon(id ,element     ,price          ,rarity      ,strength       ,speed), 
    Weapon( 6 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"espada"),
    Weapon( 7 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"machado"),
    Weapon( 8 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"clava"),
    Weapon( 9 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"massa"),
    Weapon(10 ,randint(1,4),randint(10,200),randint(1,5),randint(10,100),randint(2,10),"adaga")
    ]
p1.setItensInventory(ws1)
p1.equip()
p2.setItensInventory(ws2)
p2.equip()
print(p1)
print(p2)

print("="*100)

bf = BattleField(p1,p2)

print(bf.fight())
print(bf.showPlayersStatus())

time = 0

while(not bf.end() and p1.isEquipped() and p2.isEquipped()):
    time += 1

    if time >= 60:
        print("apos uma luta epica os combatentes se cansaram e ambos cairam exaltos no chao e assim o campeao menos machucado foi escolhido")
        print(("O "+bf.champion()+" Ganhou a luta") if bf.champion() != 0 else "Deu Empate ninguem ganhou, Droga tudo isso para nada -_-")
        break

    print(bf.fight())
    print(bf.showPlayersStatus())


