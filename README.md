# Human Detection Using OpenCV
The dataset is retail catalog images from multiple photographers/sources depicting fashion, home goods, and beauty products in an XML/JSON/CSV file
format. When human models are present in these types of images, they are partially cropped silhouettes(waist-up, waist-down, etc.) and shot front/back/side profile to emphasize the product being featured. 
what I did here is write a quick script that will visit the images URL lists, grab the links, visit the links, pull the images, resize them,convert them to grayscale, save them, and repeat until we're done. after these steps, I used haarcascade_frontalface_default.xml to detect faces in the image and haarcascade_lowerbody_default.xml to detect human in the images cropped waist-down. and also I trained my own haarcascade classifier to detect upper body and it's not working well so far, I'm still working on it. and I will train it again on the images taken from imagenet but it will takes a couple of days to get access to download images. 
