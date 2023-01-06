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

        matches_all = []
        for m, n in matches:
            matches_all.append(m)
        # Finding the best matches
        good = []
        for m, n in matches:
            if m.distance < 0.6 * n.distance:  # Threshold
                good.append(m)

        # Set minimum match condition
        MIN_MATCH_COUNT = 5

        if len(good) > MIN_MATCH_COUNT:

            # Converting keypoints to an argument for findHomography
            source_points = np.float32([keypoints1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            destination_points = np.float32([keypoints2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            # Establish a homography
            M, _ = cv2.findHomography(source_points, destination_points, cv2.RANSAC, 5.0)
            result = WarpImages.warpedImage(image2, image1, M)
            Image_List.insert(0, result)

            if len(Image_List) == 1:
                break
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    return result

