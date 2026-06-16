class Temperature:
    def __init__(self, degree=0):
        #avant le setter
        #self.__celsius = degree
        #après le setter
        self.celsius = degree
    
    #Lire la Temperature en celsius
    @property
    def celsius(self):
        return self.__celsius
    
    #Ecrire la Temperature en celsius
    @celsius.setter
    def celsius(self, new_temp):
        if not isinstance(new_temp, (int, float)) or new_temp < -273.15:
            raise ValueError ("La temperature ne peut dépasser le zéro absolu")
        self.__celsius = new_temp
    
    #Lire la Temperature en fahrenheit
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    #Ecrire la Temp en fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, fahren):
        self.celsius = (fahren - 32) * 5/9


t = Temperature()
t.celsius = 25
print(f"{t.celsius}°C = {t.fahrenheit}°F")  # 25°C = 77.0°F

t.fahrenheit = 100
print(f"{t.celsius}°C = {t.fahrenheit}°F")  # 37.777...°C = 100.0°F

try:
    t.celsius = -300
except ValueError as e:
    print("Erreur :", e)

try:
    t.fahrenheit = -500  # Correspond à environ -295°C, donc en dessous du zéro absolu
except ValueError as e:
    print("Erreur :", e)