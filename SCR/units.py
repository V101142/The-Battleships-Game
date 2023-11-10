class Unit:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def attack(self, other_unit):
        other_unit.health -= self.damage

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Damage: {self.damage})"
