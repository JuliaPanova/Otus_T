from Task_2.vehicle import Vehicle


class Bus(Vehicle):
    """
    Bus is a subclass of Vehicle
    """
    def __init__(self, weight, fuel, engine, tank_volume, number_of_wheels, seats, passengers):
        super().__init__(weight, fuel, engine, tank_volume, number_of_wheels)
        self.seats = seats
        self.passengers = passengers

    def __repr__(self):
        return """This {} has {} wheels and weighs {} tons. The engine volume is {} litres and max rpm is {}. The tank volume is {} litres. 
The number of seats is {}, and currently the bus is carrying {} passengers.""" \
            .format(self.__class__.__name__.lower(), self.number_of_wheels, self.weight, self.engine.volume,
                    self.engine.rpm, self.tank_volume, self.seats, self.passengers)

    def pick_up(self, new_passengers):
        """
        This function adds new passengers to the bus
        :param new_passengers: number of passengers to pick up
        """
        if new_passengers < 0:
            raise NegPassError(new_passengers)
        if self.passengers + new_passengers > self.seats:
            raise PickUpError(self.passengers, self.seats, new_passengers)
        self.passengers += new_passengers
        print("{} passengers have taken their seats. Now the number of passengers is {}.".format(new_passengers, self.passengers))

    def drop_off(self, leaving_passengers):
        """
        This function removes some passengers from the bus
        :param leaving_passengers: number of passengers to drop off
        """
        if self.passengers == 0:
            print("The bus has no passengers in it.")
        else:
            self.passengers -= leaving_passengers
            print("Now the bus has {} passengers.".format(self.passengers))


class PickUpError(ValueError):
    """
     Error in case the bus does not have enough seats available to pick up all the passengers
    """
    def __init__(self, passengers, seats, new_passengers):
        super().__init__("{} seats have been taken. The number of seats ({}) is not enough to pick up {} more passengers."\
                         .format(passengers, seats, new_passengers))


class NegPassError(ValueError):
    """
    Error in case the number of passengers to pick up is negative
    """
    def __init__(self, new_passengers):
        super().__init__("The number of passengers cannot be less that zero ({} passengers).".format(new_passengers))

