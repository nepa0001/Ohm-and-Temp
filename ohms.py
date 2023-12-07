class OhmsLawCalculator:
    def __init__(self, voltage=None, current=None, resistance=None, power=None):
        self.voltage = voltage
        self.current = current
        self.resistance = resistance
        self.power = power
        
    
    def calculate_power(self):
        if self.voltage is not None and self.current is not None:
            self.power = self.voltage * self.current
            return self.power
        else:
            raise ValueError("Both voltage and current must be typed to get power.")
        
    def calculate_voltage(self):
        if self.current is not None and self.resistance is not None:
            self.voltage = self.current * self.resistance
            return self.voltage
        else:
            raise ValueError("Both current and resistance must be typed to get voltage.")

    def calculate_current(self):
        if self.voltage is not None and self.resistance is not None:
            self.current = self.voltage / self.resistance
            return self.current
        else:
            raise ValueError("Both voltage and resistance must be typed to get current.")

    def calculate_resistance(self):
        if self.voltage is not None and self.current is not None:
            self.resistance = self.voltage / self.current
            return self.resistance
        else:
            raise ValueError("Both voltage and current must be typed to get resistance.")

