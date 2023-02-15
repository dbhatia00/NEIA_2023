# A Program to Convert Farenheit to Celsius

def convertFtoC(tempF):
    tempC = (tempF - 32) * (5/9)
    return tempC

print(convertFtoC(32))