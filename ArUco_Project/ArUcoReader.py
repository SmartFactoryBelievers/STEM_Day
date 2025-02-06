import cv2 as cv
from cv2 import aruco
import numpy as np

class ArUcoDetector:
    def __init__(self, cam_mat, dist_coef, marker_size):
        self.cam_mat = cam_mat
        self.dist_coef = dist_coef
        self.marker_size = marker_size
        self.marker_info = []

    def read_aruco_marker(self, frame):
        # Define the dictionary and parameters for ArUco detection
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters = aruco.DetectorParameters_create()

        # Detect the markers in the frame
        corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

        self.marker_info = []

        # If markers are detected
        if ids is not None:
            # Estimate pose of each marker
            rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, self.marker_size, self.cam_mat, self.dist_coef)
            
            # Iterate over detected markers
            for i in range(len(ids)):
                # Draw the marker boundaries
                aruco.drawDetectedMarkers(frame, corners)

                # Store the marker ID, distance, and rotation vector
                marker_id = ids[i][0]
                distance = np.linalg.norm(tvecs[i][0])
                rvec = rvecs[i][0]
                self.marker_info.append((marker_id, distance, rvec))
                print(f"ArUco Marker ID: {marker_id}, Distance: {distance:.2f} cm, Rotation Vector: {rvec}")

    def start_camera_stream(self, callback=None):
        cap = cv.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
            frame = cv.resize(frame, (1200, 700), interpolation=cv.INTER_LINEAR)
            if not ret:
                break

            self.read_aruco_marker(frame)

            if callback:
                callback(self)

            cv.imshow('Frame', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

    def distance(self, marker_id):
        for id, dist, _ in self.marker_info:
            if id == marker_id:
                return dist
        return None

    def get_ids(self):
        return [id for id, _, _ in self.marker_info]

    def orientation(self, marker_id):
        for id, _, rvec in self.marker_info:
            if id == marker_id:
                # Convert the rotation vector to a rotation matrix
                rotation_matrix, _ = cv.Rodrigues(rvec)
                # Calculate the yaw angle (rotation around the y-axis)
                yaw = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
                # Convert the yaw angle from radians to degrees
                yaw_degrees = np.degrees(yaw)
                return yaw_degrees
        return None
