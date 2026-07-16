import os
import shutil

directory = input("Saisissez le chemin du répertoire de travail : ")

if not os.path.isdir(directory) :
    print("Le répertoire spécifié n'existe pas.")
    exit(1)

print("Cette action peut être dangereuse. Confirmez-vous que le répertoire est correctement saisi ? (o / n)", end = ' ')
o = input().strip().lower()
if (o != 'o') :
    print("Arrêt du programme sans modifications.")
    exit(0)

cnt_traites = 0
cnt_ignores = 0

for path, folders, files in os.walk(directory) :
    for file in files :
        if file.endswith('.html') and file not in ['scaffold.html', 'head.html', 'foot.html'] and not 'uploads/' in path and not 'fichiers/' in path : 
            full_path = os.path.join(path, file)
            
            with open(full_path, 'r', encoding="utf-8") as f :
                lines = f.readlines()

            # already_processed = False
            # for line in lines:
            #     if 'src="/common.js"' in line:
            #         already_processed = True
            #         break
            # if already_processed:
            #     cnt_ignores += 1
            #     print(f"Ignoré (déjà formaté) : {full_path}")
            #     continue

            title = ''
            ext_lines = []
            body_start_idx = -1
            body_end_idx = -1
            
            in_ext = False
            div_depth = 0  # fermer correctement le <div id="ext">

            for idx, line in enumerate(lines) :
                # titre
                if '<title>' in line and '</title>' in line :
                    title = line
                
                # ext
                if 'id="ext"' in line :
                    in_ext = True
                if in_ext:
                    ext_lines.append(line)
                    if '<div' in line :
                        div_depth += 1
                    if '</div>' in line :
                        div_depth -= 1
                    if div_depth == 0 :
                        in_ext = False
                    continue
                
                # <body> et </body>
                if line.endswith('</body>') or line.endswith('</body>\n'):
                    body_end_idx = idx
                elif line.endswith('body>') or line.endswith('body>\n') :
                    body_start_idx = idx

            if body_start_idx != -1 and body_end_idx != -1 :
                backup_path = full_path + '.bak'
                shutil.copyfile(full_path, backup_path)
                
                head = [
                    '<!DOCTYPE html>\n',
                    '<html lang="zh-CN">\n',
                    '<head>\n',
                    '    <meta charset="utf-8">\n',
                    f'    {title.strip()}\n',
                    '    <script src="/common.js"></script>\n',
                ] + ext_lines + [
                    '</head>\n',
                    '<body>\n',
                    '    <main>\n'
                ]
                
                tail = [
                    '    </main>\n',
                    '    <footer id="footer"></footer>\n',
                    '</body>\n',
                    '</html>'
                ]
                
                raw_body_content = lines[body_start_idx + 1 : body_end_idx]

                cleaned_body_content = []
                for line_content in raw_body_content:
                    stripped = line_content.strip().lower()
                    # Si la ligne contient une balise de structure générée, on l'ignore
                    if (stripped.endswith('<main>') or 
                        stripped.endswith('<main>\n') or 
                        stripped.endswith('</main>') or 
                        stripped.endswith('</main>\n') or 
                        stripped.endswith('</footer>') or 
                        stripped.endswith('</footer>\n') or 
                        'id="header"' in stripped or
                        'id="footer"' in stripped):
                        continue
                    cleaned_body_content.append(line_content)

                new_lines = head + cleaned_body_content + tail

                with open(full_path, 'w', encoding="utf-8") as f :
                    f.writelines(new_lines)

                print(f"Fichier traité : {full_path} (Sauvegarde créée : {file}.bak)")
                cnt_traites += 1
            else :
                print(f"Ignoré (balises <body> introuvables) : {full_path}")
                cnt_ignores += 1

print("\n" + "=" * 40)
print("Rapport de traitement :")
print(f" - {cnt_traites} fichier(s) modifié(s) avec succès.")
if cnt_ignores > 0:
    print(f" - {cnt_ignores} fichier(s) ignoré(s).")
print("=" * 40)