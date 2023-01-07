import Utils
import matplotlib.pyplot as plt
import Extract_Keypoints


class stichImages:
    def __init__(self, imagesPath):
        self.imagesPath = imagesPath

    def stiching(self):
        # getting Images
        Image_List = Utils.loadImages(self.imagesPath)
        # Plotting Final Stitched Image
        plt.figure(figsize=(10, 10))
        plt.title('Image After Collation')
        plt.imshow(Extract_Keypoints.extractKeypoints(Image_List))
        plt.show()
