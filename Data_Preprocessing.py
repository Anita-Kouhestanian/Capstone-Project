import json
import cv2
import urllib.request

f = open('anine_bing_anine_bing-2021-04-13--16-45-16.json')
data = json.load(f)
# getting all urls
urls = []
for sample in range(len(data)):
    data_dict = dict(data[sample])
    if data_dict['image'] is not None and data_dict['images'] is not None:
        for element in data_dict['image'].keys():
            if element == 'src':
                urls.append(data_dict['image'][element])
        for number in range(len(data_dict['images'])):
            for el in data_dict['images'][number].keys():
                if el == 'src':
                    urls.append(data_dict['images'][number][el])


# Downloading the images and resize them and converting them to grayscale
pic_num = 1
for i in urls:
    try:
        print(i)
        urllib.request.urlretrieve(i, "image" + str(pic_num) + ".jpg")
        img = cv2.imread("image" + str(pic_num) + ".jpg", cv2.IMREAD_UNCHANGED)
        cv2.imwrite("image" + str(pic_num) + ".jpg", img)
        scale_percent = 30  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
