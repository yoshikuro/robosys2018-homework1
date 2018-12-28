#!/usr/bin/python

import time
import subprocess

def main():
	dev_cmd = "ls /dev/usb | grep hiddev*"
	flag = 0

	while True:
		result = subprocess.Popen(dev_cmd, stdout=subprocess.PIPE,shell=True).communicate()[0].strip('\n')
		if flag == 0 and result == "hiddev0":
			led_cmd = "echo 1 > /dev/myled0"
			subprocess.call(led_cmd, shell=True)
			flag = 1
		if flag == 1 and result != "hiddev0":
			flag = 0
			led_cmd = "echo 0 > /dev/myled0"
			subprocess.call(led_cmd, shell=True)
		print("flag :", flag)
		time.sleep(0.5)
		
if __name__ == "__main__":
	main()
