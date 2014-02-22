#!usr/bin/python27

import commands
import time

def main():
	eventFlag = False
	while 1:
		time.sleep(0.01)
		seconds = time.time()
		if not int(seconds % 3):
			if eventFlag:
				commands.getoutput("sass main.scss:main.css -t expanded -l")
		else:
			eventFlag = True


if __name__ == "__main__":
	main()
