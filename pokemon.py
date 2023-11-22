import time
import numpy as np
import sys 

#Imprime texto lento, una letra a la vez
def slowPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, type, moves, EVs, healthPoints="===================="):
        #guardar variables como atributos
        self.name = name
        self.type = type
        self.moves = moves
        self.attack = EVs["attack"]
        self.defense = EVs["defense"]
        self.healthPoints = healthPoints
        self.bars = 20 #health points en barras

    def fight(self, Pokemon2):
        print("-----POKEMON BATTLE-----")
        #Pokemon 1
        print(f"\n{self.name}")
        print("type/", self.type)
        print("attack/", self.attack)
        print("defense/", self.defense)
        print("Lv./", 3*(1+np.mean([self.attack, self.defense])))
        print("\nVS")
        #Pokemon 2
        print(f"\n{Pokemon2.name}")
        print("type/", Pokemon2.type)
        print("attack/", Pokemon2.attack)
        print("defense/", Pokemon2.defense)
        print("Lv./", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))
        time.sleep(2)
    
        #Considera las ventajas del tipo    
    
        version = ["fire", "water", "grass"]
        for i,k in enumerate(version):
            
            if self.type == k:
                #mismo tipo
                if Pokemon2.type == k:
                    atkChain1 = "\nIt's not very effective..."
                    atkChain2 = "\nIt's not very effective..."
                #Pokemon2 tiene ventaja de tipo
                if Pokemon2.type == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    atkChain1 = "\nIt's not very effective..."
                    atkChain2 = "\nIt's super effective!"
                #self tiene la ventaja
                if self.type == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    atkChain1 = "\nIt's super effective!"
                    atkChain2 = "\nIt's not very effective..."
                    
        #turnos
        while (self.bars > 0) and (Pokemon2.bars > 0):
            print(f"\n{self.name}\t\tHP\t{self.healthPoints}")
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.healthPoints}")
            
            #Pokemon 1 (self)
            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("Choose your move: "))
            slowPrint(f"\n{self.name} used {self.moves[index-1]}")
            
            
            #Daño al Pokemon 2
            Pokemon2.bars -= self.attack
            Pokemon2.healthPoints = ""
            
            #Agregando barras mas un boost de defensa
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.healthPoints += "="
            
            time.sleep(1)
            print(f"\n{self.name}\t\tHP\t{self.healthPoints}")
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.healthPoints}")
            time.sleep(.5)
            
            #Comprobar si Pokemon 2 se debilitó
            if Pokemon2.bars <= 0:
                slowPrint("\n..."+ Pokemon2.name + " fainted.")
                break
            
            #Pokemon 2
            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input("Choose your move: "))
            slowPrint(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            
            #Daño al Pokemon 1
            self.bars -= Pokemon2.attack
            self.healthPoints = ""
            
            #Agregando barras mas un boost de defensa
            for j in range(int(self.bars+.2*self.defense)):
                self.healthPoints += "=="
            
            time.sleep(1)
            print(f"\n{self.name}\t\tHP\t{self.healthPoints}")
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.healthPoints}")
            time.sleep(.5)
            
            #Comprobar si Pokemon 1 se debilitó
            if self.bars <= 0:
                slowPrint("\n..."+ self.name + " fainted.")
                break
            
        #el dinero
        money = np.random.choice(5000)
        slowPrint(f"\nYou won ${money}\n")
        
        
if __name__ == "__main__":
    #Pokemones
    Charizard = Pokemon("Charizard", "fire", ['Flamethrower', 'Pyrotechnics', 'Fire Spin', 'Ember'], {"attack": 14, "defense": 20})
    Blastoise = Pokemon("Blastoise", "water", ['Water Gun', 'Bubble Beam', 'Hydropulse', 'Hydrobomb'], {"attack": 10, "defense": 16})
    Venusaur = Pokemon("Venusaur", "grass", ['Vine Whip', 'Razor Leaf', 'Solar Beam', 'Worry Seed'], {"attack": 8, "defense": 24})
    
    #ACTIVAR LUCHA
    #pokemon1.fight(pokemon2)
    Charizard.fight(Blastoise)