def ciezar(typ_przedmiotu, ilosc):
    
    # Maksymalna liczba przedmiotów w jednej kieszeni
    max_items = 64
    
    
    wagi = {
        "gold": 20000,
        "iron": 9000,
        "dirt": 25,
        "stick": 0.2,
        "wood": 400,
        "stone": 7000,
        "diamond": 10000
    }
    
    if typ_przedmiotu not in wagi:
        return "Nieznany typ przedmiotu!"
    
    ilosc = min(ilosc, max_items)
    
    ciezar_calkowity = ilosc * wagi[typ_przedmiotu]
    
    return f"Ciężar {ilosc} sztuk {typ_przedmiotu} to {ciezar_calkowity} gram."

# Przykładowe wywołania
print(ciezar("gold", 10))   
print(ciezar("stick", 100))  
print(ciezar("diamond", 5)) 
