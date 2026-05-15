import numpy as np
import matplotlib.pyplot as plt

# Okunacak dosya yolu
file_path = "/home/tunahan/ros2_library/install/dock_apex_detector/lib/python3.10/site-packages/dock_sablon.npy"   # kendi dosya adını buraya yaz

#lib/python3.10/site-packages

# .npy dosyasını oku
data = np.load(file_path, allow_pickle=True)

print("Veri tipi:", type(data))
print("Shape:", data.shape)
print("Dtype:", data.dtype)

# Numpy array'e çevir
arr = np.array(data)

# Eğer object tipinde kayıtlıysa düzeltmeyi dene
if arr.dtype == object:
    try:
        arr = np.vstack(arr)
    except Exception:
        arr = np.array(arr.tolist())

print("Dönüştürülmüş shape:", arr.shape)

# 2D X-Y noktası ise çiz
if arr.ndim == 2 and arr.shape[1] >= 2:
    x = arr[:, 0]
    y = arr[:, 1]

    plt.figure(figsize=(7, 7))
    plt.scatter(x, y, s=8)
    plt.plot(x, y, linewidth=0.8, alpha=0.6)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Dock Şablonu 2D Çizimi")
    plt.axis("equal")
    plt.grid(True)

    plt.show()

else:
    print("Bu dosya 2D X-Y nokta formatında değil.")
