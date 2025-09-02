import random
game_title = "Gardening Simulator III"
game_description = "In this game you will find seeds, nuture them, and harvest your crops!"
commands = ['Forage: Forage the forest for a random plant seed and add it to your inventory.', 
            'Plant: Select a seed from your inventory and plant it.', 
            'Tend: Tend to your growing plants and progress each of them to the next growth stage. You must tend to your plants repeatedly until they are harvest ready.',
            'Harvest: Select a plant from you garden and harvest the crop, if it is harvest ready.',
            'Quit: Quit the simulator.' ]

class Plant(object):

    def __init__(self, name: str, harvest_yield: int, growth_stages: list):
        self.name = name
        self.harvest_yield = harvest_yield
        self.growth_stages = growth_stages
        self.current_growth_stage = self.growth_stages[0]
        self.harvestable = False

    def grow(self) -> None:
        curr_index = self.growth_stages.index(self.current_growth_stage)

        if self.current_growth_stage == self.growth_stages[-1]: # If the plant is already at its final growth stage, set harvestable to True 
            self.harvestable = True
            print(f"{self.name} is already fully grown!")
        elif curr_index < len(self.growth_stages) - 1:

            self.current_growth_stage = self.growth_stages[curr_index + 1]
            print(f"{username}'s {self.name.lower()} has grown to the next stage, {self.current_growth_stage}!")
            
            if self.current_growth_stage == self.growth_stages[-1]: # If the plant has reached its final stage, set harvestable to True
                self.harvestable = True
                print(f"{self.name} is ready for harvest!")

    def harvest(self) -> int | None:
        if self.harvestable:
            return self.harvest_yield
        else:
            return None
        
class Tomato(Plant):

    def __init__(self):
        super().__init__('Tomato', 10, ['germination', 'early growth', 'vegetative growth', 'flowering', 'fruit formation', 'ripening', 'harvest-ready'])    

class Lettuce(Plant):
    
    def __init__(self):
        super().__init__('Lettuce', 5, ['seed', 'cotyledon', 'seedling', 'rosette', 'heading', 'harvest-ready'])
    
class Carrot(Plant):
    
    def __init__(self):
        super().__init__('Carrot', 3, ['seed', 'germination', 'seedling', 'vegetative growth', 'root development', 'maturation', 'harvest-ready'])

class Gardener(object):

    plant_dict = {'Tomato':Tomato, 'Lettuce':Lettuce, 'Carrot':Carrot}

    def __init__(self, name: str):
        self.name = name
        self.garden = []
        self.inventory = {}

    def forage_for_seeds(self) -> None:
        seed = random.choice(all_plants)

        if seed in self.inventory:
            self.inventory[seed] += 1
        else:
            self.inventory[seed] = 1
        print(f"{self.name} found a {seed} seed!")

    def plant(self) -> None:
        selected_plant = select_item(self.inventory)

        if selected_plant in self.inventory and self.inventory[selected_plant] > 0:
            self.inventory[selected_plant] -= 1
            
            if self.inventory[selected_plant] == 0:
                print(f"That was {self.name}'s last {selected_plant} seed.")
                del self.inventory[selected_plant]
            
            new_plant = self.plant_dict[selected_plant]()
            self.garden.append(new_plant)
            print(f"{self.name} planted a {selected_plant} seed.")
        else:
            print(f"{self.name} doesn't have any {selected_plant} seeds to plant!")
    
    def tend(self) -> None:
        for plant in self.garden:
            if plant.harvestable:
                print(f"{plant.name} is ready for harvest!")
            else:
                plant.grow()
    
    def harvest(self) -> None:
        selected_plant = select_item(self.garden)
        
        if selected_plant.harvestable:
            if selected_plant.name in self.inventory:   
                self.inventory[selected_plant.name] += selected_plant.harvest()
            else:
                self.inventory[selected_plant.name] = selected_plant.harvest()
            print(f"{self.name} harvested {selected_plant.harvest_yield} {selected_plant.name.lower()}s!")
            self.garden.remove(selected_plant)
        else:
            print(f"{self.name} can't harvest their {selected_plant.name} yet.")

def select_item(items: list[object] | dict[str, int]) -> object | str:
    # Check if items is a dictionary containing seed amounts or a list containing plant objects, then display contents.
    if type(items) == dict:
        item_list = list(items.keys())
        for i in range(len(item_list)):
            seed_type = item_list[i]
            print(f"{i + 1}. {seed_type} ({items.get(seed_type)} seed(s))")
    elif type(items) == list:
        item_list = items
        for i in range(len(items)):
            plant_type = item_list[i].name
            print(f"{i + 1}. {plant_type}")
    else:
        print("Invalid items type.")
        return None
    
    while True: # Prompt user until they enter a valid list option.
        user_input = input("Select an plant/seed by its option number: ")
        try:
            user_input = int(user_input)
            if 0 < user_input <= len(item_list):
                return item_list[user_input - 1]
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")

def valid_name() -> None:
    #Loop until the user submits a name of only letters
    while True:
        username = input("What will your gardener's name be? ")

        if username.isalpha():
            return username
        else:
            print("Please enter a name without numbers or special characters.")

all_plants = ['Tomato', 'Lettuce', 'Carrot']
valid_actions = ['forage','plant', 'tend', 'harvest', 'help', 'quit']

#Print game state
print(f"Welcome to {game_title}! {game_description}")
#Retrieve the user's name
username = valid_name()
#Create gardener object using username 
avatar = Gardener(username)

# Game Loop
while True:
    action = input(f"What will {username} do (Forage, Plant, Tend, Harvest, Help, or Quit)? ").lower()
    if action in valid_actions:
        if action == 'forage':
            avatar.forage_for_seeds()
        elif action == 'plant':
            avatar.plant()
        elif action == 'tend':
            avatar.tend()
        elif action == 'harvest':
            avatar.harvest()
        elif action == 'help':
            print("In this game there are five possible actions: \n")
            for i in commands:
                print(i, '\n')
        elif action == 'quit':
            print("Thanks for playing!")
            quit()
    else:
        print("Invalid action, please try again.")