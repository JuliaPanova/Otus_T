class WeightError(ValueError):
    """
    Error in case weight <=0
    """
    def __init__(self):
        super().__init__("Weight cannot be zero or less than zero!")


class FuelError(ValueError):
    """
     Error in case fuel <=0
    """
    def __init__(self, amount):
        super().__init__("Fuel cannot be zero or less than zero ({} litres).".format(amount))


class TankError(ValueError):
    """
     Error in case the tank volume <=0
    """
    def __init__(self):
        super().__init__("The tank volume cannot be zero or less than zero!")


class TankUpError(ValueError):
    """
     Error in case the tank volume is not enough to fuel up the transport
    """
    def __init__(self, tank_volume, fuel, amount):
        super().__init__("""The maximum tank volume of {} litres exceeded. The current amount of fuel is {} litres.
It is not possible to fuel {} more litres.""".format(tank_volume, fuel, amount))

