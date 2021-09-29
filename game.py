from random import *

class Item:
    def __init__(self,id=None,price=None,rarity=None,strength=None,speed=None):
        self.id = id
        self.price = price
        self.rarity = rarity
        self.strength = strength
        self.speed = speed

class Weapon(Item):

    def __init__(self,id=None,element=None,price=None,rarity=None,strength=None,speed=None,_type=None):
        Item.__init__(self,id=id,price=price,rarity=rarity,strength=strength,speed=speed)
        self._type = _type
        self.element = element

    def __str__(self):
        return f"Id: {self.id}, Tipo da arma: {self._type}, elemento: {self.element}, preco: {self.price}, raridade: {self.rarity}, Forca: {self.strength}, Velocidade: {self.speed}"

    def __repr__(self):
     return str(self.__dict__)

    def damage(self):
        return self.strength
    
    def getElement(self):
        return self.element
    
    def getElementName(self):
        #Elementos e seus ids
        # 1-fogo
        # 2-agua
        # 3-terra
        # 4-ar
        elementName = None
        if self.element == 1:
            elementName = "Fogo"
        elif self.element == 2:
            elementName = "Agua"
        elif self.element == 3:
            elementName = "Terra"
        elif self.element == 4:
            elementName = "Ar"
        else:
            elementName = self.element
        
        return elementName

class Player: 
    def __init__(self,name=None,description=None,genre=None,race=None):
        self.name = name
        self.description = description
        self.genre = genre
        self.race = race
        self.muscle = 1
        self.intelligence = 25
        self.speed = 25
        self.charm = 1
        self.life = 100
        self.magic = 1
        self.inventory = []
        self.weaponEquipped = None
        self.isEscape = False

    def __str__(self):
       
        return f"""
Nome: {self.name}\nDescricao: {self.description}\nGenero: {self.genre}\nRaca:{self.race}\nMuscle: {self.muscle}
Inteligencia: {self.intelligence}\nVelocidade: {self.speed}\nCharme: {self.charm}\nVida: {self.life if self.life >= 0 else 0}\nMagica: {self.magic}
Inventario: {self.inventory}
""" 

    def setItensInventory(self,itens):
        if type(itens) == list:
            for i in itens:
                self.inventory.append(i)

        else:
            self.inventory.extend(itens)

    def equip(self):
        if len(self.inventory) == 0:
            print("Sem Itens, Corre !!")
            return None
        else:
            self.weaponEquipped = choice(self.inventory)

    def isEquipped(self):
        if self.weaponEquipped == None:
            return False
        else:
            return True

    def damageCaused(self):
        damage = self.muscle + (self.weaponEquipped.damage() if self.weaponEquipped.getElement() != None else 0 )
        self.muscle += 1
        return damage,(self.weaponEquipped.getElement() if self.weaponEquipped.getElement() != None else 0 )

    def chanceEscape(self):
        chace = self.speed + self.intelligence
        l = choice(list(((True for x in range((chace if chace <= 100 else 100))))) + list((False for x in range(100 - (chace if chace <= 100 else 100)))))
        
        if l == True:
            self.intelligence += 1
            self.speed += 1

        self.isEscape = l
        

    def balenceWeapons(self,damage,element):
        #Elementos e seus ids
        # 1-fogo
        # 2-agua
        # 3-terra
        # 4-ar
      
        damageFinal = 0

        if self.weaponEquipped.getElement() == element:
                damageFinal += damage
        
        elif element == 1 and self.weaponEquipped.getElement() == 2:
                damageFinal += damage/5 

        elif element == 1 and self.weaponEquipped.getElement() == 3:
                damageFinal += damage/7 

        elif element == 1 and self.weaponEquipped.getElement() == 4:
                damageFinal += damage/2
        
        elif element == 2 and self.weaponEquipped.getElement() == 1:
                damageFinal += damage + 10

        elif element == 2 and self.weaponEquipped.getElement() == 3:
                damageFinal += damage + 2

        elif element == 2 and self.weaponEquipped.getElement() == 4:
                damageFinal += damage/4
        
        elif element == 3 and self.weaponEquipped.getElement() == 1:
                damageFinal += damage + 5

        elif element == 3 and self.weaponEquipped.getElement() == 2:
                damageFinal += damage

        elif element == 3 and self.weaponEquipped.getElement() == 4:
                damageFinal += damage ** 2

        elif element == 4 and self.weaponEquipped.getElement() == 1:
                damageFinal += damage/7

        elif element == 4 and self.weaponEquipped.getElement() == 2:
                damageFinal += damage

        elif element == 4 and self.weaponEquipped.getElement() == 3:
                damageFinal += damage/3
        
        return damageFinal

    def damageTaken(self,damage,element):
        self.chanceEscape()
        #print("Levou uma: ",self.isEscape)
        if not self.isEscape:
            self.life -= self.balenceWeapons(damage,element)     
        else:
            self.life -= 0

class BattleField:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.endgame = False

    def fight(self):

        attacker = choice([self.player1,self.player2])
        itWillTake = None
       
        if attacker == self.player1:
            itWillTake = self.player2
        if attacker == self.player2:
            itWillTake = self.player1
        else:
            pass

        if attacker.isEquipped() and itWillTake.isEquipped():
            pass

        else:
            if (not attacker.isEquipped()):
                return f"o jogador {attacker.name} esta desarmado equipe uma arma antes de iniciar a batalha"
            else:
                return f"o jogador {itWillTake.name} esta desarmado equipe uma arma antes de iniciar a batalha"


        d,e = attacker.damageCaused()
        itWillTake.damageTaken(d,e)
        
        
        if self.player1.life <= 0:
           self.endgame = True
           return self.attackingWith(attacker,itWillTake) + "\n" + f"O {self.player2.name} ganhou!!\n"
        elif self.player2.life <= 0:
            self.endgame = True
            return self.attackingWith(attacker,itWillTake) + "\n" + f"O {self.player1.name} ganhou!!\n"
        else:
            self.endgame = False
            return "O pau ainda ta rolando" + "\n" + self.attackingWith(attacker,itWillTake)

    def showPlayersStatus(self):
        s = "=--=--=--="*2
        f = "=========="*5
    
        return f"Player1: \nVida:{self.player1.life if self.player1.life >= 0 else 0}\n {s}\nPlayer2: \nVida:{self.player2.life if self.player2.life >= 0 else 0}\n{f}"
    
    def attackingWith(self,att,itW):
        #print("Bf:",itW.isEscape)
        d,e = att.damageCaused()
        return f"""
O {att.name} atacou o {itW.name} com {att.weaponEquipped._type} de {att.weaponEquipped.getElementName()} causando {itW.balenceWeapons(d,e)}
contra uma {itW.weaponEquipped._type} de {itW.weaponEquipped.getElementName()} 
{f"So que foi um golpe errado, com isso o {itW.name} diz '{self.showIfEscape()}'" if itW.isEscape else ""}
        """
    def showIfEscape(self):
        f = choice(["Errou o ataque, ha hah ha", "Talvez na proxima","Se continuar vivo te ensino a usar esse seu brinquedinho"])
        return f

    def champion(self):

        if self.player1.life > self.player2.life:
            return self.player1.name

        elif self.player1.life < self.player2.life:
            return self.player2.name

        else:
            return 0
    
    def end(self):
        return self.endgame
