import cv2
import mediapipe as mp
import pyautogui

mpHands=mp.solutions.hands
hands=mpHands.Hands(max_num_hands=1,min_detection_confidence=0.5)
mpDraw=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    x,y,c=frame.shape
    framce=cv2.flip(frame,1)
    framergb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    result=hands.process(framergb)

    num_fingers=0
    if(result.multi_hand_landmarks):
        landmarks=[]
        for handslms in result.multi_hand_landmarks:
            for idx, lm in enumerate(handslms.landmark):
                landmarks.append([lm.x*x,lm.y*y])
            mpDraw.draw_landmarks(frame,handslms,mpHands.HAND_CONNECTIONS)
            if len(landmarks) > 0:
                if landmarks[4][0] < landmarks[3][0]:
                    num_fingers += 1
                if landmarks[8][1] < landmarks[6][1]:
                    num_fingers += 1
                if landmarks[12][1] < landmarks[10][1]:
                    num_fingers += 1
                if landmarks[16][1] < landmarks[14][1]:
                    num_fingers += 1
                if landmarks[20][1] < landmarks[18][1]:
                    num_fingers += 1
                
            # cv2.putText(frame, f"{num_fingers}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            if(num_fingers==5):
                cv2.putText(frame, "Accelerate", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
                pyautogui.keyUp("up")
                pyautogui.keyUp("down")
                pyautogui.keyDown("right")
                pyautogui.keyUp("left")
            
            elif(num_fingers==1):
                cv2.putText(frame, "Stop", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
                pyautogui.keyUp("up")
                pyautogui.keyUp("down")
                pyautogui.keyUp("right")
                pyautogui.keyDown("left")
            else :
                pass
                pyautogui.keyUp("up")
                pyautogui.keyUp("down")
                pyautogui.keyUp("right")
                pyautogui.keyUp("left")
    cv2.imshow("Sample", frame) 
    if cv2.waitKey(1) == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
