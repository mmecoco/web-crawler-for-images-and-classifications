from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode="nearest")

print("ok")
img = load_img("rabbit_0.png")  # PIL 이미지
x = img_to_array(img)
x = x.reshape((1,) + x.shape)
print(x.shape)

i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=".", save_prefix="cat", save_format="png"):
    i += 1
    if i > 20:
        break