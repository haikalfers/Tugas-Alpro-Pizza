
"""
Kelas : 2023E
Prodi : D4 Manajemen Informatika
Kelompok 4
Anggota Kelompok
1. Zaidan Dhiya' Ulhaq (23091397152)
2. Alya Faadhilah Putri (23091397153)
3. Haikal Ferdian Saputra (23091397154)
"""
print("WELCOME TO PIZZA HUT WIYUNG")
print("SILAHKAN PILIH MENU")

total_harga : 0

print(
    """
    1. Frankfuter BBQ
    2. Meat Monsta
    3. Super Supreme
    4. Super Supreme Chicken
    """)

topping_pizza = int(input("Pilih Topping Pizza yang diinginkan(piih angka 1-4) : "))
if topping_pizza == 1:
    topping_pizza = "Frankfuter BBQ"
if topping_pizza == 2:
    topping_pizza = "Meat Monsta"
if topping_pizza == 3:
    topping_pizza = "Super Supreme"
if topping_pizza == 4:
    topping_pizza = "Super Supreme Chicken"

print(
    """
    1. Pan
    2. StuffedCrust Cheese
    3. StuffedCrust Sausage
    4. Cheesy Bites
    5. Crown Bites
    """)
crust_pizza = int(input("Pilih Crust/Pinggiran (piih angka 1-5) : "))
if crust_pizza == 1:
    crust_pizza = "Pan"
    total_harga = 43_637
if crust_pizza == 2:
    crust_pizza = "StuffedCrust Cheese"
    total_harga = 55_455
if crust_pizza == 3:
    crust_pizza = "StuffedCrust Sausage"
    total_harga = 52_728
if crust_pizza == 4:
    crust_pizza = "Cheesy Bites"
    total_harga = 57_273
if crust_pizza == 5:
    crust_pizza = "Crown Bites"
    total_harga = 55_455

extra_cheese = input("Apakah Annda Mau menambahkan Keju (y/n) : ").lower()
while extra_cheese not in ["y", "n"]:
    extra_cheese = input("Apakah Annda Mau menambahkan Keju (y/n) : ").lower()
if extra_cheese == "y":
    total_harga += 13_636
    extra_cheese =True
elif extra_cheese == "n":
    extra_cheese = False
    
print("\nTerima Kasih telah membeli di Pizza Hut")
print(f"Pesanan Anda\nPizza Dengan Topping {topping_pizza}")
print(f"Crust/Pinggiran {crust_pizza} dan")
print(f"{'dengan'if extra_cheese else 'tanpa'} Tambahan Keju")
print(f"Total Bill anda adalah {total_harga}")
