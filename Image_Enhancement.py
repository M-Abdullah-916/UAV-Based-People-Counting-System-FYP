import numpy as np
import Utils
import Extract_Keypoints
from matplotlib import pyplot as plt
import cv2


class Enhancement:
    def __init__(self, images_path):
        self.imagesPath = images_path
        self.count = 0

    def image_is_in_gray_scale(self, image):
        return len(image.shape) == 2

    def make_image_negative(self, image):
        if not self.image_is_in_gray_scale(image):
            output = np.subtract([255, 255, 255], image)
            return output.astype(np.uint8)
        else:
            return np.subtract(255, image)

    def local_thresholding(self, image, kernel_size=7):
        output = self.padding(image, kernel_size)
        return self.apply_thresholding(image, output, kernel_size)

    def padding(self, image, kernel_size):
        output = np.zeros(image.shape)
        up_side_inf_limit = 0
        up_side_sup_limit = int(kernel_size / 2)
        for i in range(up_side_inf_limit, up_side_sup_limit):
            for j in range(image.shape[1]):
                output[i, j] = image[i, j]

        down_side_inf_limit = image.shape[0] - int(kernel_size / 2)
        down_side_sup_limit = image.shape[0]
        for i in range(down_side_inf_limit, down_side_sup_limit):
            for j in range(image.shape[1]):
                output[i, j] = image[i, j]

        left_side_inf_limit = 0
        left_side_sup_limit = int(kernel_size / 2)
        for i in range(image.shape[0]):
            for j in range(left_side_inf_limit, left_side_sup_limit):
                output[i, j] = image[i, j]

        right_side_inf_limit = image.shape[1] - int(kernel_size / 2)
        right_side_sup_limit = image.shape[1]
        for i in range(image.shape[0]):
            for j in range(right_side_inf_limit, right_side_sup_limit):
                output[i, j] = image[i, j]
        return output

    def apply_thresholding(self, image, output, kernel_size):
        off_set = int(kernel_size / 2)
        starting_row = off_set
        ending_row = image.shape[0] - off_set
        starting_column = off_set
        ending_column = image.shape[1] - off_set

        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                if not self.image_is_in_gray_scale(image):
                    frame = image[i - off_set:i + off_set, j - off_set:j + off_set]
                    median_hue = np.median(frame[:, :, 0])
                    median_sat = np.median(frame[:, :, 1])
                    median_val = np.median(frame[:, :, 2])
                    threshold_hue = int(median_hue) - 5
                    threshold_sat = int(median_sat) - 5
                    threshold_val = int(median_val) - 5

                    if image[i, j, 0] > threshold_hue:
                        output[i, j] = 255
                    if image[i, j, 1] > threshold_sat:
                        output[i, j] = 255
                    if image[i, j, 2] > threshold_val:
                        output[i, j] = 255
                else:
                    frame = image[i - off_set:i + off_set, j - off_set:j + off_set]
                    median = np.median(frame)
                    threshold = int(median) - 5
                    if image[i, j] > threshold:
                        output[i, j] = 255

        if not self.image_is_in_gray_scale(image):
            for i in range(output.shape[0]):
                for j in range(output.shape[1]):
                    if not np.array_equal(output[i, j], [255, 255, 255]):
                        output[i, j] = image[i, j]
        return output.astype(np.uint8)

    def adapt_image_to_color_scale(self,image, color_scale):
        color = None
        if color_scale != 'gray':
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        else:
            color = "gray"
        return image, color

    def enhance_image(self):
        image_loading_object = Utils.ReceiveImages(self.imagesPath)
        image_list = image_loading_object.load_images()
        final_image = Extract_Keypoints.extract_keypoints(image_list)
        plt.figure(figsize=(10, 10))
        plt.title('Enhancement (Local Thresholding) After Collation')
        output = self.local_thresholding(final_image, 7)
        plt.imshow(output)
        plt.show()
        plt.figure(figsize=(10, 10))
        plt.title('Enhancement (Negative) After Collation')
        plt.imshow(self.make_image_negative(final_image))
        plt.show()
