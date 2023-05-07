class Character:
    def __init__(self, hp=100, defense=0, damage=5, speed=5, width=0, height=0, x=0, y=0):
        self.hp = hp
        self.defense = defense
        self.damage = damage
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_hp(self):
        return self.hp

    def get_defense(self):
        return self.defense

    def get_damage(self):
        return self.damage

    def get_speed(self):
        return self.speed

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

class Player(Character):
    def __init__(self, width, height, stamina=100, num_arrows=0, x=0, y=0):
        super().__init__(width=width, height=height, x=x, y=y)
        self.stamina = stamina
        self.num_arrows = num_arrows

    def get_stamina(self):
        return self.stamina

    def get_num_arrows(self):
        return self.num_arrows

class Slime(Character):
    def __init__(self, width, height, hp=50, defense=1, damage=10, speed=2, x=0, y=0):
        super().__init__(hp, defense, damage, speed, width, height, x, y)
