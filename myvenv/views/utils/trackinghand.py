import cv2
import mediapipe as mp
import math
class HandTracker:
    def __init__(self, mode=False, maxHands=2, detectionThresh=0.5, tThresh=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionthresh = detectionThresh
        self.tThresh = tThresh
        self.hands = mp.solutions.hands.Hands(
             max_num_hands = 1,
             model_complexity = 0,
             min_detection_confidence = 0.5,
             min_tracking_confidence=0.5
        )
        self.tipIds = [4,8,12,16,20]

    def findHands(self, img):
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)
        if self.results.multi_hand_landmarks:
            for hd in self.results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(img, hd, mp.solutions.hands.HAND_CONNECTIONS)
        return img
    
    def findHandsPosition(self, img, draw=True):
        xList = []
        yList = []
        self.lmlist = []
        bbox = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[0]
            for idx, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmlist.append([idx, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        if xList and yList:
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = [xmin, xmax, ymin, ymax]
            if draw:
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 255), 5)
        if self.lmlist:
            return self.lmlist
        else:
            return []
    def findDistance(self, p1, p2, img, draw=True,r=15, t=3):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
           cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
           cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
           cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
           cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
           length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2, cx, cy]

    def findFingure(self):
        FingersUps = []
        #check if the tip of our thumb is right or left
        # TODO CHECKING IF THE HAND IS RIGHT OF LEFT
        if self.lmlist[self.tipIds[0]][1]< self.lmlist[self.tipIds[0]-1][1]:
                 FingersUps.append(0)
        else:
                FingersUps.append(1)

        #check if the tip of the finger is above the other landmarks which is 2 steps below it 
        for i in range(1,5):
            if self.lmlist[self.tipIds[i]][2]< self.lmlist[self.tipIds[i]-2][2]:
                 FingersUps.append(1)
            else:
                FingersUps.append(0)
        return FingersUps
                   
    

# def main():
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error: Camera could not be opened.")
#         return
#     tracker = HandTracker()
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame = cv2.flip(frame, 1)
#         frame = tracker.findHands(frame)
#         positions = tracker.findHandsPosition(frame)
#         if positions:
#             lmlist, bbox = positions
#         cv2.imshow("Video Capturing", frame)
        
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
    # main()
