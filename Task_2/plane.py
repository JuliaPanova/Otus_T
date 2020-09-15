from Task_2.transport import Transport, FuelError


class Plane(Transport):
    """
    Class for planes
    """
    def __init__(self, weight, fuel, engine, tank_volume, number_of_wings):
        self.weight = weight
        self.fuel = fuel
        self.engine = engine
        self.tank_volume = tank_volume
        self.number_of_wings = number_of_wings
    def __repr__(self):
        return 'This plane has {} wings and weighs {} tons. The engine volume is {} litres and max rpm is {}. The tank volume is {} litres.'\
            .format(self.number_of_wings, self.weight, self.engine.volume, self.engine.rpm, self.tank_volume)

    def move(self):
        """This function shows the type of movement"""
        print("The plane can fly.")

    def tank_up(self, amount):
        """This function is used to fuel up the transport"""
        super().tank_up(amount)
        print("Now the amount of fuel is {} litres.".format(self.fuel))

    def start_engine(self):
        """This function starts the engine"""
        super().start_engine()
        print("Now the plane is ready to take off.")

    def stop_engine(self):
        """This function stops the engine"""
        print("The plane has stopped.")