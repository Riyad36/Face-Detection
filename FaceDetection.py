import cv2

def generate_dataset(img, id, img_id):
    cv2.imwrite("data/user."+str(id)+"."+str(img_id)+".jpg", img)


def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text ,clf):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []

    for (x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        id, _ = clf.predict(gray_img[y:y+h, x:x+w])

        if id == 1:
            cv2.putText(img, "Riyad", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        else:
            cv2.putText(img, "Unknown", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]

    return coords


def recognize(img, clf, faceCascade):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}

    coords = draw_boundary(img, faceCascade, 1.1, 10, color["green"], "Face", clf)
    return img




def detect(img, faceCascade, eyeCascade, noseCascade, img_id):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
    coords= draw_boundary(img, faceCascade, 1.1, 10, color['green'],"Face")

    if len(coords) == 4:

        roi_img = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]]
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)


        # coords = draw_boundary(roi_img, eyeCascade, 1.1, 10, color['red'], "Eye")
        # coords = draw_boundary(roi_img, noseCascade, 1.1, 5, color['blue'], "Nose")
        #coords = draw_boundary(roi_img, mouthCascade, 1.1, 20, color['white'], "Mouse") #mouth paitese na

    return  img


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
noseCascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")
#mouthCascade = cv2.CascadeClassifier("Mouth2.xml")


clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")


camera_port = 0
camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)

img_id = 0

while True:
    _, img = camera.read()
    #img = detect(img, faceCascade, eyeCascade, noseCascade, img_id)
    img = recognize(img, clf, faceCascade)
    cv2.imshow("face detection", img)
    img_id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()