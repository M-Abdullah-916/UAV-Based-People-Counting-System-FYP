import glob  #We can use the function glob.glob() or glob.iglob() directly from glob module to retrieve paths recursively from inside the directories/files and subdirectories/subfiles.
import cv2

def loadImages(imagesPath):
    path = sorted(glob.glob(imagesPath + "/*.jpg"))
    Image_List = []
    for Image in path:
        n = cv2.imread(Image)
        Image_List.append(n)
    return Image_List
