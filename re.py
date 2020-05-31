# import cv2
# # print(cv2.__version__)
# cap = cv2.VideoCapture()
# # Check if the webcam is opened correctly
# # if not cap.isOpened():
# #     cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     # raise IOError("Cannot open webcam")
#     cap.open

# while True:
#     ret,frame = cap.read()

#     cv2.imshow('Original video',frame)

#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break


# cap.release()
# cv2.destroyAllWindows()
#         # plt.figure()
#         # cap = cv2.VideoCapture()

        
#         # ret, frame = cap.read()
#         # if not ret:
#         #     break
#         # facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#         # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
#         # canvas = np.zeros((250, 300, 3), dtype="uint8")
#         # for (x, y, w, h) in faces:
#         #     draw_Rounded_Corners(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2,15, 10) 
#         #     roi_gray = gray[y:y + h, x:x + w]
#         #     cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
#         #     prediction = model.predict(cropped_img)
#         #     maxindex = np.argmax(prediction)
#         #     cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
#         #     objects = (['Angry', 'Disgusted', 'Fearful', 'Happy', 'Neutral', 'Sad','Surprised'])
#         #     index = np.arange(len(objects))
#         #     MakingPositive=lambda a: (abs(a)+a)/2
#             # plt.barh(objects, MakingPositive(prediction[0]),color='orange')
#         # plt.xlabel('Predictions')
#         # plt.title('Emotion Percentage')
#         # plt.plot()
#         # plt.draw()
#         # plt.pause(0.05)
#         # plt.clf()
#         # cv2.imshow('Face Emotion Detection')
        
#         # if cv2.waitKey(1) & 0xFF == ord('q'):
#         #      break
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#do some ops

cap.release()
cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()