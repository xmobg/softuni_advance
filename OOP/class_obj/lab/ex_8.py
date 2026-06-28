class Thermometer:
    def __init__(self,temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def is_freezing(self):
        if self.temperature <= 0:
            return True
        return False

    def is_hot(self):
        if self.temperature >= 30:
            return True
        return False

    def __str__(self):
        return f"{self.temperature}°C / {self.to_fahrenheit()}°F"


t = Thermometer(100)
print(t)               # 100°C / 212.0°F
print(t.is_freezing()) # False
print(t.is_hot())      # True

t2 = Thermometer(-5)
print(t2)              # -5°C / 23.0°F
print(t2.is_freezing()) # True