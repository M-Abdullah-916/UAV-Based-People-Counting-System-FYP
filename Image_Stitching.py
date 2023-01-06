import Utils
import matplotlib.pyplot as plt
import Extract_Keypoints

def stichImages(imagesPath):
    # getting Images
    Image_List = Utils.loadImages(imagesPath)
    # Plotting Final Stitched Image
    plt.figure(figsize=(10, 10))
    plt.title('Image After Collation')
    plt.imshow(Extract_Keypoints.extractKeypoints(Image_List))
    plt.show()
