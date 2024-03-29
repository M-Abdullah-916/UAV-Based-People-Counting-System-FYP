import cv2
import glob


class ExtractImages:

    def __init__(self):
        self.video_path = 0

    def extraction(self):
        # Open the video file
        video = cv2.VideoCapture("Videos/video3.mp4")

        # Initialize variables
        frame_count = 0
        success = True

        # Loop through each frame of the video
        while success:
            # Read the next frame
            success, image = video.read()

            # If a frame was successfully read
            if success:
                # Save the frame as a JPEG image
                cv2.imwrite(f'Images/frame{frame_count}.jpg', image)

                # Increment the frame counter
                frame_count += 1

        # Release the video file
        video.release()


