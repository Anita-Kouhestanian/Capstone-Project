import cv2
import urllib.request
import json

f = open('anine_bing_anine_bing-2021-04-13--16-45-16.json')
data = json.load(f)
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

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
low_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lowerbody.xml')
upper_cascade = cv2.CascadeClassifier('own_upper_body.xml')

pic_num = 1
for i in urls:
    try:
        print(i)
        urllib.request.urlretrieve(i, "image" + str(pic_num) + ".jpg")
        img = cv2.imread("image" + str(pic_num) + ".jpg", cv2.IMREAD_UNCHANGED)
        scale_percent = 30  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        # locate the exact features in the face
        faces = face_cascade.detectMultiScale(gray, 1.0485258, 6)
        for (x, y, w, h) in faces:
            cv2.rectangle(resized, (x, y), (x + w, y + h), (127, 0, 255), 2)

            cv2.imshow('img', resized)
            cv2.waitKey(0)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)

        low = low_cascade.detectMultiScale(gray, 1.1, 3)
        for (x, y, w, h) in low:
            cv2.rectangle(img, (x, y), (x + w, y + h), (12, 150, 100), 2)
        upper = upper_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in upper:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('img', img)
        cv2.waitKey(0)

        if faces is () and low is () and upper is ():
            print("No Human Found")
            pic_num += 1
    except Exception as e:
        print(str(e))

    cv2.destroyAllWindows()