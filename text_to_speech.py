import easyocr
import cv2
import pytesseract
from gtts import gTTS
import os

from playsound import playsound


cuadro = 100
anchocam, altocam =640,480

reader = easyocr.Reader(["es", "en"], gpu=False)
cap = cv2.VideoCapture(0)
cap.set(3, anchocam)
cap.set(4, altocam)


def text(image):
    def voz(arch_text, lenguaje, nom_arch):
        with open(arch_text, "r") as lec:
            lectura = lec.read()
        lect = gTTS(text = lectura, lang = lenguaje, slow= False)
        nombre = nom_arch
        lect.save(nombre)
    
    #pytesseract.pytesseract.tesseract_cmd
    
    gris =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #texto = pytesseract.image_to_string(gris)
    texto= reader.readtext(image)
    for res in texto:
        print("result: ", res)
        pt0 = res[0][0]
        pt1 = res[0][1]
        pt2 = res[0][2]
        pt3 = res[0][3]

        cv2.rectangle(image, pt0, (pt1[0], pt1[1] - 23), (255,0,0),-1)
        cv2.putText(image, res[1], (pt0[0], pt0[1] -3),2, 0.8, (255,255,255),1)
        cv2.rectangle(image, pt0, pt2, (255,0,0),2)
        cv2.circle(image, pt0, 2, (255,0,0),2)
        cv2.circle(image, pt1, 2, (255,0,0),2)
        cv2.circle(image, pt2, 2, (255,0,0),2)
        cv2.circle(image, pt3, 2, (255,0,0),2)
       
    texto = str(texto)    
    print(texto)
    dire=open("Info.txt", "w")
    dire.write(texto)
    dire.close()
    
    


while True:
    ret, frame = cap.read()
    if ret == False:break
    cv2.putText(frame, 'coloque la imagen en el recuadro', (158,80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.71, (255,255,255,0), 2)
    cv2.putText(frame, 'coloque la imagen en el recuadro', (160,80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,0,0), 2)
    cv2.rectangle(frame, (cuadro,cuadro), (anchocam - cuadro, altocam - cuadro), (0,0,0), 2)
    x1, y1 = cuadro, cuadro
    ancho, alto = (anchocam - cuadro) - x1, (altocam - cuadro) -y1
    x2, y2 = ancho, y1 + alto
    doc = frame[y1:y2, x1:x2]
    cv2.imwrite("Imatext.jpg", doc)
    
    cv2.imshow("lector de documentos", frame)
    t = cv2.waitKey(1)
    if t == 27:
        break
        
text(doc)
cap.release()
cv2.destroyAllWindows()


