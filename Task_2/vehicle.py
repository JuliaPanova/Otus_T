from Task_2.transport import Transport, FuelError


class Vehicle(Transport):
    """
    Class for vehicles
    """
    def __init__(self, weight, fuel, engine, tank_volume, number_of_wheels):
        self.weight = weight
        self.fuel = fuel
        self.engine = engine
        self.tank_volume = tank_volume
        self.number_of_wheels = number_of_wheels

    def __repr__(self):
        return 'This {} has {} wheels and weighs {} tons. The engine volume is {} litres and max rpm is {}. The tank volume is {} litres.'\
            .format(self.__class__.__name__.lower(), self.number_of_wheels, self.weight, self.engine.volume, self.engine.rpm, self.tank_volume)

    def move(self):
        """This function shows the type of movement"""
        print("The {} can move on a road.".format(self.__class__.__name__.lower()))

    def tank_up(self, amount):
        """This function is used to fuel up the transport"""
        super().tank_up(amount)
        print("Now the amount of fuel is {} litres.".format(self.fuel))

    def start_engine(self):
        """This function starts the engine"""
        super().start_engine()
        print("Now the {} is ready to go.".format(self.__class__.__name__.lower()))

    def stop_engine(self):
        """This function stops the engine"""
        print("The {} has stopped.".format(self.__class__.__name__.lower()))