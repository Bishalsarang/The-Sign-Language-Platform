import pyttsx3
from predict import *


# Initialise Text to speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 105)
engine.setProperty('voice', 1)


def getMaxContour(contours,  minArea = -1):
    maxC = None
    maxArea = minArea
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (area > maxArea):
            maxArea = area
            maxC = cnt
    return maxC


def centreCrop(x, y, w, h):
    # Centre cropping the image
    x_start, y_start, x_end, y_end = 0, 0, 0, 0
    mx = 0
    if w > 0 and h > 0:
        mx = max(w, h, 150)
        if x + 7 * mx // 8 > roi_width and y + mx > roi_height:
            mx = max(roi_width - x, roi_height - y, 150)
            x_start, x_end = roi_width - mx, roi_width
            y_start, y_end = roi_height - mx, roi_height

        elif y + mx > roi_height and x == 0:
            mx = max(w, roi_height - y, 150)
            x_start, x_end = x, x + mx
            y_start, y_end = roi_height - mx, roi_height
        elif y + mx > roi_height:
            mx = max(w, roi_height - y, 150)
            x_start, x_end = x - mx // 8, x + 7 * mx // 8
            y_start, y_end = roi_height - mx, roi_height
        elif x + 7 * mx // 8 > roi_width:
            mx = max(roi_width - x, h, 150)
            x_start, x_end = roi_width - mx, roi_width
            y_start, y_end = y, y + mx
        elif x == 0:
            x_start, x_end = 0, mx
            y_start, y_end = y, y + mx
        else:
            x_start, x_end = x - mx // 8, x + 7 * mx // 8
            y_start, y_end = y, y + mx
    return  (x_start, y_start), (x_end, y_end)


window_name = "ASL"
frame_height, frame_width, roi_height, roi_width = 480, 900, 600, 300
cap = cv2.VideoCapture(0)
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
sentence = ""
while True:
    ret, frame = cap.read()
    if ret is None:
        print("No Frame Captured")
        continue

    cv2.rectangle(frame, (0, 0), (roi_width, roi_height), (255, 0, 0), 3)  # bounding box which captures ASL sign to be detected by the system

    # Crop blue rectangular area(ROI)
    img1 = frame[0: roi_height, 0: roi_width]
    img_ycrcb = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
    blur = cv2.GaussianBlur(img_ycrcb, (11, 11), 0)

    # lower  and upper skin color
    skin_ycrcb_min = np.array((0, 138, 67))
    skin_ycrcb_max = np.array((255, 173, 133))

    mask = cv2.inRange(blur, skin_ycrcb_min, skin_ycrcb_max)  # detecting the hand in the bounding box

    kernel = np.ones((2, 2), dtype = np.uint8)

    # Fixes holes in foreground
    mask = cv2.dilate(mask, kernel, iterations = 1)

    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, 2)
    # _, contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, 2)
    cnt = getMaxContour(contours, minArea = 2000)
    naya = cv2.bitwise_and(img1, img1, mask = mask)
    cv2.imshow("mask", mask)
    x, y, w, h = cv2.boundingRect(cnt)

    (x_start, y_start), (x_end, y_end) = centreCrop(x, y, w, h)

    # Draw Green Square around the hand
    cv2.rectangle(img1, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)

    cv2.imshow("naya", naya)
    hand_bg_rm = naya[y_start: y_end, x_start: x_end]
    hand = img1[y_start: y_end, x_start: x_end]

    # Control Key
    c = cv2.waitKey(1) & 0xff

    # Speak the sentence
    if len(sentence) > 0 and c == ord('s'):
        engine.say(sentence)
        engine.runAndWait()
    # Clear the sentence
    if c == ord('c') or c == ord('C'):
        sentence = ""
    # Delete the last character
    if c == ord('d') or c == ord('D'):
        sentence = sentence[:-1]

    # Put Space between words
    if c == ord('m') or c == ord('M'):
        sentence += " "

    # If  valid hand area is cropped
    if hand.shape[0] != 0 and hand.shape[1] != 0:
        conf, label = which(hand)
        conf, label1 = which(hand_bg_rm)
        cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, .7, (0, 0, 255))
        if c == ord('n') or c == ord('N'):
                sentence += label

    cv2.putText(frame, sentence, (50, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, .7, (0, 0, 255))
    cv2.imshow(window_name, frame)

    if c == 32:
        if hand.shape[0] == hand.shape[1] + 1:
            hand = img1[y_start: y_end, x_start: x_end + 1]
        elif hand.shape[1] == hand.shape[0] + 1:
            hand = img1[y_start: y_end + 1, x_start: x_end]
        elif hand.shape[0] != hand.shape[1]:
            print(hand.shape)
            print("Outside ROI")
            continue
        cv2.imwrite("test.jpg", hand)
        cv2.imwrite("test_bg_less.jpg", hand_bg_rm)
    # If pressed ESC break
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
