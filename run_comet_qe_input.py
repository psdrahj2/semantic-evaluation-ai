from comet import download_model, load_from_checkpoint

# 1. Výběr směru překladu
print("Zvol směr překladu:")
print("1 = EN → CZ")
print("2 = CZ → EN")
choice = input("Tvoje volba (1 nebo 2): ").strip()

if choice == "1":
    path_src = input("Zadej cestu k ANGLICKÉMU souboru: ").strip()
    path_mt = input("Zadej cestu k ČESKÉMU souboru: ").strip()
elif choice == "2":
    path_src = input("Zadej cestu k ČESKÉMU souboru: ").strip()
    path_mt = input("Zadej cestu k ANGLICKÉMU souboru: ").strip()
else:
    print("Neplatná volba.")
    exit(1)

# 2. Načtení souborů
with open(path_src, encoding='utf-8') as f:
    src = f.read()
with open(path_mt, encoding='utf-8') as f:
    mt = f.read()

# 3. Načtení modelu
print("🔄 Načítám COMET-QE model...")
model_path = download_model("Unbabel/wmt22-cometkiwi-da")
model = load_from_checkpoint(model_path)

# 4. Výpočet
result = model.predict([{"src": src, "mt": mt}])

# 5. Výstup
print("\n📊 COMET-QE skóre:", result["system_score"])
