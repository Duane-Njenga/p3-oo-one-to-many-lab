class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
    

        Pet.all.append(self)
        if owner and isinstance(owner, Owner):
            owner.add_pet(self)

    
class Owner:
    
    def __init__(self,name):
        self.name = name
        self._pets = []

    def pets(self): 
        return self._pets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.owner = self
        else:
            raise Exception

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda Pet: Pet.name)
owner = Owner("Ben")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
print(owner.pets())
