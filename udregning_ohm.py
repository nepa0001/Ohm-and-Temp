from ohms import OhmsLawCalculator
#⇊⇊⇊⇊den ønskedde lommeregner, til at finde sin ønskede værdi#⇊⇊⇊


#ohms_law_calculator = (OhmsLawCalculator(voltage=12, current=3))
#print("modstand")

#ohms_law_calculator = (OhmsLawCalculator(voltage=6, resistance=5))
#print("strøm")

ohms_law_calculator = (OhmsLawCalculator(voltage=500, current=4.5))
print("effekt")

#ohms_law_calculator = (OhmsLawCalculator(resistance=6, current=5))
#print("Spændning")

#--------------⇊⇊⇊------Den ønskede omhs lovs værdi--⇊⇊⇊--------------------------------#


#resistance_result = ohms_law_calculator.calculate_resistance()
#print(f"Resistance: {resistance_result} ohms")

#current_result = ohms_law_calculator.calculate_current()
#print(f"current: {current_result} amp")

power_result = ohms_law_calculator.calculate_power()
print(f"power: {power_result} watt")

#voltage_result = ohms_law_calculator.calculate_voltage()
#print(f"voltage: {voltage_result} volt")