print(f"{open('hi.txt', encoding='UTF-8').read()}")
def kalkulator_winrate():
    print("\n=== Masukan Data WR ===\n")
    
    try:
        total_pertandingan = int(input("Total pertandingan saat ini: "))
        winrate_sekarang = float(input("Winrate saat ini (%): "))
        winrate_target = float(input("Winrate yang diinginkan (%): "))
        
        if total_pertandingan < 0 or winrate_sekarang < 0 or winrate_sekarang > 100 or winrate_target < 0 or winrate_target > 100:
            print("Error: Input tidak valid. Pastikan angka positif dan winrate antara 0-100%.")
            return
        
        # Hitung jumlah win saat ini
        jumlah_menang = (winrate_sekarang / 100) * total_pertandingan
        
        # Hitung pertandingan tambahan yang dibutuhkan
        if winrate_target <= winrate_sekarang:
            print("\nWinrate target harus lebih tinggi dari winrate saat ini!")
            return
        
        if winrate_target == 100:
            print("\nUntuk mencapai 100% winrate, Anda perlu menang semua pertandingan berikutnya.")
            print("Ini tidak mungkin dilakukan kecuali Anda belum pernah kalah.")
            return
        
        # Rumus: (jumlah_menang + x) / (total_pertandingan + x) = winrate_target/100
        # Diubah menjadi: x = (winrate_target*total_pertandingan - 100*jumlah_menang) / (100 - winrate_target)
        pertandingan_tambahan = (winrate_target * total_pertandingan - 100 * jumlah_menang) / (100 - winrate_target)
        
        # Bulatkan ke atas karena tidak bisa bermain sebagian pertandingan
        pertandingan_tambahan = max(0, pertandingan_tambahan)
        pertandingan_tambahan = int(pertandingan_tambahan) if pertandingan_tambahan == int(pertandingan_tambahan) else int(pertandingan_tambahan) + 1
        
        total_baru = total_pertandingan + pertandingan_tambahan
        jumlah_menang_baru = jumlah_menang + pertandingan_tambahan
        winrate_akhir = (jumlah_menang_baru / total_baru) * 100
        
        print("\n\n=====  Hasil  =====")
        print(f"Total pertandingan saat ini: {total_pertandingan}")
        print(f"Winrate kamu sekarang: {winrate_sekarang:.2f}%")
        print(f"Winrate yang diingkan: {winrate_target:.2f}%")
        print(f"\nKamu butuh {pertandingan_tambahan} win untuk mencapai target winrate")
        print(f"Total pertandingan setelah mencapai target Winrate: {total_baru}")
        print(f"Winrate akhir: {winrate_akhir:.2f}%")
        
        # Tambahan info
        if pertandingan_tambahan > 0:
            print("\nCatatan:")
            print("- Angka ini mengasumsikan Kamu akan menang semua pertandingan berikutnya")
            print("- Jika Kamu kalah, Kamu akan membutuhkan lebih banyak pertandingan lagi :/")
            print("- Semakin tinggi winrate target, semakin banyak pertandingan yang dibutuhkan")
    
    except ValueError:
        print("Error: Masukkan angka yang valid!")

# Jalankan kalkulator
kalkulator_winrate()
