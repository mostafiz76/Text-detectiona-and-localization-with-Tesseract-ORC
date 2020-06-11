##OCR : Text detection and localization with Tesseract
##import libraries
##Author: Mostafiz
from pytesseract import Output
import pytesseract
import argparse
import cv2

if __name__ == '__main__':
	#Read the test image
	image = cv2.imread('test.jpg')
	#convert BGR to RGB
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	#use Tesseract to localize
	texts = pytesseract.image_to_data(rgb, output_type=Output.DICT)
	
	#walk through the resulting text
	for i in range(0, len(texts["text"])):
		# get  coordinates of the bounding box	
		x = texts["left"][i]
		y = texts["top"][i]
		w = texts["width"][i]
		h = texts["height"][i]

		# get the OCR text along with its confidence of the	
		text = texts["text"][i]
		conf = int(texts["conf"][i])
		print(text,conf)

		if conf > 60:
			# printing the text and its confidence
			print("Confidence: {}".format(conf))
			print("Text: {}".format(text))
			print("")
			text = "".join([c if ord(c) < 128 else "" for c in text]).strip()

			#draw the bounding boxes and write the text on the image
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
			cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			1.2, (0, 0, 255), 3)

	# show the output image
	cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
	cv2.imwrite('result.jpg',image)
	cv2.imshow("Image", image)
	cv2.waitKey(0)


