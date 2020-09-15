from Task_2.transport import Transport, FuelError


class Ship(Transport):
    """
    Class for ships
    """
    def __init__(self, weight, fuel, engine, tank_volume, number_of_decks):
        self.weight = weight
        self.fuel = fuel
        self.engine = engine
        self.tank_volume = tank_volume
        self.number_of_decks = number_of_decks
    def __repr__(self):
        return 'This ship has {} decks and weighs {} tons. The engine volume is {} litres and max rpm is {}. The tank volume is {} litres.'\
            .format(self.number_of_decks, self.weight, self.engine.volume, self.engine.rpm, self.tank_volume)

    def move(self):
        """This function shows the type of movement"""
        print("The ship can sail.")

    def tank_up(self, amount):
        """This function is used to fuel up the transport"""
        super().tank_up(amount)
        print("Now the amount of fuel is {} litres.".format(self.fuel))

    def start_engine(self):
        """This function starts the engine"""
        super().start_engine()
        print("Now the ship is ready to set sail.")

    def stop_engine(self):
        """This function stops the engine"""
        print("The ship has stopped.")