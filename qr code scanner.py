from cvzone import putTextRect
import time
from pyzbar.pyzbar import decode
import cv2
# img=cv2.imread('abc.png')
# code=decode(img)
# print(code)
# for barcode in decode(img):
#     # print(barcode.data)
#     text=barcode.data.decode('utf-8')
#     print(text)
#     print(type(text))
#     print(list(text))
#     r=barcode.rect
#     print(r)
    
#     cv2.imshow('img.',img)

#     cv2.waitKey(0)


cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    img=cv2.flip(img,1)
    code=decode(img)
    # print(code)
    if code:
        for barcode in decode(img):
            # print(barcode.data)
            text=barcode.data.decode('utf-8')
            print(text)
            password_start_index=text.find('P:')+2
            password_end_index=text.find(';H:')
            password=text[password_start_index:password_end_index]
            print(password)
            password=f"Code : {password} "
            r=barcode.rect
            cv2.rectangle(img,(r[0],r[1]),(r[0]+r[2],r[1]+r[3]),(255,150,200),5)
            cv2.putText(img,"press 'q' to scan code again!! ",(10,40),cv2.FONT_HERSHEY_TRIPLEX,1,(255,100,255),2)
            # putTextRect(img,password,(30,100),scale=2)
            putTextRect(img,password,(30,80),scale=1,colorT=(0,0,0),font=cv2.FONT_HERSHEY_TRIPLEX)
            putTextRect(img,"Press 's' for save image! ",(10,130),scale=1,colorB=(0,0,0),font=cv2.FONT_HERSHEY_TRIPLEX)

            if cv2.waitKey(1) & 0xFF ==ord('s'):
                t=time.time()
                cv2.imwrite(f'{t}.png',img)

            cv2.imshow("image",img)
            cv2.waitKey(0)

    else:
        cv2.putText(img,"Show QR code   ",(10,30),cv2.FONT_HERSHEY_TRIPLEX,1,(255,100,255),2)
        cv2.putText(img,"Press 'q' for exit !! ",(10,70),cv2.FONT_HERSHEY_TRIPLEX,1,(255,100,255),1)
        cv2.imshow("image",img)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
                     break
    
# cam.release()
# cv2.destroyAllWindows()

    