import os

directory = input()

for path, folders, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            full_path = os.path.join(path, file)
            with open(full_path, 'r', encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if '<title>' in line and '</title>' in line:
                        title = line
                    if line.endswith('<body>') or line.endswith('<body>\n'):
                        body_start = lines.index(line)
                    if line.startswith('</body>') or line.endswith('</body>\n'):
                        body_end = lines.index(line)
                
