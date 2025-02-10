import numpy as np
from ArUcoReader import ArUcoDetector

if __name__ == "__main__":
    # Load calibration data
    calib_data_path = "/home/pi/Desktop/ArUco_Project/Calib_Data/MultiMatrix.npz"
    calib_data = np.load(calib_data_path)
    cam_mat = calib_data["camMatrix"]
    dist_coef = calib_data["distCoef"]
    marker_size = 7.62  # centimeters

    # Create an instance of ArUcoDetector
    aruco_detector = ArUcoDetector(cam_mat, dist_coef, marker_size)

    def process_marker_data(detector):
        distance = detector.distance(marker_id)
        detected_ids = detector.get_ids()
        print(f"Detected marker IDs: {detected_ids}")

    # Start the camera stream with the callback function
    aruco_detector.start_camera_stream(callback=process_marker_data)

