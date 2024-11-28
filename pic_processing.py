import cv2
import numpy as np

def process_pic_opencv(file_path):
    # Загрузка изображения
    pic = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    
    # Проверяем, содержит ли изображение альфа-канал
    if pic.shape[2] == 4:  # Альфа-канал присутствует
        # Отделяем альфа-канал
        b, g, r, alpha = cv2.split(pic)
        
        # Создаем белый фон
        white_background = np.ones_like(alpha) * 255
        
        # Добавляем белый фон к прозрачным участкам
        alpha_normalized = alpha / 255.0
        b = b * alpha_normalized + white_background * (1 - alpha_normalized)
        g = g * alpha_normalized + white_background * (1 - alpha_normalized)
        r = r * alpha_normalized + white_background * (1 - alpha_normalized)
        
        # Объединяем каналы в итоговое изображение
        pic = cv2.merge((b, g, r)).astype(np.uint8)
    
    # Возвращаем обработанное изображение
    return pic

# Пример использования
file_path = "pic.png"  # Путь к вашему файлу
processed_pic = process_pic_opencv(file_path)
cv2.imshow("Processed pic", processed_pic)  # Покажем результат
cv2.imwrite("processed_pic.jpg", processed_pic)  # Сохраним в новый файл
cv2.waitKey(0)
cv2.destroyAllWindows()
