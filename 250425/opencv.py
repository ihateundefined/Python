import cv2

# print(cv2.__version__)

'''
# 이미지
img1 = cv2.imread('sh.png', 1)
img2 = cv2.imread('sh.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Test Image1', img1)
cv2.imshow('Test Image2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지를 다른 파일로 저장하기
cv2.imwrite('sunghun.png', img2)
'''

'''
# 카메라
camera = cv2.VideoCapture(0)

width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('test.avi', fourcc, 24, (int(width), int(height)))

while camera.isOpened():   
    # 카메라 프레임 읽기
    # 파이썬은 return 값을 두 개 받을 수 있음...?
    success, frame = camera.read()
    if success:
        writer.write(frame)
        # 프레임 출력
        cv2.imshow('Camera Window', frame)

        # ESC 클릭 시 종료
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
camera.release()
cv2.destroyAllWindows()
'''