from pipeline.store_data import init_db, save_translation, get_all_translations, is_translated

save_translation("koira", "dog")
save_translation("kissa", "cat")

for fi, en in get_all_translations():
    print(f"{fi} → {en}")
