import Image_Enhancement
import Utils
import Extract_Keypoints
from matplotlib import pyplot as plt
import cv2


def adapt_image_to_color_scale(image, color_scale):
    color = None
    if (color_scale != 'gray'):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        color = "gray"
    return image, color



class ImageCollation:
    def __init__(self, images_path):
        self.imagesPath = images_path

    def stitching(self):
        # getting Images
        image_loading_object = Utils.ReceiveImages(self.imagesPath)
        image_list = image_loading_object.load_images()
        # Plotting Final Stitched Image
        plt.figure(figsize=(10, 10))
        plt.title('Image After Collation')
        plt.imshow(Extract_Keypoints.extract_keypoints(image_list))
        plt.show()

    def image_enhancement(self):
        image_loading_object = Utils.ReceiveImages(self.imagesPath)
        image_list = image_loading_object.load_images()
        plt.figure(figsize=(10, 10))
        plt.title('Enhancement (Local Thresholding) After Collation')
        final_image = Extract_Keypoints.extract_keypoints(image_list)
        output = Enhancement.local_thresholding(final_image, 7)
        plt.imshow(output)
        plt.show()
        color_scale = "rgb"
        show_couple_of_images(final_image, output, "Original", "Local Thresholding", color_scale)
        show_couple_of_images(final_image, Enhancement.make_image_negative(final_image), "Original", "Negative", "rgb")


