import cv2
import os
import numpy as np

def saveImage(Path,savePath):
    file=os.listdir(Path)
    file1=os.listdir(savePath)
    k=len(file1)
    start=k
    for i in range(len(file)-2):
        image1=cv2.imread(Path+str(i)+'.jpg')
        image2 = cv2.imread(Path+str(i+1)+'.jpg')
        image3 = cv2.imread(Path+str(i+2)+'.jpg')
        image=np.concatenate((image1,image2,image3),axis=1)
        cv2.imwrite(savePath+str(k)+'.jpg',image)
        k=k+1
    end=k-1
    print('Finish  ',Path,'  Total ',k, '编号：',start, ' To ',end)
saveImage('G:\\MICCAI\\dataset 1\\keyframe_1\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 1\\keyframe_2\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 1\\keyframe_3\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 2\\keyframe_1\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 2\\keyframe_2\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 2\\keyframe_3\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 2\\keyframe_4\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 3\\keyframe_1\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 3\\keyframe_2\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 3\\keyframe_3\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 3\\keyframe_4\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 4\\keyframe_1\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 4\\keyframe_2\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 4\\keyframe_3\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 4\\keyframe_4\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 5\\keyframe_1\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 5\\keyframe_2\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 5\\keyframe_3\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 5\\keyframe_4\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 6\\keyframe_1\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 6\\keyframe_2\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 6\\keyframe_3\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 6\\keyframe_4\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 7\\keyframe_1\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 7\\keyframe_2\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 7\\keyframe_3\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
saveImage('G:\\MICCAI\\dataset 7\\keyframe_4\\data\\left_image\\','G:\\MICCAI\\Data\\image1\\')
# Path='G:\\MICCAI\\dataset 1\\keyframe_1\\data\\left_image\\'
# savePath='G:\\MICCAI\\Data\\image1\\'
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
# file1=os.listdir(savePath)
# print(len(file1))
        #print(i,j)
    

# Path='G:\\MICCAI\\dataset 5\\keyframe_2\\data\\left_mask\\'
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
