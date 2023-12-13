# Importing the OpenCV library for computer vision tasks
import cv2

# Load the pre-trained Haar Cascade for detecting Russian license plates
haarcascade_platenumber = "haarcascade_russian_plate_number.xml"

# Open the default camera (camera index 0)
Capture = cv2.VideoCapture(0)

# Set the width and height of the captured frames
Capture.set(3, 640)  # width
Capture.set(4, 480)  # height

# Set the minimum area required to consider a detected region as a license plate
mininum_area_plate = 500

# Initialize a counter to keep track of saved license plates
count_save_click = 0

# Infinite loop for capturing frames from the camera
while True:
    # Read a frame from the camera
    success, img = Capture.read()

    # Create a CascadeClassifier object using the trained Haar Cascade for license plates
    plate_cascade = cv2.CascadeClassifier(haarcascade_platenumber)

    # Convert the frame to grayscale
    gray_scale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect license plates in the grayscale image
    car_plates = plate_cascade.detectMultiScale(gray_scale_image, 1.1, 4)

    # Iterate over the detected license plates
    for (x, y, w, h) in car_plates:
        # Calculate the area of the detected license plate
        image_area = w * h

        # Check if the area is greater than the minimum required area
        if image_area > mininum_area_plate:
            # Draw a rectangle around the detected license plate
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 139), 2)
           
            # Add text indicating that a number plate is detected
            cv2.putText(img, "Number Plate Detected", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 139), 2)

            # Extract the region of interest (ROI) containing the license plate
            image_region = img[y: y+h, x:x+w]

            # Display the ROI in a separate window
            cv2.imshow("ROI", image_region)

    # Display the original frame with license plate detection results
    cv2.imshow("Result", img)

    # Check if the 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the detected license plate region as an image
        cv2.imwrite("plates/scaned_img_" + str(count_save_click) + ".jpg", image_region)

        # Display a message indicating that the license plate is saved
        cv2.rectangle(img, (0, 200), (640, 300), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, "Plate Number Saved", (80, 250), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 139), 2)
       
        # Display the result with the saved message
        cv2.imshow("Results", img)

        # Wait for 500 milliseconds before clearing the saved message
        cv2.waitKey(500)

        # Increment the counter for saved license plates
        count_save_click += 1



# import cv2

# harcascade = "haarcascade_russian_plate_number.xml"

# cap = cv2.VideoCapture(0)

# cap.set(3, 640)  # width
# cap.set(4, 480)  # height

# # Set the percentage of the image area for minimum plate area
# min_area_percentage = 0.01  # Adjust this value as needed

# count = 0

# while True:
#     success, img = cap.read()

#     plate_cascade = cv2.CascadeClassifier(harcascade)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
# for (x, y, w, h) in plates:
#         area = w * h

#         # Calculate the minimum area based on the percentage of the image area
#         img_area = img.shape[0] * img.shape[1]
#         min_area = min_area_percentage * img_area

#         if area > min_area:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
#             img_roi = img[y: y + h, x:x + w]
#             cv2.imshow("ROI", img_roi)

#             cv2.imshow("Result", img)

#         if cv2.waitKey(1) & 0xFF == ord('s'):
#            if 'img_roi' in locals():  # Check if img_roi is defined
#             cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
#             cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
#             cv2.imshow("Results", img)
#             cv2.waitKey(500)
#             count += 1
