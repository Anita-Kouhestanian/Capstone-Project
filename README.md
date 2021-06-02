# Human Detection Using OpenCV
## Objective
Online shopping became so popular recently. we as customers look to brands for guidance. we may spend 3x more when given this guidance in a complete
outfit, furniture set, or beauty look.
FineMine creates visual contents for many amazing companies such as Adidas, Cole Haan and so on. right now, they create all these contents manually.  But manual content creation can only cover a small portion of the catalog, leaving revenue on the table.

For my capstone project, I will help FindMine automates and scales content creation for online retailers. 
In this project, I build different classifier to identify photos of isolated fashion products vs. human models wearing the fashion products. other words, the aim is to
detect whether a human model is present in product depiction photos. This would not be to determine what products are being depicted. 

The dataset is retail catalog images from multiple photographers/sources depicting fashion, home goods, and beauty products in an XML/JSON/CSV file
format. When human models are present in these types of images, they are partially cropped silhouettes(waist-up, waist-down, etc.) and shot front/back/side profile to emphasize the product being featured. 

what I did here is write a quick script that will visit the images URL lists, grab the links, visit the links, pull the images, resize them,convert them to grayscale, save them, and repeat until we're done. after these steps, I used haarcascade_frontalface_default.xml to detect faces in the image and haarcascade_lowerbody_default.xml to detect human in the images cropped waist-down. and also I trained my own haarcascade classifier to detect upper body and it's not working well so far, I'm still working on it. and I will train it again on the images taken from imagenet but it will takes a couple of days to get access to download images. 
