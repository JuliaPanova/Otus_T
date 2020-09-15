from Task_2.ship import Ship
from Task_2.plane import Plane
from Task_2.bus import Bus, PickUpError, NegPassError
from Task_2.truck import Truck, LoadError, NegCargoError
from Task_2.transport import Engine, FuelError, TankError, TankUpError


def try_tank_up(transport, amount):
    """This function tries to tank up the transport"""
    try:
        transport.tank_up(amount)
    except TankUpError as e:
        print(e)
    except FuelError as e:
        print(e)


def try_pick_up(bus, num_of_people):
    """This function tries to pick up some passengers"""
    try:
        bus.pick_up(num_of_people)
    except PickUpError as e:
        print(e)
    except NegPassError as e:
        print(e)


def try_load(truck, new_cargo):
    """This function tries to load some cargo"""
    try:
        truck.load(new_cargo)
    except LoadError as e:
        print(e)
    except NegCargoError as e:
        print(e)



print('\n'+'='*90+'\nThis is a ship\n'+'-'*90)
ship = Ship(200, 3000, Engine(30, 500), 5000, 2)
print(ship)
ship.move()
try_tank_up(ship, 3500)
try_tank_up(ship, 0)
try_tank_up(ship, 2000)
try:
    ship.start_engine()
except FuelError as e:
    print(e)
ship.stop_engine()


print('\n'+'='*90+'\nThis is a plane\n'+'-'*90)
plane = Plane(41, 5000, Engine(50, 3000), 10000, 2)
print(plane)
plane.move()
try_tank_up(plane, 7000)
try_tank_up(plane, -5)
try_tank_up(plane, 2000)
try:
    plane.start_engine()
except FuelError as e:
    print(e)
plane.stop_engine()


print('\n'+'='*90+'\nThis is a bus\n'+'-'*90)
bus = Bus(5, 100, Engine(5, 1000), 200, 4, 50, 0)
print(bus)
bus.move()
try_tank_up(bus, 150)
try_tank_up(bus, 0)
try_tank_up(bus, 100)

try_pick_up(bus, 70)
try_pick_up(bus, -10)
try_pick_up(bus, 30)
try:
    bus.start_engine()
except FuelError as e:
    print(e)
bus.stop_engine()


print('\n'+'='*90+'\nThis is a truck\n'+'-'*90)
truck = Truck(10, 150, Engine(7, 1500), 300, 8, 40, 20)
print(truck)
truck.move()
try_tank_up(truck, 250)
try_tank_up(truck, -50)
try_tank_up(truck, 100)

try_load(truck, 50)
try_load(truck, -1)
try_load(truck, 15)
try:
    truck.start_engine()
except FuelError as e:
    print(e)
truck.stop_engine()
