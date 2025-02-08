berat_awal = 25
harga_awal = 650000  
modal_awal = harga_awal * berat_awal
print("Modal Awal:", modal_awal)

harga_sekarang = 685000
keuntungan_dalam_rupiah = (harga_sekarang - harga_awal) * berat_awal
print("Keuntungan dalam Rupiah:", keuntungan_dalam_rupiah)

keuntungan_dalam_persen = (keuntungan_dalam_rupiah / modal_awal) * 100
print(f"Persentase Keuntungan: {keuntungan_dalam_persen:.2f}%")

berat_tambahan = 15
harga_beli_tambahan = 685000
modal_tambahan = berat_tambahan * harga_beli_tambahan
print("Modal Tambahan:", modal_tambahan)

total_modal = modal_awal + modal_tambahan
print("Total Modal:", total_modal)

harga_naik = 715000
nilai_akhir = (berat_awal + berat_tambahan) * harga_naik
print("Nilai Akhir:", nilai_akhir)

keuntungan_akhir_dalam_rupiah = nilai_akhir - total_modal
print("Keuntungan Akhir dalam Rupiah:", keuntungan_akhir_dalam_rupiah)

keuntungan_akhir_dalam_persen = (keuntungan_akhir_dalam_rupiah / total_modal) * 100
print(f"Persentase Keuntungan Akhir: {keuntungan_akhir_dalam_persen:.2f}%")
