Total_item_terjual = 0
Total_pembeli = 0

def proses_pesanan(pelanggan, *args, **kwargs):
    global Total_item_terjual, Total_pembeli

    print(f"\nPelanggan: {pelanggan}")

    #Hitung total item dari args
    total_item = sum(args)
    Total_item_terjual += total_item
    Total_pembeli += 1

    print(f"\nJumlah item yang dipesan: {total_item}")

    if kwargs:
        print("Keterangan tambahan: ")
        for key, value in kwargs.items():
            print(f"-{key}: {value}")

# Input user
nama = input("Nama pelanggan: ")
burger = int(input(" Jumlah Burger: "))
roti = int(input(" Jumlah Roti: "))
coffee = int(input(" Jumlah Coffee: "))
tea = int(input(" Jumlah Tea: "))
keterangan = input("Spicy or not, Less sugar or not: ")

proses_pesanan(nama, roti, coffee, tea, keterangan=keterangan)

print("\nTotal item yang terjual hari ini:", Total_item_terjual)
print("Total pembeli hari ini:", Total_pembeli)