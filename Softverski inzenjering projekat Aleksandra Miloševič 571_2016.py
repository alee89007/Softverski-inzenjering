import pydicom
#import os
import numpy as np
#import pandas as pd
import cv2
#import sys
#import scipy
#import argparse
#import matplotlib.pyplot as plt
#from matplotlib import pyplot, cm
#from matplotlib import colors
#from matplotlib.colors import hsv_to_rgb
#from pydicom.data import get_testdata_files
#from mpl_toolkits.mplot3d import Axes3D
#from PIL import Image



#putanja do slike


class RacunanjePovrsine(object):
    def __init__(self, ime):
        self.slika = ime
    def racunanje(self):
        filename = pydicom.dcmread(self.slika)
        n=0
        m=0
        k=200

        np.set_printoptions(threshold=np.inf)

       # p = filename.pixel_array
        for row in filename.pixel_array:
            for cell in row:
                n=n+1
        print(n)
        for row in filename.pixel_array:
            for cell in row:
                if cell>=k:
                    m=m+1
        print(m)
        print(m/n*100)

class Segmentiranje(object):
    def __init__(self, ime):
        self.slika = ime
    
    def bojenje(self):
    



        def DicomtoRGB(filename,bt,wt):
        
            img=np.array(filename.pixel_array, np.int16)
            clipped_img = np.clip(img,bt,wt)
        
            rgb_add = clipped_img - bt
        
            rgb_mult = np.multiply(rgb_add,255/(wt-bt))
        
            rgb_int = np.around(rgb_mult,0).astype(np.uint8)
        
            rgb_img = np.stack([rgb_int]*3,axis=-1)
            return rgb_img
        filename = pydicom.dcmread(slika)

        image=DicomtoRGB(filename,bt=0,wt=1400)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray", gray)
#cv2.waitKey(0)
#cv2.destroyWindow("gray")

#image[np.where((image >= [255,255,255]).all(axis = 2))] = [0,33,166]
#ref=0
        len=image.shape
        for a in range(0,len[0]):
            first=0
            last=0
            for b in range(0,int(len[1]/2)):
                if (first==0):
                    if (image[a,b]<=[250,250,250]).all() and (image[a,b+1]>[250,250,250]).all() and (image[a,b+2]>[250,250,250]).all() and (image[a,b+3]>[250,250,250]).all():
                        first=b+1
                if(first!=0):
                    if (image[a,b]>[250,250,250]).all() and (image[a,b+1]<=[250,250,250]).all():
                        last=b
            for i in range(first,last):
                image[a,i]=[0,33,166]

            first=0
            last=0
            for b in range(int(len[1]/2),len[1]-3):
                if (first==0):
                    if (image[a,b]<=[250,250,250]).all() and (image[a,b+1]>[250,250,250]).all() and (image[a,b+2]>[250,250,250]).all() and (image[a,b+3]>[250,250,250]).all():
                        first=b+1
                if(first!=0):
                    if (image[a,b]>[250,250,250]).all() and (image[a,b+1]<=[250,250,250]).all():
                        last=b
            for i in range(first,last):
                image[a,i]=[0,33,166]

        cv2.imwrite(slika+".jpg", image)

        print("Nova .JPG slika: "+slika+".jpg")
    
if __name__ == "__main__":
    print("unesite ime slike ili purtanju do slike!")
    slika=input()
    povrsina=RacunanjePovrsine(slika)
    povrsina.racunanje()
    novaSlika=Segmentiranje(slika)
    novaSlika.bojenje()