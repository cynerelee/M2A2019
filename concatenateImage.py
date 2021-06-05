import cv2
import os
import numpy as np

# Path='G:\\MICCAI\\dataset 7\\keyframe_5\\data\\left_mask\\'
# savePath='G:\\MICCAI\\Data\\image\\'
# file=os.listdir(Path)
# file1=os.listdir(savePath)
# k=len(file1)
# for i in range(len(file)-2):
    
#     image1=cv2.imread(Path+str(i)+'.jpg')
#     image2 = cv2.imread(Path+str(i+1)+'.jpg')
#     image3 = cv2.imread(Path+str(i+2)+'.jpg')
#     image=np.concatenate((image1,image2,image3),axis=1)
#     cv2.imwrite(savePath+str(k)+'.jpg',image)
#     k=k+1
        #print(i,j)
    
def saveImage(Path,savePath):
    file=os.listdir(Path)
    file1=os.listdir(savePath)
    k=len(file1)
    start=k
    for i in range(len(file)-2):
        image1=cv2.imread(Path+str(i)+'_mask.jpg')
        image2 = cv2.imread(Path+str(i+1)+'_mask.jpg')
        image3 = cv2.imread(Path+str(i+2)+'_mask.jpg')
        image=np.concatenate((image1,image2,image3),axis=1)
        cv2.imwrite(savePath+str(k)+'_mask.jpg',image)
        k=k+1
    end=k-1
    print('Finish  ',Path,'  Total ',k, '编号：',start, ' To ',end)
saveImage('G:\\MICCAI\\dataset 5\\keyframe_4\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')
saveImage('G:\\MICCAI\\dataset 6\\keyframe_1\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')
saveImage('G:\\MICCAI\\dataset 6\\keyframe_2\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')
saveImage('G:\\MICCAI\\dataset 6\\keyframe_3\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')
saveImage('G:\\MICCAI\\dataset 6\\keyframe_4\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')
saveImage('G:\\MICCAI\\dataset 7\\keyframe_1\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')
saveImage('G:\\MICCAI\\dataset 7\\keyframe_2\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')
saveImage('G:\\MICCAI\\dataset 7\\keyframe_3\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')
saveImage('G:\\MICCAI\\dataset 7\\keyframe_4\\data\\left_mask\\','G:\\MICCAI\\Data\\mask\\')

# Path='G:\\MICCAI\\dataset 5\\keyframe_4\\data\\left_mask\\'
# savePath='G:\\MICCAI\\Data\\mask\\'
# file=os.listdir(Path)
# file1=os.listdir(savePath)
# k=len(file1)
# for i in range(len(file)-2):
    
#     image1=cv2.imread(Path+str(i)+'_mask.jpg')
#     image2 = cv2.imread(Path+str(i+1)+'_mask.jpg')
#     image3 = cv2.imread(Path+str(i+2)+'_mask.jpg')
#     image=np.concatenate((image1,image2,image3),axis=1)
#     cv2.imwrite(savePath+str(k)+'_mask.jpg',image)
#     k=k+1
# file1=os.listdir(savePath)
# print(len(file1))