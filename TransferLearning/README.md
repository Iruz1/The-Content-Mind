# 🧠 The Content Mind: AI Image Classifier

---

## About The Project
Sebagai seorang **Content Director**, makanan sehari-hari saya adalah folder Google Drive yang berantakan: ribuan foto baju campur dengan foto makanan, tanpa label, tanpa struktur.

Iseng belajar Data Science, saya menantang diri sendiri: **"Bisa nggak sih AI bantuin kerjaan sortir ini?"**

Awalnya saya coba bangun model CNN sendiri (from scratch), tapi hasilnya kurang memuaskan (akurasi cuma 50-60%). Setelah riset lebih lanjut, saya mengimplementasikan **Transfer Learning** menggunakan **MobileNetV2**—memanfaatkan model yang sudah dilatih Google.

Hasilnya? Akurasi melonjak ke **90%+** dan AI ini sekarang bisa membedakan mana konten **Food** dan mana **Fashion** dengan sangat percaya diri.

## 🛠️ Tech Stack & Tools
Projek ini dibuat sesimpel mungkin tapi *powerful* di belakang layar:
* **Brain:** Python, TensorFlow, Keras.
* **Model:** MobileNetV2 (Pre-trained on ImageNet).
* **Technique:** Transfer Learning & Fine-Tuning.
* **Data Processing:** Pandas & OS Module (untuk cleaning dataset yang berantakan).

## The Challenge: "Nasi Uduk Test"
Tantangan terbesar projek ini bukan di kodingan, tapi di **Dataset** yang kotor.
1.  **Cleaning:** Saya menulis script otomatis untuk membuang file corrupt/0KB.
2.  **Structuring:** Merapikan ribuan file dari sub-folder ke struktur flat agar bisa dibaca TensorFlow.
3.  **Real World Test:** Saya mengetes model dengan foto nasi uduk yang saya potret sendiri (`nasi.jpeg`).

**Hasilnya:**
Model mengenali foto tersebut sebagai **FOOD** dengan tingkat keyakinan (confidence) **99.8%**.



## Performance
Menggunakan 10 Epoch saja, model sudah mencapai konvergensi yang baik.
* **Training Accuracy:** ~96%
* **Validation Accuracy:** ~92%


## Cara Menjalankan (Local)
Kalau penasaran mau coba di laptop sendiri:

1.  **Clone repo ini:**
    ```bash
    git clone [https://github.com/username-lo/The-Content-Mind.git](https://github.com/username-lo/The-Content-Mind.git)
    ```
2.  **Install library:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run Training:**
    ```bash
    python notebooks/2_transfer_learning.py
    ```
    

---

**dataset**
Food : https://www.kaggle.com/datasets/trolukovich/food11-image-dataset/data

Fashion : https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full/data

**Dibuat oleh Khairuz Zuhdi**

Learning Data Science one line of code at a time.
