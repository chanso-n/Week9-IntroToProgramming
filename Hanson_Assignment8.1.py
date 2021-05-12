ALL_OPTIONS = ['power mirrors', 'power locks', 'remote start', 'backup camera', 'bluetooth',
               'cruise control', '4 wheel drive', 'anti-lock brakes', 'power steering']

def choose_options():
    """Display all options"""
    for option in ALL_OPTIONS:
        print(f'You can choose {option}')

    print('Please enter your choices separated by a comma.')


class Vehicle:
    """An attempt to represent a car."""

    def __init__(self, make, model, color, fuelType, options):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options.split(", ")
        self.validate()

    def __repr__(self):
        return f'{self.make} {self.model}'

    def validate(self):
        if len(self.options) == 1 and self.options[0] == '':
            raise Exception('Must enter at least one option.')

        for option in self.options:
            if option not in ALL_OPTIONS:
                raise Exception('Option invalid!')
        

    def getMake(self):
        """Return the make of vehicle."""
        v_make = self.make
        return v_make.title()

    def getModel(self):
        """Return the model of vehicle."""
        v_model = self.model
        return v_model.title()

    def getColor(self):
        """Return the color of vehicle."""
        v_color = self.color
        return v_color.title()

    def getFuelType(self):
        """Return the fuel type of vehicle."""
        v_fuelType = self.fuelType
        return v_fuelType.title()

    def getOptions(self):
        """Return the options of vehicle."""
        v_options = self.options
        return v_options

#create car child class
    
class Car(Vehicle):
    """Initialize attributes of parent class.
        Then initialize attributes specific to cars."""

    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):

        super().__init__(make, model, color, fuelType, options)
        self.engineSize = engineSize
        self.numDoors = numDoors

    def getEngineSize(self):
        """Return the engine size of a car."""
        c_engineSize = self.engineSize
        return c_engineSize.title()

    def getNumDoors(self):
        """Return the number of doors."""
        c_numDoors = self.numDoors
        return c_numDoors.title()

#creat pickup child class
    
class Pickup(Vehicle):
    """Initialize attributes of parent class.
        Then initialize attributes specific to pickups."""

    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):

        super().__init__(make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    def getCabStyle(self):
        """Return the cab style."""
        t_cabStyle = self.cabStyle
        return t_cabStyle.title()

    def getBedLength(self):
        """Return the bed length."""
        t_bedLength = self.bedLength
        return t_bedLength.title()

garage = []

add_v_active = True

while add_v_active:
    vehicle_type = input('Would you like to add a car or a pickup? ').lower()
    vehicle_make = input('What is the make? ').lower()
    vehicle_model = input('What is the model? ').lower()  
    vehicle_color = input('What is the color? ').lower()
    vehicle_fuelType = input('What is the fuel type? ').lower()
    choose_options()
    vehicle_options = input('What options would you like? ').lower()

    if vehicle_type == 'car':
        engine_size = input('What is the engine size? ').lower()
        num_doors = input('How many doors? ')
        cab_style = 'N/A'
        bed_length = 'N/A'
        new_car = Car(vehicle_make, vehicle_model, vehicle_color, vehicle_fuelType, vehicle_options,
                    engine_size, num_doors)
        garage.append(new_car)

    if vehicle_type == 'pickup':
        engine_size = 'N/A'
        num_doors = 'N/A'
        cab_style = input('What is the cab style? ')
        bed_length = input('What is the bed length? ')
        new_pickup = Pickup(vehicle_make, vehicle_model, vehicle_color, vehicle_fuelType, vehicle_options,
                     cab_style, bed_length)
        garage.append(new_pickup)
 

#    garage[vehicle_type] = vehicle_make, vehicle_model, vehicle_color, vehicle_fuelType, vehicle_options, engine_size, num_doors, cab_style, bed_length

    repeat = input('Would you like to add another vehicle? (y/n) ')
    if repeat == 'n':
        add_v_active = False


print(f'You have {len(garage)} vehicles in your garage. ')

print(garage)

#garage_items = garage.items()

#print("\nHere are your vehicles: ")
#for item in garage_items:
#    print(item)









