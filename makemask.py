import cv2
import numpy as np
import os
def RGB2HSI(rgb_img,gray):

    #保存原始图像的行列数
    row = np.shape(rgb_img)[0]
    col = np.shape(rgb_img)[1]
    
    hsi_img = rgb_img.copy()
    #对图像进行通道拆分
    B,G,R = cv2.split(rgb_img)
    Bg,Gg,Rg=cv2.split(rgb_img)
    #把通道归一化到[0,1]
    [B,G,R] = [ i/ 255.0 for i in ([B,G,R])]
    H = np.zeros((row, col))    #定义H通道
    I = (R + G + B) / 3.0       #计算I通道
    S = np.zeros((row,col))      #定义S通道
    for i in range(row):
        den = np.sqrt((R[i]-G[i])**2+(R[i]-B[i])*(G[i]-B[i]))
        thetha = np.arccos(0.5*(R[i]-B[i]+R[i]-G[i])/den)   #计算夹角
        h = np.zeros(col)               #定义临时数组
        #den>0且G>=B的元素h赋值为thetha
        h[B[i]<=G[i]] = thetha[B[i]<=G[i]]
        #den>0且G<=B的元素h赋值为thetha
        h[G[i]<B[i]] = 2*np.pi-thetha[G[i]<B[i]]
        #den<0的元素h赋值为0
        h[den == 0] = 0
        H[i] = h/(2*np.pi)      #弧度化后赋值给H通道
    #计算S通道
    for i in range(row):
        min = []
       
        for j in range(col):
            arr = [B[i][j],G[i][j],R[i][j]]
            min.append(np.min(arr))
        min = np.array(min)
        #计算S通道
        S[i] = 1 - min*3/(R[i]+B[i]+G[i])
        
        S[i][R[i]+B[i]+G[i] == 0] = 0
   


    hsi_img[:,:,0] = H*255



    hsi_img[:,:,1] = S*255
    hsi_img[:, :, 2] = I * 255

    for a in range(hsi_img[:,:,1].shape[0]):
        for b in range(hsi_img[:,:,1].shape[1]):
            if hsi_img[:,:,1][a][b]<=25 and hsi_img[:,:,2][a][b]>=200:
                B[a][b]=B[a][b]
                G[a][b]=G[a][b]
                R[a][b]=R[a][b]
            else:
                B[a][b]=0
                G[a][b]=0
                R[a][b]=0

    #
    #
    # newrgb=cv2.merge([B,G,R])
    # cv2.imshow('image',newrgb)
    #
    #

    gray = gray.astype("float")
    # row, column = gray.shape
    # gradient = np.zeros((row, column))

    scharrx = cv2.Sobel(gray, cv2.CV_64F, dx=1, dy=0)
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.Sobel(gray, cv2.CV_64F, dx=0, dy=1)
    scharry = cv2.convertScaleAbs(scharry)
    result = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    row, column = result.shape



    for w in range(row):
        for x in range(column):
            if result[w][x] > 200:
                Bg[w][x] = Bg[w][x]
                Gg[w][x] = Gg[w][x]
                Rg[w][x] = Rg[w][x]
            else:
                Bg[w][x] = 0
                Gg[w][x] = 0
                Rg[w][x] = 0


    newnewrgb=cv2.merge([Bg,Gg,Rg])
    # cv2.imshow('images',newnewrgb)

    # cv2.imwrite(r'C:\Users\moon\Desktop\dataarrange\data(370)\2remain2\20151216009\6.jpg',newnewrgb)
    for a in range(row):
        for b in range(column):
            # 制作黑彩掩膜
            # if B[a][b]!=0 and Bg[a][b]==0:
            #     Bg[a][b] = B[a][b]*255
            #     print(B[a][b])
            # if G[a][b]!=0 and Gg[a][b]==0:
            #     Gg[a][b] = G[a][b]*255
            # if R[a][b]!=0 and Rg[a][b]==0:
            #     Rg[a][b] = R[a][b]*255


            # 制作黑白掩膜
            # if B[a][b]!=0 and Bg[a][b]==0:
            #     Bg[a][b] = 255
            #    # print(B[a][b])
            #
            # elif B[a][b]==0 and Bg[a][b]!=0:
            #     Bg[a][b] = 255
            #
            # elif B[a][b]!=0 and Bg[a][b]!=0:
            #     Bg[a][b] = 255
            #
            # if G[a][b] != 0 and Gg[a][b] == 0:
            #     Gg[a][b] = 255
            #    # print(G[a][b])
            #
            # elif G[a][b] == 0 and Gg[a][b] != 0:
            #     Gg[a][b] = 255
            #
            # elif G[a][b] != 0 and Gg[a][b] != 0:
            #     Gg[a][b] = 255
            #
            # if R[a][b] != 0 and Rg[a][b] == 0:
            #     Rg[a][b] = 255
            #    # print(R[a][b])
            #
            # elif R[a][b] == 0 and Rg[a][b] != 0:
            #     Rg[a][b] = 255
            #
            # elif R[a][b] != 0 and Rg[a][b] != 0:
            #     Rg[a][b] = 255

            # 制作白黑掩膜
            if B[a][b]!=0 and Bg[a][b]==0:
                Bg[a][b] = 0
                #print(B[a][b])

            elif B[a][b]==0 and Bg[a][b]!=0:
                Bg[a][b] = 0

            elif B[a][b]!=0 and Bg[a][b]!=0:
                Bg[a][b] = 0
            else:
                Bg[a][b] = 255

            if G[a][b] != 0 and Gg[a][b] == 0:
                Gg[a][b] = 0
                #print(G[a][b])

            elif G[a][b] == 0 and Gg[a][b] != 0:
                Gg[a][b] = 0

            elif G[a][b] != 0 and Gg[a][b] != 0:
                Gg[a][b] = 0

            else:
                Gg[a][b] = 255

            if R[a][b] != 0 and Rg[a][b] == 0:
                Rg[a][b] = 0
                #print(R[a][b])

            elif R[a][b] == 0 and Rg[a][b] != 0:
                Rg[a][b] = 0

            elif R[a][b] != 0 and Rg[a][b] != 0:
                Rg[a][b] = 0
            else:
                Rg[a][b] = 255




    newnewnewrgb=cv2.merge([Bg,Gg,Rg])
    # cv2.imshow('imagesss',newnewnewrgb)
    # cv2.imwrite(r'C:\Users\moon\Desktop\dataarrange\data(370)\2remain2\20151230009\imagesssss.jpg',newnewnewrgb)



    return newnewnewrgb



