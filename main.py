from random import randint, choice

weigh_params = [
    1, 2, 3, 4, 5
]

colors = [
    "red", "blue", "green", "yellow"
]

motor_power = [
    100, 200, 300, 400, 500
]

acceleration_time = [
    "10sec", "20sec", "30sec", "40sec", "50sec", "60sec"
]

steering_wheel_side = [
    "right_side", "left_side"
]

gears = [
    1, 2, 3, 4
]

class Kick_scooter(object):
    def __init__(self, weigh, color, name):
        self.name = name
        self.weigh = weigh
        self.color = color

    def __str__(self):
        return "{} {} {}".format(self.weigh, self.color, self.name)

class Bicycle(Kick_scooter):
    def __init__(self, weigh, color, gears, name):
        super().__init__(weigh, color, name)
        self.name = name
        self.gears = gears

    def __str__(self):
        return super().__str__()+" {} ".format(self.gears)


class Electric_scooter(Kick_scooter):
    def __init__(self, weigh, color, motor_power, name):
        super().__init__(weigh, color, name)
        self.name = name
        self.motor_power = motor_power

    def __str__(self):
        return super().__str__()+" {} ".format(self.motor_power)

class Moto(Electric_scooter):
    def __init__(self, weigh, color, motor_power, acceleration_time, name):
        super().__init__(weigh, color, motor_power, name)
        self.name = name
        self.acceleration_time = acceleration_time

    def __str__(self):
        return super().__str__()+" {} ".format(self.acceleration_time)

class Auto(Moto):
    def __init__(self, weigh, color, motor_power, acceleration_time, steering_wheel_side, name):
        super().__init__(weigh, color, motor_power, acceleration_time, name)
        self.name = name
        self.steering_wheel_side = steering_wheel_side


    def __str__(self):
        return super().__str__()+" {} ".format(self.steering_wheel_side)


list = []
list_auto = []

class Garage():
    def add(self, item):
        list.append(item)

if __name__ == '__main__':
    g = Garage()

    for i in range(randint(1, 2)):
        s = Kick_scooter(choice(weigh_params), choice(colors), name="Kick_scooter")
        g.add(s)

    for i in range(randint(1, 2)):
        b = Bicycle(choice(weigh_params), choice(colors), choice(gears), name="Bicycle")
        g.add(b)

    for i in range(randint(1, 2)):
        e = Electric_scooter(choice(weigh_params), choice(colors), choice(motor_power), name="Electric_scooter")
        g.add(e)

    for i in range(randint(1, 2)):
        m = Moto(choice(weigh_params), choice(colors), choice(motor_power), choice(acceleration_time), name="Moto")
        g.add(m)

    for i in range(randint(1, 2)):
        a = Auto(choice(weigh_params), choice(colors), choice(motor_power), choice(acceleration_time), choice(steering_wheel_side), name="Auto")
        g.add(a)

    for i in list:
        if i.name == "Kick_scooter":
            print("Name: " + i.name + " Color: " + i.color + " Weight: " + str(i.weigh))

        if i.name == "Bycicle":
            print("Name: " + i.name + " Color: " + i.color + " Weight: " + i.weigh + " Gears: " + i.gears)

        if i.name == "Electric_scooter":
            print("Name: " + i.name + " Color: " + i.color + " Weight: " + str(i.weigh) + " Motor power: " + str(i.motor_power))

        if i.name == "Moto":
            print("Name: " + i.name + " Color: " + i.color + " Weight: " + str(i.weigh) + " Motor power: " + str(i.motor_power) + " Acceleration time: " + str(i.acceleration_time))

        if i.name == "Auto":
            print("Name: " + i.name + " Color: " + i.color + " Weight: " + str(i.weigh) + " Motor power: " + str(i.motor_power) + " Acceleration time: " + str(i.acceleration_time) + " Steering wheel side: " + i.steering_wheel_side)


    for i in list:
        if i.name == "Auto":
            list_auto.append(i)

    print("Quantity Auto: " + str(len(list_auto)))
    print("Quantity: " + str(len(list)))
