from SerialClass import SerialAchieve   # Import serial communication class
from web import get_hex_code

myser = SerialAchieve(band=115200)
# myser.open_port("/dev/ttyUSB0")
myser.open_port("COM4")

hex_code = get_hex_code()

if hex_code != None:
	count = 0
	for index,line in enumerate(hex_code):
		print(line)
		myser.Write_data(line)
		check = myser.Read_data()
		print(check)
		while (check != 'ok'):
			check = myser.Read_data()
			print(check)

		count = count + 1
		print(count)
		if index % 10 == 0:
			print('.')

	print("done Update", count,' ',index)
else:
	print("No Update Found now!")
