class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1      #after adding the animal to he corresponding list, we add it also to the total count

    def get_info(self, species):
        printing_result = ""
        if species == "mammal":
            printing_result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            printing_result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            printing_result += f"Birds in {self.name}: {', '.join(self.birds)}"

        printing_result += f"\nTotal animals: {Zoo.__animals}"
        return printing_result          #using variable printing result to add information, since we can only use one return in a function

#_________________________________________________________________________________

zoo_name = input()
number = int(input())
current_zoo = Zoo(zoo_name)         #creating object in the Zoo class with the defined name

for _ in range(number):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    current_zoo.add_animal(species, name)       #adding current animal to the current zoo using class method

species_info = input()
print(current_zoo.get_info(species_info))       #calling method from the object to print information about the given species


