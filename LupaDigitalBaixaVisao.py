# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:29:13 2019

@author: Heron
"""

import cv2

cv2.setNumThreads(4)
camera = cv2.VideoCapture(1,cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
camera.set(cv2.CAP_PROP_FPS,30)
camera.set(cv2.CAP_PROP_AUTOFOCUS,True)
zoomX = 16


def trataImagem(imagem):
    imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
#    cv2.imshow('ImagemCinza',imagemCinza)
    return imagemCinza;

def retornaZoom(frame,zoom=5,wRef=40,hRef=20):
    height,width, = frame.shape[:2]
    meioX = round(width/2)
    meioY = round(height/2)
    x0 = meioX-wRef
    y0 = meioY-hRef
    x1 = meioX+wRef
    y1 = meioY+hRef
#    cv2.rectangle(frame,(x0,y0),(x1,y1),(255,0,255),1)
#    cv2.imshow('Teste',frame)
    imagemRoi = frame[y0:y1,x0:x1]
    heightRoi, widthRoi = imagemRoi.shape[:2]
    imagemZoom = cv2.resize(imagemRoi,(widthRoi*zoom,heightRoi*zoom), interpolation = cv2.INTER_BITS2)
#    cv2.imshow('ImagemZoom',imagemZoom)
    return imagemZoom
    
    
while(camera.isOpened()):
    isCaptura,imagemCaptura = camera.read()
    
    if(isCaptura):
        imagemZoom = retornaZoom(imagemCaptura,zoomX)
        imagemTratada = trataImagem(imagemZoom)
        
    
        cv2.imshow('Zoom',imagemCaptura)
        cv2.setWindowProperty('Zoom',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == ord('q'):
        camera.release()
        cv2.destroyAllWindows()
        break