import time
import navio.ms5611
import navio.util

def barometer():

	navio.util.check_apm()

	baro = navio.ms5611.MS5611()

	baro.initialize()

	baro.refreshPressure()

	time.sleep(0.01)

	baro.readPressure()

	baro.refreshTemperature()

	time.sleep(0.01)

	baro.readTemperature()

	baro.calculatePressureAndTemperature()

	height = (((1013.25/baro.PRES)**(1/5.257)-1)*(baro.TEMP+273.15))/ 0.0065

	height = height - 45 

	temp = baro.TEMP

	return(height, temp)
