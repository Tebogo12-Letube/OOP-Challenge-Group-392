from pet import Pet

marlem = Pet("Marlem")

print(f"Creating pet: {marlem.name}\n")

print(f"{marlem.name} is eating...")
marlem.eat()
print(f"{marlem.name} is playing...")
marlem.play()
print(f"{marlem.name} is sleeping...")
marlem.sleep()

print("\nMarlem's current status:")
marlem.get_status()

marlem.train("Sit")
marlem.train("Roll Over")
print("\nTricks learned:")
marlem.show_tricks()
