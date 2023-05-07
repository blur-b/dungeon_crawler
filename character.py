class Character:
    def __init__(self, sprite, hp=100, defense=0, damage=5, speed=5, width=0, height=0, x=0, y=0):
        self.sprite = sprite
        self.hp = hp
        self.defense = defense
        self.damage = damage
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_sprite(self):
        return self.sprite

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
    
    def set_sprite(self, sprite):
        self.sprite = sprite

    def set_hp(self, hp):
        if hp >= 0:
            self.hp = hp

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

class Player(Character):
    def __init__(self, sprite, width, height, stamina=100, num_arrows=0, x=0, y=0):
        super().__init__(sprite=sprite, width=width, height=height, x=x, y=y)
        self.stamina = stamina
        self.num_arrows = num_arrows

    def get_stamina(self):
        return self.stamina

    def get_num_arrows(self):
        return self.num_arrows

class Slime(Character):
    def __init__(self, sprite, width, height, hp=50, defense=1, damage=10, speed=1, x=0, y=0):
        super().__init__(sprite, hp, defense, damage, speed, width, height, x, y)
