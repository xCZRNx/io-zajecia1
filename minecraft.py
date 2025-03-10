def ciezar(typ_przedmiotu, ilosc):
    # Maksymalna liczba przedmiotów w jednej kieszeni
    MAX_ITEMS = 64
    
    # Wagi przedmiotów w gramach
    wagi = {
        "gold": 20000,
        "iron": 9000,
        "dirt": 25,
        "stick": 0.2,
        "wood": 400,
        "stone": 7000,
        "diamond": 10000
    }
    
    # Sprawdzenie czy przedmiot istnieje w bazie wag
    if typ_przedmiotu not in wagi:
        return "Nieznany typ przedmiotu!"
    
    # Ograniczenie ilości do maksymalnej wartości
    ilosc = min(ilosc, MAX_ITEMS)
    
    # Obliczenie ciężaru
    ciezar_calkowity = ilosc * wagi[typ_przedmiotu]
    
    return f"Ciężar {ilosc} sztuk {typ_przedmiotu} to {ciezar_calkowity} gram."

# Przykładowe wywołania
print(ciezar("gold", 10))   # Ciężar 10 sztuk gold to 200000 gram.
print(ciezar("stick", 100))  # Ciężar 64 sztuk stick to 12.8 gram.
print(ciezar("diamond", 5))  # Ciężar 5 sztuk diamond to 50000 gram.
