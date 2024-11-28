import cv2

# Функция изменения размера изображения
def resize_picture(picture_path, width, height):
    picture = cv2.imread(picture_path)
    resized_picture = cv2.resize(picture, (width, height))
    return resized_picture

# Функция конвертации в черно-белое
def convert_to_grayscale(picture_path):
    picture = cv2.imread(picture_path)
    grayscale_picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    return grayscale_picture

# Функция применения фильтра Гаусса
def apply_gaussian_blur(picture_path, kernel_size=(5, 5)):
    picture = cv2.imread(picture_path)
    blurred_picture = cv2.GaussianBlur(picture, kernel_size, 0)
    return blurred_picture
# 
# Использование
file_path = "pic.jpeg"  # Путь к изображению

# Изменение размера
resized = resize_picture(file_path, 700, 700)
cv2.imshow("Resized pic", resized)
cv2.imwrite("resized_pic.jpeg", resized)

# Конвертация в черно-белое
grayscale = convert_to_grayscale(file_path)
cv2.imshow("Gray picture", grayscale)
cv2.imwrite("gray_pic.jpeg", grayscale)

# Применение фильтра Гаусса
blurred = apply_gaussian_blur(file_path)
cv2.imshow("Blur pic", blurred)
cv2.imwrite("blur_pic.jpeg", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
