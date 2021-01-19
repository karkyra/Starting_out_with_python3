# Compute the wind chill index for a given air temperature and wind speed

WC_OFFSET = 13.12
WC_FACTOR1 = 0.6215
WC_FACTOR2 = -11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16

temp = float(input("Air temperatura degrees Celsius): "))
speed = float(input("Wind speed (kilometers per hour): "))

wci = WC_OFFSET + WC_FACTOR1 * temp + WC_FACTOR2 * speed ** WC_EXPONENT + \
      WC_FACTOR3 * temp * speed ** WC_EXPONENT

print("The wind chill index is", round(wci))
