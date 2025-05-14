# Script topology.py Mininet untuk Topologi UMKM Fashion Lokal
Topologi ini akan menyimulasikan:
- 1 Cloud node (tempat VNF & marketplace)
- 1 SDN Controller (Ryu)
- 4 node UMKM Fashion berbeda (misal: BatikJogja, ModestBandung, EcoBali, ResellerJakarta)
- Semua node terhubung melalui switch pusat (s1) → bisa kamu kembangkan jadi SD-WAN

🛠️ Cara Menjalankan
1. Simpan file sebagai topology.py
2. Pastikan Ryu controller sudah aktif:
ryu-manager ryu.app.simple_switch_13
3. Jalankan topologi:
sudo python3 topology.py
4. Setelah net.interact() aktif, kamu bisa masuk ke node:
batikjogja ping cloud
