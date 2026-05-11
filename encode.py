from LSBSteg import LSBSteg
import cv2
image = cv2.imread("sample.png")


steg = LSBSteg(image)
with open("secret.txt", "r") as file:
    secret_message = file.read()

encoded_image = steg.encode_text(secret_message)

cv2.imwrite("encoded.png", encoded_image)

print("Message encoded successfully into encoded.png")