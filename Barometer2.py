import sys
sys.stdout = open('DummyFile.txt','wt')
import time
import navio.ms5611
import navio.util
navio.util.check_apm()
baro = navio.ms5611.MS5611()
baro.initialize()
while(True):
	baro.refreshPressure()
	time.sleep(0.01)
	baro.readPressure()
	baro.refreshTemperature()
	time.sleep(0.01)
	baro.readTemperature()
	baro.calculatePressureAndTemperature()
	height = (((1013.25/baro.PRES)**(1/5.257)-1)*(baro.TEMP+273.15))/ 0.0065
	height = height - 45 
	print "Temperature(C): %.6f" % (baro.TEMP), "Pressure(millibar): %.6f" % (baro.PRES), "Height(m) %.6f" % (height)
	break