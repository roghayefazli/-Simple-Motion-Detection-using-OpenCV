import cv2

# راه‌اندازی دوربین
cap = cv2.VideoCapture(0)

# خواندن اولین فریم
ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

while True:
    # خواندن فریم بعدی
    ret, frame2 = cap.read()
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

    # محاسبه تفاوت بین دو فریم
    delta = cv2.absdiff(frame1_gray, frame2_gray)
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]

    # بزرگ‌نمایی نواحی متحرک
    thresh = cv2.dilate(thresh, None, iterations=2)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # نمایش فریم
    cv2.imshow("Motion Detection", frame2)

    # برای خروج کلید 'q' را فشار دهید
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # به‌روزرسانی فریم مرجع
    frame1_gray = frame2_gray.copy()

cap.release()
cv2.destroyAllWindows()
