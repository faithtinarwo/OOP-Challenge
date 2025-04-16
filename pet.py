class Pet:
    def __init__(self, name):
        self.name = name 
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness +1)
        print(f"{self.name} eats. Hunger descreases, happiness increases slightly!")

    def sleep(self):
        self.energy = min(10, self.energy +5)
        print(f"{self.name} sleeps soundly. Energy restored!")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play right now.")
            return

        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness +2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} plays happily!")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'★' * self.energy}{'☆' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)} ({self.happiness}/10)")
        
        # Additional status messages based on levels
        if self.hunger >= 8:
            print(f"{self.name} is very hungry!")
        if self.energy <= 2:
            print(f"{self.name} is very tired!")
        if self.happiness <= 2:
            print(f"{self.name} is feeling sad.")

    
    def train(self, trick):
        """Teach the pet a new trick"""
        if self.energy < 3:
            print(f"{self.name} is too tired to learn right now.")
            return
        
        self.energy -= 1
        self.hunger += 1
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 2)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}.")
    
    def show_tricks(self):
        """Display all learned tricks"""
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")

        