if __name__ == '__main__':

    img_path=r'G:\\MICCAI\\dataset 6\\keyframe_1\\data\\left_image\\'
   # image_save_path = r'D:\python\code\image_new\\'
    mask_save_path=r'G:\\MICCAI\\dataset 6\\keyframe_1\\data\\left_mask\\'
    if not os.path.isdir(mask_save_path):
        os.mkdir(mask_save_path)
    imageNames=os.listdir(img_path)
    len=len(imageNames)
    i=0
    for imageName in imageNames:
        i=i+1
        if(i%10==0):
            print("在处理第"+str(i)+"   共"+str(len))
        if not ".jpg" in imageName:
            continue

        imagePath=img_path+imageName
        rgb_lwpImg=cv2.imread(imagePath)
        gray = cv2.cvtColor(rgb_lwpImg, cv2.COLOR_BGR2GRAY)
        mask = RGB2HSI(rgb_lwpImg, gray)
        #cv2.imwrite(image_save_path+imageName,rgb_lwpImg)
        cv2.imwrite(mask_save_path+imageName[:-4]+"_mask.jpg",mask)

        

    # patients=os.listdir(img_path)
    # for i in range(len(patients)):
    #    #image_path=img_path
    #     images=os.listdir(img_path+'\\'+patients[i])
    #     for j in range(len(images)):
    #         rgb_lwpImg=cv2.imread(img_path+'/'+patients[i]+'/'+images[j])
    #         gray = cv2.cvtColor(rgb_lwpImg, cv2.COLOR_BGR2GRAY)
    #         mask = RGB2HSI(rgb_lwpImg, gray)

    #         cv2.imwrite(image_save_path+'/'+str(i)+'.jpg',rgb_lwpImg)

    #         cv2.imwrite(mask_save_path+'/'+str(i)+'.jpg',mask)




    # key = cv2.waitKey(0) & 0xFF
    # cv2.destroyAllWindows()
