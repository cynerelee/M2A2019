import numpy as np
import os
import math
import json
def RTorxryrz(R):  # 单位:rad弧度
    rx = math.atan2(R[2, 1], R[2, 2])
    ry = math.atan2(-R[2, 0], math.sqrt(R[2, 1] * R[2, 1] + R[2, 2] * R[2, 2]))
    rz = math.atan2(R[1, 0], R[0, 0])
    return rx, ry, rz
def ReturnOula(T):
    #根据T得出rx,ry,rz,tx,ty,tz
    R=T[:3,:3]
    rx,ry,rz=RTorxryrz(R)
    tx,ty,tz=T[0,3],T[1,3],T[1,3]
    return rx,ry,rz,tx,ty,tz
def TAB(T):
    #根据A->B的T，得出B->A的rx,ry,rz,tx,ty,tz
    R=T[:3,:3]
    t=T[:3,3]
    newR=R.T
    newt=R.T*(t.T)
    rx,ry,rz=RTorxryrz(newR)
    tx,ty,tz=newt[0,3],newt[1,3],newt[2,3]
    return rx,ry,rz,tx,ty,tz

def loadCamerapose(Path):
    f = open(Path, encoding='utf-8')  # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    data = setting['camera-pose']
    data = np.array(data)
    #rotation = data[:3, :3]
    return data
def ConvertNum(i):
    if i<10:
        j='00000'+str(i)
    elif i<100:
        j='0000'+str(i)
    elif i<1000:
        j='000'+str(i)
    elif i<10000:
        j='00'+str(i)
    elif i<100000:
        j='0'+str(i)
    else:
        j=str(i)
    return j
# Path = "D:\\data\\dataset 6\\keyframe_2\\data\\frame_data\\"
# FileName=os.listdir(Path)
# len=len(FileName)
# f=open('D:\\data\\cameramotion\\62.txt','w')
# for i in range(len-1):
#     filePath1=Path+'frame_data'+ConvertNum(i)+'.json'
#     filePath2=Path+'frame_data'+ConvertNum(i+1)+'.json'
#     T1 = np.matrix(loadCamerapose(filePath1))
#     T2 = np.matrix(loadCamerapose(filePath2))
#     T=T1.I*T2   
#     rx,ry,rz,tx,ty,tz=ReturnOula(T)
#     rx1,ry1,rz1,tx1,ty1,tz1=ReturnOula(T)
#     f.write(str(rx)+' '+str(ry)+' '+str(rz)+' '+str(tx)+' '+str(ty)+' '+str(tz)+" ")
#     f.write(str(rx1)+' '+str(ry1)+' '+str(rz1)+' '+str(tx1)+' '+str(ty1)+' '+str(tz1))
#     f.write('\n')
# f.close()

for j in range(2,8):
    for k in range(1,5):
        Path = "D:\\data\\dataset "+str(j)+"\\keyframe_"+str(k)+"\\data\\frame_data\\"
        FileName=os.listdir(Path)
        len1=len(FileName)
        txtPath="D:\\data\\cameramotion13\\"+str(j)+str(k)+'.txt'
        f=open(txtPath,'w')
        for i in range(len1-2):
            filePath1=Path+'frame_data'+ConvertNum(i)+'.json'
            filePath2=Path+'frame_data'+ConvertNum(i+2)+'.json'
            T1 = np.matrix(loadCamerapose(filePath1))
            T2 = np.matrix(loadCamerapose(filePath2))
            T=T1.I*T2   
            rx,ry,rz,tx,ty,tz=ReturnOula(T)
            rx1,ry1,rz1,tx1,ty1,tz1=ReturnOula(T)
            f.write(str(rx)+' '+str(ry)+' '+str(rz)+' '+str(tx)+' '+str(ty)+' '+str(tz)+" ")
            f.write(str(rx1)+' '+str(ry1)+' '+str(rz1)+' '+str(tx1)+' '+str(ty1)+' '+str(tz1))
            f.write('\n')
        f.close()
        print("finish:"+str(j)+str(k)+'\n')
    



# for file in FileName:
#     T1 = loadRotation(file)




# a=np.array([[1,0,0,0],
# [0,1,0,0],
# [0,0,1,0],
# [0,0,0,1]])
# b=np.array([[0.9999977407167917,0.0017023722178253205,-0.0006537000616405157,-0.077089417409411],
# [-0.0017007895288109957,0.9999976276181592,0.0008216550578390506,0.09702463654309668],
# [0.0006552416195081496,-0.0008206237309850348,0.999998449986963,-0.07521725298624915],
# [0,0,0,1]])
# c=np.array([[0.999972685454456,
#             -0.007366816699442634,
#             -0.0005403196678863263,
#             -0.06916507615963496],
# [0.007365277277705762,
#             0.9999688891286629,
#             -0.0026596894668772823,
#             -0.3405672375248514],
# [ 0.0005598823680102017,
#             0.0026558851296978165,
#             0.9999961776598996,
#             0.9260814331971687],
# [0,0,0,1]])


# B = np.matrix(b)
# C=np.matrix(c)
# d=B.I*C
# print(d)

    
