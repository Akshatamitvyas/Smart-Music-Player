import imutils
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import vlc
import time
player1=vlc.MediaPlayer(r'C:\Users\akshat vyas\Desktop\songs\Tum Saath Ho.mp3')
player2=vlc.MediaPlayer(r'C:\Users\akshat vyas\Desktop\songs\Ve Maahi.mp3')
player3=vlc.MediaPlayer(r'C:\Users\akshat vyas\Desktop\songs\Bhaag Milkha bhaag.mp3')
player4=vlc.MediaPlayer(r'C:\Users\akshat vyas\Desktop\songs\De De Jagah.mp3')
player5=vlc.MediaPlayer(r'C:\Users\akshat vyas\Desktop\songs\O Rangrez.mp3')
player6=vlc.MediaPlayer(r'C:\Users\akshat vyas\Desktop\songs\Apna Time Aayega.mp3')
player7=vlc.MediaPlayer(r'C:\Users\akshat vyas\Desktop\songs\Mann Ki Lagan.mp3')
fd=cv2.CascadeClassifier(r'C:\Users\akshat vyas\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
model=load_model(r'C:\Users\akshat vyas\Desktop\ML\_mini_XCEPTION.106-0.65.hdf5')
v=cv2.VideoCapture(0)
em=['angry','disgust','fear','happy','sad','surprised','neutral']
count=0
c=0
d=0
while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(j)
    l=len(f)
    t1=c
    t2=d
    if(l>0):
        for [x,y,w,h] in f:
            cv2.rectangle(i,(x,y),(x+w,y+h),(0,200,255),2)
            c=w
            d=h
            roi=j[y:y+h,x:x+w]
            roi=cv2.resize(roi,(48,48))
            roi=roi.astype('float')/255.0
            roi=img_to_array(roi)
            roi=np.expand_dims(roi,axis=0)
            p=list(model.predict(roi)[0])
            #print(p)
            t=em[p.index(max(p))]
            #print(t)
            cv2.imshow("My Camera",i)
            k=cv2.waitKey(5)
            if k==ord('q'):
                cv2.destroyAllWindows()
                player1.stop()
                player2.stop()
                player3.stop()
                player4.stop()
                player5.stop()
                player6.stop()
                player7.stop()
                break
            
            if(t==em[0]):
                print(t)
                player1.play()
                
                if l==0 and count==1:
                    player1.pause()
                    count=0
                elif l!=0:
                    player1.play()
                    
                    count=1
                    if t1>w and t2>h:
                        player1.audio_set_volume(50)
                        player1.play()
                       
                        count = 1
                    elif t1<w and t2<h:
                        player1.audio_set_volume(100)
                        player1.play()
                        count = 1
                        time.sleep(180)
                        player1.stop()
                        break
            elif(t==em[1]):
                print(t)
                player2.play()
                
                if l==0 and count==1:
                    player2.pause()
                    count=0
                elif l!=0:
                    player2.play()
                    
                    count=1
                    if t1>w and t2>h:
                        player2.audio_set_volume(50)
                        player2.play()
                        
                        count = 1
                    elif t1<w and t2<h:
                        player2.audio_set_volume(100)
                        player2.play()
                        count = 1
                        time.sleep(180)
                        player2.stop()
                        break
            elif(t==em[2]):
                print(t)
                player3.play()
                
                if l==0 and count==1:
                    player3.pause()
                    
                    count=0
                elif l!=0:
                    player3.play()
                    
                    count=1
                    if t1>w and t2>h:
                        player3.audio_set_volume(50)
                        player3.play()
                        
                        count = 1
                    elif t1<w and t2<h:
                        player3.audio_set_volume(100)
                        player3.play()
                        
                        count = 1
                        time.sleep(180)
                        player3.stop()
                        break
            elif(t==em[3]):
                print(t)
                player4.play()
                
                if l==0 and count==1:
                    player4.pause()
                    count=0
                elif l!=0:
                    player4.play()
                    
                    count=1
                    if t1>w and t2>h:
                        player4.audio_set_volume(50)
                        player4.play()
                        
                        count = 1
                    elif t1<w and t2<h:
                        player4.audio_set_volume(100)
                        player4.play()
                        
                        count = 1
                        time.sleep(180)
                        player4.stop()
                        break
            elif(t==em[4]):
                print(t)
                player5.play()
                
                if l==0 and count==1:
                    player5.pause()
                    count=0
                elif l!=0:
                    player5.play()
                    
                    count=1
                    if t1>w and t2>h:
                        player5.audio_set_volume(50)
                        player5.play()
                        
                        count = 1
                    elif t1<w and t2<h:
                        player5.audio_set_volume(100)
                        player5.play()
                        
                        count = 1
                        time.sleep(180)
                        player5.stop()
                        break
            elif(t==em[5]):
                print(t)
                player6.play()
                
                if l==0 and count==1:
                    player6.pause()
                    count=0
                elif l!=0:
                    player6.play()
                    
                    count=1
                    if t1>w and t2>h:
                        player6.audio_set_volume(50)
                        player6.play()
                        
                        count = 1
                    elif t1<w and t2<h:
                        player6.audio_set_volume(100)
                        player6.play()
                        
                        count = 1
                        time.sleep(180)
                        player6.stop()
                        break
            elif(t==em[6]):
                print(t)
                player7.play()
                
                if l==0 and count==1:
                    player7.pause()
                    count=0
                elif l!=0:
                    player7.play()
                    
                    count=1
                    if t1>w and t2>h:
                        player7.audio_set_volume(50)
                        player7.play()
                        
                        count = 1
                    elif t1<w and t2<h:
                        player7.audio_set_volume(100)
                        player7.play()
                        
                        count = 1
                        time.sleep(180)
                        player7.stop()
                        break
