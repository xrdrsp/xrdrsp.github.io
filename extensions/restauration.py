import os
import shutil

directory = input("Saisissez le chemin pour la RESTAURATION : ")

for path, folders, files in os.walk(directory):
    for file in files:
        if file.endswith('.html.bak'):
            bak_path = os.path.join(path, file)
            original_html_path = bak_path[:-4]
            shutil.copyfile(bak_path, original_html_path)
            print(f"Restauré : {original_html_path}")