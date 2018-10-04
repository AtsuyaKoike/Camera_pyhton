import os
import cv2

path = 'num.txt'

if ( os.path.exists(path) == False ):
    f = open('num.txt', 'w')
    f.write('0')
    f.close()

f = open('num.txt', 'r')
i = int(f.readlines()[0])
f.close()

print(i)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

directory = 'pic'
extension = '.jpeg'


f = open('num.txt', 'w')
while(True):
    ret, frame = capture.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        i += 1
        picture = directory + str(i) + extension
        cv2.imwrite(picture, frame)
        cv2.waitKey(1)
    elif cv2.waitKey(1) & 0xFF == ord('z'):
        break;
       
capture.release()
cv2.destroyAllWindows()
f.write(str(i))
