with open('secret.txt', 'r') as file:
    secret_message = file.read()
from steganogan import SteganoGAN
steganogan = SteganoGAN.load(architecture='dense')


steganogan.encode('sample_image.png', 'encoded_image1.png', secret_message)
print("Message encoded and saved in 'encoded_image1.png'.")
# Decode the message from the image
# decoded_message = steganogan.decode('encoded_image.png')
# print("Decoded message:", decoded_message)
