class Pet:
    def __init__(self, name, hunger=5, energy=5, happiness=5):
        """
        Initialize a Pet object with name, hunger, energy, and happiness attributes.
        :param name: str - The name of the pet.
        :param hunger: int - Hunger level (0 = full, 10 = very hungry). Default is 5.
        :param energy: int - Energy level (0 = tired, 10 = fully rested). Default is 5.
        :param happiness: int - Happiness level (0–10). Default is 5.
        """
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness

    def eat(self):
        """Reduces hunger by 3 points (but not below 0), and increases happiness by 1."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        """Increases energy by 5 points (but not above 10)."""
        self.energy = min(10, self.energy + 5)

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1."""
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        """Prints the current state of the pet."""
        print(f"Pet Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

        from pet import Pet

# Create a pet object
my_pet = Pet(name="Simba")

# Test the methods
print("Initial Status:")
my_pet.get_status()

print("\nAfter Eating:")
my_pet.eat()
my_pet.get_status()

print("\nAfter Sleeping:")
my_pet.sleep()
my_pet.get_status()

print("\nAfter Playing:")
my_pet.play()
my_pet.get_status()