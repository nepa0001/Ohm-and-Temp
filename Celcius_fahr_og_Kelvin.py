from machine import Pin, ADC
from time import sleep

class LMT84:
    def __init__(self, pin_number=35, atten=2, alpha=-4.85, beta=1035, adc2_mv=2048/4095, average=128):
        self.pin_number = pin_number
        self.atten = atten
        self.alpha = alpha
        self.beta = beta
        self.adc2_mv =adc2_mv
        self.temperature_celsius = None 
        self.temperature_farhenheit = None
        self.temperature_kelvin = None
        self.lmt84_ADC = ADC(Pin(pin_number, Pin.IN))
        self.lmt84_ADC.atten(atten)
        self.average = average
        
    
    def get_temperature_celsius(self):
          ADC_value = 0
          if self.average > 1:
               for i in range(self.average):
                   ADC_value +=self.lmt84_ADC.read()
                   sleep(1 / self.average)
               ADC_value = ADC_value / self.average
          else:
              ADC_value = self.lmt84_ADC.read()
              sleep(1)
        
          mV = self.adc2_mv * ADC_value
          temp = (mV - self.beta) / self.alpha
          return temp
        
    def get_temperature_fahrenheit(self):
        celsius = self.get_temperature_celsius()
        print("celsius", celsius)
        # lav udregning er
        fahrenheit = celsius * 1.8 + 32
        print("fahr", fahrenheit)
        

    
    def get_temperature_kelvin(self):
        celsius = self.get_temperature_celsius()
        print("celsius", celsius)
        
        kelvin = celsius + 273.15
        print("kelvin", kelvin)
    
        

lmt84 = LMT84()
print(lmt84.get_temperature_fahrenheit())
print (lmt84.get_temperature_kelvin())