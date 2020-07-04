from animalone import Animal
from mammals import Big_Cats
from lions import Lion



lion_one = Animal("Mufasa","Lion",breathing=True,hunt=True)

lion_two = Big_Cats("Diego","Jaguar",breathing=True,hunt=True,mood="sad",climbing_ability=True)

lion_three = Lion("Scar","lion",breathing=True,hunt=True,mood=True,climbing_ability=True,hunter="female",mane=True,pride = 4)

lion_three.go_for_hunt()
lion_three.protect_pride()
lion_three.protect_prey()
lion_three.roar()

lion_two.roar()
lion_two.play_fighting()
lion_two.hunting()
lion_two.protect_prey()

lion_one.describe_animal()
lion_one.breathe()
lion_one.moving()
lion_one.eat()
lion_one.sleeping()