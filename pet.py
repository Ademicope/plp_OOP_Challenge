class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """This function reduces hunger level by 3 but not below 0
        and increases happiness by 1
        """
        if self.hunger <= 2:
            self.hunger = 0
        else:
            self.hunger -= 3
            self.happiness += 1
        print(f"{self.name} ate, happiness increased\n")
        # print(f"Hunger level: {self.hunger}, Happiness_level: {self.happiness}")

    def sleep(self):
        """This function increases energy level by 5
          but not above 10
        """
        print(f"Energy level: {self.energy}")
        if self.energy >= 5:
            self.energy = 10
        else:
            self.energy += 5
        print(f"{self.name} slept.\n")
        # print(f"Current energy level: {self.energy}")

    def play(self):
        """This function reduces energy level by 2 but not below 0,
        increases happiness by 2, and increases hunger by 1
        """
        if self.energy <= 2:
            self.energy = 0
        else:
            self.energy -= 2
            self.happiness +=2
            self.hunger += 1
        print(f"{self.name} played, happiness increased\n")

    def train(self, trick):
        """This function adds a trick to the pet's tricks list,
        """
        # trick_list = self.tricks.append(input("Enter new trick for pet"))
        trick_list = trick.split(',')
        self.tricks.extend(trick_list)
    

    def show_tricks(self):
        """Displays all tricks learned by the pet."""

        for i, trick in enumerate(self.tricks):
            print(f"Trick {i+1}: {self.tricks[i]}")  # Strip removes any extra whitespace


    def get_status(self):
        """This function prints the current state of the pet"""
        print("Current status of the pet:")
        print(f"Pet name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks learned: {self.tricks}")

