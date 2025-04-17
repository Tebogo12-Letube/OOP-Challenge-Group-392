from pet import Pet

# Create a pet object
my_pet = Pet(name="Marlem")

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

print("\nTraining Tricks:")
my_pet.train("sit")
my_pet.train("roll over")   
my_pet.train("play dead")
my_pet.train("roll over")  # Should indicate already learned
my_pet.show_tricks()
print("\nFinal Status:")
my_pet.get_status()
