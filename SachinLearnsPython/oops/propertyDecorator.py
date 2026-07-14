#@property decorator - controlled attribute access
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius     #protected attribute

    @property
    def celsius(self):              #getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):       #setter with validation
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):           #computed property (read-only)
        return self._celsius * 9/5 + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15

t = Temperature(25)
print(f"Celsius:    {t.celsius}")
print(f"Fahrenheit: {t.fahrenheit}")
print(f"Kelvin:     {t.kelvin}")

t.celsius = 100
print(f"Boiling point in F: {t.fahrenheit}")

try:
    t.celsius = -300
except ValueError as e:
    print(f"Error: {e}")
