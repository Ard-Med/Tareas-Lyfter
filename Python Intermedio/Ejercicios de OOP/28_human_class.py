# Cree las siguientes clases:
# Head
# Torso
# Arm
# Hand
# Leg
# Feet
# Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.

class Human:
    def __init__(self, head, torso):
        self.head = head
        self.torso = torso  
        pass

class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self,right_arm, left_arm, right_leg, left_leg):
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand
        pass

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self, feet):
        self.feet = feet
        pass

class Feet:
    def __init__(self):
        pass

right_hand = Hand()
right_arm = Arm(right_hand)

left_hand = Hand()
left_arm = Arm(left_hand)

right_feet = Feet()
right_leg = Leg(right_feet)

left_feet = Feet()
left_leg = Leg(left_feet)

torso = Torso(right_arm, left_arm, right_leg, left_leg)

head = Head()

human = Human(head, torso)