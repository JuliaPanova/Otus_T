from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from Task_2.transport_exceptions import WeightError, FuelError, TankError, TankUpError


class Transport(metaclass=ABCMeta):
    """
    Abstract class which is common for all the transportation means
    """
    @abstractmethod
    def move(self):
        """This function shows the type of movement"""
        raise NotImplementedError

    @abstractmethod
    def stop_engine(self):
        """This function stops the engine"""
        raise NotImplementedError

    def tank_up(self, amount):
        """This function is used to fuel up the transport"""
        if amount <= 0:
            raise FuelError(amount)
        if self.fuel + amount > self.tank_volume:
            raise TankUpError(self.tank_volume, self.fuel, amount)
        self.fuel += amount
        print("The {} has been fueled up.".format(self.__class__.__name__.lower()))

    def start_engine(self):
        """This function starts the engine"""
        if self.fuel == 0:
            raise FuelError(self.fuel)
        print("Starting the engine...")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, val):
        if val <= 0:
            raise WeightError()
        self.__weight = val

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, val):
        if val < 0:
            raise FuelError(val)
        self.__fuel = val

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, obj):
        self.__engine = obj

    @property
    def tank_volume(self):
        return self.__tank_volume

    @tank_volume.setter
    def tank_volume(self, val):
        if val <= 0:
            raise TankError()
        self.__tank_volume = val

@dataclass
class Engine:
    volume: int
    rpm: int