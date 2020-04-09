import spidev
import time
import argparse 
import sys
import navio.mpu9250
import navio.util

def magnetometer():

	navio.util.check_apm()

	parser = argparse.ArgumentParser()

	args = parser.parse_args()

	imu = navio.mpu9250.MPU9250()

	imu.initialize()

	time.sleep(0.5)

	# imu.read_all()
	# imu.read_gyro()
	# imu.read_acc()
	# imu.read_temp()
	# imu.read_mag()

	# print "Accelerometer: ", imu.accelerometer_data
	# print "Gyroscope:     ", imu.gyroscope_data
	# print "Temperature:   ", imu.temperature
	# print "Magnetometer:  ", imu.magnetometer_data

	# time.sleep(0.1)

	m9a, m9g, m9m = imu.getMotion9()

	return(m9m[0], m9m[1])