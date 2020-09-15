from Task_2.vehicle import Vehicle


class Truck(Vehicle):
    """
    Truck is a subclass of Vehicle
    """
    def __init__(self, weight, fuel, engine, tank_volume, number_of_wheels, capacity, cargo):
        super().__init__(weight, fuel, engine, tank_volume, number_of_wheels)
        self.capacity = capacity
        self.cargo = cargo

    def __repr__(self):
        return """This {} has {} wheels and weighs {} tons. The engine volume is {} litres and max rpm is {}. The tank volume is {} litres. 
The load capacity is {} tons, and the current cargo weighs {} tons.""" \
            .format(self.__class__.__name__.lower(), self.number_of_wheels, self.weight, self.engine.volume,
                    self.engine.rpm, self.tank_volume, self.capacity, self.cargo)

    def load(self, new_cargo):
        """
        This function adds new cargo to the truck
        :param new_cargo: weight of cargo to be loaded
        """
        if new_cargo < 0:
            raise NegCargoError(new_cargo)
        if self.cargo + new_cargo > self.capacity:
            raise LoadError(self.capacity, self.cargo, new_cargo)
        self.cargo += new_cargo
        print("{} tons has been loaded. Now the total weight of cargo is {} tons.".format(new_cargo, self.cargo))

    def drop_off(self, cargo_to_remove):
        """
        This function adds new cargo to the truck
        :param new_cargo: weight of cargo to be loaded
        """
        if self.cargo == 0:
            print("The truck has no cargo.")
        else:
            self.cargo -= cargo_to_remove
            print("Now the truck has {} tons of cargo.".format(self.cargo))


class LoadError(ValueError):
    """
     Error in case the load capacity of the truck is not enough to load the cargo
    """
    def __init__(self, capacity, cargo, new_cargo):
        super().__init__("The load capacity of {} tons exceeded. Current cargo weight is {} tons. It's not possible to load {} more tons."\
                         .format(capacity, cargo, new_cargo))


class NegCargoError(ValueError):
    """
    Error in case the weight of cargo to pick up is negative
    """
    def __init__(self, new_cargo):
        super().__init__("Cargo weight cannot be less that zero ({} tons).".format(new_cargo))

