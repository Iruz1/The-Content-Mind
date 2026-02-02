import os
from PIL import Image 


dataset_path = r"C:\Users\KHAIRUZ ZUHDI\OneDrive\Desktop\porto\TransferLearning\Dataset"

print(f"🧹 Sedang memeriksa folder: {dataset_path}")
print("Mencari file 0KB dan gambar corrupt...")

total_dihapus = 0

for root, dirs, files in os.walk(dataset_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        try:
            if os.path.getsize(file_path) == 0:
                print(f"❌ Menghapus file 0KB: {filename}")
                os.remove(file_path)
                total_dihapus += 1
                continue 

            try:
                img = Image.open(file_path)
                img.verify() 
                img.close()
            except (IOError, SyntaxError) as e:
                print(f"⚠️ Menghapus gambar corrupt: {filename}")
                os.remove(file_path)
                total_dihapus += 1

        except Exception as e:
            print(f"Error pada {filename}: {e}")

print("-" * 30)
if total_dihapus == 0:
    print("Dataset bersih! Tidak ada file rusak.")
else:
    print(f" Selesai! Total {total_dihapus} file 'sampah' berhasil dibuang.")
    print("Sekarang coba jalankan training lagi!")