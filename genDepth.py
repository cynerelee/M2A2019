#coding=utf-8
from libtiff import TIFF
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
#import thread
import time
import cv2


def tiff2Stack(filePath):
    tif = TIFF.open(filePath,mode='r')
    stack = []
    for img in list(tif.iter_images()):
        stack.append(img)
    stack=np.array(stack)
    stack=stack[:,:1024,:,:]
    stack=np.reshape(stack,[1024,1280,3])
    #print('image',stack.shape)
    return  stack

def readRGB(imagePath):
    image=cv2.imread(imagePath)
    #print(image.shape)
    return image


def ExactDepth(filePath):
    tif = TIFF.open(filePath,mode='r')
    stack = []
    for img in list(tif.iter_images()):       
        depth=img[:,:,2]
        depth=depth[:1024,:]
        stack.append(depth)
    stack=np.array(stack)   
    stack=stack.reshape(stack.shape[1],stack.shape[2])
    #print(stack.shape)      
    return  stack

xyz=tiff2Stack("D:\data\dataset 1\keyframe_1\data\scene_points\scene_points\scene_points000002.tiff")
imagePath="D:\data\dataset 1\keyframe_1\data\left_image\\2.jpg"
rgb=readRGB(imagePath)
xyz=np.reshape(xyz,[-1,3])
mask = np.all(np.equal(xyz, 0), axis=1)
#print(xyz[~mask].shape)

rgb=np.reshape(rgb,[-1,3])
def encode_rgb_for_pcl(rgb):
    a=rgb
    rgb[:,0]=a[:,2]
    rgb[:,2]=a[:,0]
    

    """ Encode bit-packed RGB for use with PCL.
    :param rgb: Nx3 uint8 array with RGB values.
    :rtype: Nx1 float32 array with bit-packed RGB, for PCL.
    """
    assert(rgb.dtype == np.uint8)
    assert(rgb.ndim == 2)
    assert(rgb.shape[1] == 3)
    rgb = rgb.astype(np.uint32)
    rgb = np.array((rgb[:, 0] << 16) | (rgb[:, 1] << 8) | (rgb[:, 2] << 0),
                   dtype=np.uint32)
    rgb.dtype = np.float32
    rgb=np.reshape(rgb,[-1,1])
    return rgb
#rgb=encode_rgb_for_pcl(rgb)
a=rgb
rgb[:,0]=a[:,2]
rgb[:,2]=a[:,0]

#print(rgb.shape)
xyzrgb=np.concatenate((xyz,rgb),axis=1)
np.savetxt('2.txt',xyzrgb)
#print(xyzrgb[~mask].shape)
# f=open('1.pcd','w')
# f.write('# .PCD v.7 - Point Cloud Data file format\n')
# f.write('VERSION .7\n')
# f.write('FIELDS x y z rgb\n')
# f.write('SIZE 4 4 4 4\n')
# f.write('TYPE F F F U\n')
# f.write('WIDTH '+str(xyzrgb[~mask].shape[0])+'\n')
# f.write('HEIGHT 1\n')
# f.write('VIEWPOINT 0 0 0 1 0 0 0\n')
# f.write('POINTS '+str(xyzrgb[~mask].shape[0])+'\n')
# f.write('DATA ascii\n')
# xyzrgb=xyzrgb[~mask]
# for i in range(len(xyzrgb)):
#     f.write(str(xyzrgb[i][0])+' '+str(xyzrgb[i][1])+' '+str(xyzrgb[i][2])+' '+str(xyzrgb[i][3])+'\n')
#     #f.write(str(int(xyzrgb[i][4]))+' '+str(int(xyzrgb[i][3]))+'\n')
# f.close()


#np.savetxt('001.txt',xyzrgb)



# depth=ExactDepth("/media/cynere/ubuntu/MICCAI/dataset 1/keyframe_3/data/scenre_points/scene_points000001.tiff")

# print(depth.shape)
def saveDepth(threadName,tifpath,depthpath):
    if not os.path.exists(depthpath):
        os.makedirs(depthpath)
    fileNames=os.listdir(tifpath)
    for file in fileNames:
        filePath=tifpath+file
        depth=ExactDepth(filePath)
        depthPath=depthpath+str(int(file.split('.')[0][12:]))+'.npy'
        #print "%s: %s" % ( threadName, time.ctime(time.time()) )
        np.save(depthPath,depth)
    print('end'+threadName+tifpath)



# 创建两个线程
# try:
#     thread.start_new_thread( saveDepth, ("Thread-1", "/media/cynere/ubuntu/MICCAI/dataset 5/keyframe_1/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 5/keyframe_1/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-2", "/media/cynere/ubuntu/MICCAI/dataset 5/keyframe_2/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 5/keyframe_2/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-3", "/media/cynere/ubuntu/MICCAI/dataset 5/keyframe_3/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 5/keyframe_3/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-4", "/media/cynere/ubuntu/MICCAI/dataset 5/keyframe_4/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 5/keyframe_4/data/depth/" ) )

#     thread.start_new_thread( saveDepth, ("Thread-1", "/media/cynere/ubuntu/MICCAI/dataset 6/keyframe_1/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 6/keyframe_1/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-2", "/media/cynere/ubuntu/MICCAI/dataset 6/keyframe_2/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 6/keyframe_2/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-3", "/media/cynere/ubuntu/MICCAI/dataset 6/keyframe_3/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 6/keyframe_3/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-4", "/media/cynere/ubuntu/MICCAI/dataset 6/keyframe_4/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 6/keyframe_4/data/depth/" ) )

#     thread.start_new_thread( saveDepth, ("Thread-1", "/media/cynere/ubuntu/MICCAI/dataset 7/keyframe_1/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 7/keyframe_1/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-2", "/media/cynere/ubuntu/MICCAI/dataset 7/keyframe_2/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 7/keyframe_2/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-3", "/media/cynere/ubuntu/MICCAI/dataset 7/keyframe_3/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 7/keyframe_3/data/depth/" ) )
#     thread.start_new_thread( saveDepth, ("Thread-4", "/media/cynere/ubuntu/MICCAI/dataset 7/keyframe_4/data/scenre_points/","/media/cynere/ubuntu/MICCAI/dataset 7/keyframe_4/data/depth/" ) )
# except:
#    print "Error: unable to start thread"
 
# while 1:
#    pass

# tifpath="/media/cynere/ubuntu/MICCAI/dataset 1/keyframe_1/data/scene_points/scene_points/"
# depthpath="/media/cynere/ubuntu/MICCAI/dataset 1/keyframe_1/data/depth/"
# if not os.path.exists(depthpath):
#     os.makedirs(depthpath)
# fileNames=os.listdir(tifpath)
# for file in fileNames:
#     filePath=tifpath+file
#     depth=ExactDepth(filePath)
#     depthPath=depthpath+str(int(file.split('.')[0][12:]))+'.npy'
#     #print(depthpath)
#     np.save(depthPath,depth)
