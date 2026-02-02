import tensorflow as tf
from keras import layers, models
from keras.applications import MobileNetV2
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os

DATA_DIR = r'C:\Users\KHAIRUZ ZUHDI\OneDrive\Desktop\porto\TransferLearning\Dataset'
test_image = r'C:\Users\KHAIRUZ ZUHDI\OneDrive\Desktop\porto\TransferLearning\test1.jpeg'


IMG_SIZE = (160, 160)
BATCH_SIZE = 32
EPOCHS = 10


print(f"membaca dataset dari {DATA_DIR}")

if not os.path.exists(DATA_DIR):
    print("folder tidak ditemukan")
    exit()
    
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATA_DIR,
    validation_split = 0.2,
    subset = 'training',
    seed = 123,
    image_size = IMG_SIZE,
    batch_size = BATCH_SIZE
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    DATA_DIR,
    validation_split = 0.2,
    subset = 'validation',
    seed = 123,
    image_size = IMG_SIZE,
    batch_size = BATCH_SIZE
)

class_names = train_ds.class_names
print(f"\nkategori terdeteksi {class_names}")

print("\nMobileNet2 Aktif...")

base_model = MobileNetV2(input_shape=IMG_SIZE + (3,), include_top = False, weights = 'imagenet' )
base_model.trainable = False

model = models.Sequential([
    layers.Input(shape=IMG_SIZE + (3,)),
    layers.Rescaling(1./127.5, offset=-1),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.2),
    layers.Dense(len(class_names), activation='softmax')
])

model.compile(optimizer= tf.keras.optimizers.Adam(learning_rate = 0.0001), loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])


print("\n mulai training")

history = model.fit(train_ds, validation_data = val_ds, epochs = EPOCHS)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label = "Training Accuracy")
plt.plot(val_acc, label = "Validation Accuracy")
plt.legend(loc = "lower right")
plt.title='Training and Validation Accuracy'


plt.subplot(2, 1, 2)
plt.plot(loss, label="Training loss")
plt.plot(val_loss, label="validation loss")
plt.legend(loc="upper right")
plt.title="Training and Validation Loss"
plt.show()

print(f"\n Final test: {test_image}")

try:
    img = image.load_img(test_image, target_size = IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    score = tf.nn.softmax(prediction[0])
    
    label = class_names[np.argmax(score)]
    confidence = 100 * np.max(score)
    
    print('=' *  40)
    print(f'hasil :{label.upper()}')
    print(f'keyakinan: {confidence:.2f}%')
    print('=' *  40)

except Exception as e:
    print(f'gagal load gambar {e}')    


model.save('content_classifier.keras')
print("✅ Model berhasil disimpan!")