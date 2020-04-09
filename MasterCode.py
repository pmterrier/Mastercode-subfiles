import math
import time

while(True):

	info = open("data.srt","w")
	info.close

	i = 1
	for i in range(1,67):
	
		#h, t = Baro.barometer() #height and Temperature
		h = 72
		t = 72
		#gps_long, gps_lat = GPS.gps()
		gps_long = -87.5436688
		gps_lat = 33.2157085
		#mag_x, mag_y = Mag.magnetometer()
		mag_x = 15.820
		mag_y = 12.698
		D = math.atan((mag_y) / (mag_x)) * ((180 / math.pi))

		#theta is angle from due North
		if mag_x == 0:
			if mag_y < 0:
				theta = 90
			else:
				theta = 0
		else:
			if D >= 360:
				theta = D - 360
			elif D < 0:
				theta = D + 360
			else:
				theta = D

		d = h / (math.cos((math.pi) / 4)) #distance to object from camera

		alpha = 0.872665 #(50 / 180) * (math.pi) horizontal angle of cam
		beta = 0.7155850 #(41 / 180) * (math.pi) vertical angle of cam

		w = 2 * d * math.tan(alpha / 2) #width of view
		l = 2 * d * math.tan(beta / 2) #length of view

		pos = abs(gps_long)
		gps_deg_long = math.floor(pos) #degrees
		gps_min_long = math.floor(((pos) - (gps_deg_long)) * 60) #minutes
		gps_sec_long = (((pos - gps_deg_long) * 60) - gps_min_long) * 60 #seconds

		gps_deg_lat = math.floor(gps_lat) #degrees
		gps_min_lat = math.floor(((gps_lat) - (gps_deg_lat)) * 60) #minutes
		gps_sec_lat = (((gps_lat - gps_deg_lat) * 60) - gps_min_lat) *60 #seconds

		delta_lat = 111194.93 #m/deg
		delta_long = ((0.0671)*(gps_lat**3)) - ((20.464)*(gps_lat**2)) + ((63.042)*(gps_lat)) + (110989) #m/deg
	
		gps_long_met = gps_long * delta_long
		gps_lat_met = gps_lat * delta_lat

		dg = d * math.cos(math.pi / 4)
		x = dg * math.sin((theta * (math.pi / 180)))
		y = dg * math.cos((theta * (math.pi / 180)))

		gps_lat_met_poi = gps_lat_met + y
		gps_long_met_poi = gps_long_met + x

		gps_lat_poi = gps_lat_met_poi / delta_lat
		gps_long_poi = gps_long_met_poi / delta_long

		pos_poi = abs(gps_long_poi)
		gps_deg_long_poi = math.floor(pos_poi) #degrees
		gps_min_long_poi = math.floor(((pos_poi) - (gps_deg_long_poi)) * 60) #minutes
		gps_sec_long_poi = (((pos_poi - gps_deg_long_poi) * 60) - gps_min_long_poi) * 60 #seconds


		gps_deg_lat_poi = math.floor(gps_lat_poi) #degrees
		gps_min_lat_poi = math.floor(((gps_lat_poi) - (gps_deg_lat_poi)) * 60) #minutes
		gps_sec_lat_poi = (((gps_lat_poi - gps_deg_lat_poi) * 60) - gps_min_lat_poi) *60 #seconds

		info = open("data.srt","a")

		info.truncate(0)
		
		print >>info, "1"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "Module Height: %.6f m\n"%(h)
		print >>info, "2"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "Temperature: %.6f C\n"%(t)
		print >>info, "3"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "Degrees from North: %.6f\n"%(theta)
		print >>info, "4"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "Distance to POI: %.6f m\n"%(d)
		print >>info, "5"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "FOV: %.6f m X %.6f m\n"%(w,l)
		print >>info, "6"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "Longitude: ",gps_deg_long,"deg",gps_min_long,"min",gps_sec_long,"sec W\n"
		print >>info, "7"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "Latitude: ",gps_deg_lat,"deg",gps_min_lat,"min",gps_sec_lat,"sec N\n"
		print >>info, "8"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "POI Longitude: ",gps_deg_long_poi,"deg",gps_min_long_poi,"min",gps_sec_long_poi,"sec W\n"
		print >>info, "9"
		print >>info, "00:00:00,000 --> 00:00:60,000"
		print >>info, "POI Latitude: ",gps_deg_lat_poi,"deg",gps_min_lat_poi,"min",gps_sec_lat_poi,"sec N\n"

		info.close()

		i = i + 1
		time.sleep(1)
		