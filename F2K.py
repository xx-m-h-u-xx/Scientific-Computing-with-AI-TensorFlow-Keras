# F2K Converter

"""
    A function to convert degrees Fahrenheit to Kelvin
"""

def F2K():
    F = float(input("Enter temperature in degrees Fahrenheit: "))
    K = (F + 459.67) * 5 / 9
    print("Temparature in Kelvin is {:08.4f} K".format(K))
