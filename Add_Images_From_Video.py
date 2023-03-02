import cv2
import glob


class ExtractImages:

    def __int__(self, video_path):
        self.video_path = video_path

    def extraction(self):
        path = sorted(glob.glob(self.video_path + "/*.mp4"))
        # Open the video file
        video = cv2.VideoCapture(path)

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
                cv2.imwrite(f'Extracted_Images/frame{frame_count}.jpg', image)

                # Increment the frame counter
                frame_count += 1

        # Release the video file
        video.release()


