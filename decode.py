from LSBSteg import LSBSteg
import cv2

# Load encoded image
image = cv2.imread("encoded.png")

# Create LSB object
steg = LSBSteg(image)

# Decode hidden message
hidden_message = steg.decode_text()

print("Hidden Message:")
print(hidden_message)