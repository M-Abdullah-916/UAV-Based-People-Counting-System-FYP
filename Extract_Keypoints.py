import cv2
import WarpImages
import numpy as np


def extractKeypoints(Image_List):
    orb = cv2.ORB_create(nfeatures=2000)
    while True:
        image1 = Image_List.pop(0)
        image2 = Image_List.pop(0)
        # Finding the key points and descriptors with ORB Class
        keypoints1, descriptors1 = orb.detectAndCompute(image1,
                                                        None)  # descriptors are arrays of numbers that define the keypoints
        keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

        # Create a Brute Force Matcher object to match descriptors
        # It will find all matching keypoints in the two images
        bruteForce = cv2.BFMatcher_create(
            cv2.NORM_HAMMING)  # NORM_HAMMING specifies the distance as a measurement of similarity between two descriptors

        # Find matching points
        matches = bruteForce.knnMatch(descriptors1, descriptors2, k=2)

