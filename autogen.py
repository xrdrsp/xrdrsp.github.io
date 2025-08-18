import os

directory = input()

if not os.path.isdir(directory):
    print("The specified directory does not exist.")
    exit(1)

print("This action can be dangerous. Do you confirm that the directory is correctly entered? (y/n)", end=' ')
o = input().strip().lower()
if (o != 'y'):
    print("Exiting without changes.")
    exit(0)

for path, folders, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            full_path = os.path.join(path, file)
            with open(full_path, 'r', encoding="utf-8") as f:
                lines = f.readlines()
                ext_index = []
                body_index = []
                title = ''

                for line in lines:
                    
                    if '<title>' in line and '</title>' in line:
                        title = line
                    if 'id="ext"' in line:
                        ext_index.append(lines.index(line))

                    if line.endswith('body>') or line.endswith('body>\n'):
                        body_index.append(lines.index(line))

                if len(ext_index) == 2:
                    ext = lines[ext_index[0] : ext_index[1] + 1]
                else:
                    ext = []

                head = [
                    '<html>\n',
                    '    <div id="header"></div>\n',
                    '    <head>\n',
                    '        <meta charset="utf-8">\n',
                    f'        {title.strip()}\n',
                    '        <script src="/node_modules/jquery.js"></script>\n',
                    '        <script>\n',
                    '            $("#header").load("/head.html");\n',
                    '        </script>\n',
                ] + ext + [
                    '    </head>\n'
                ]
                foot = [
                    '    <div id="footer"></div>\n',
                    '    <foot>\n',
                    '        <script>\n',
                    '            $("#footer").load("/foot.html");\n',
                    '        </script>\n',
                    '    </foot>\n',
                    '</html>'
                ]
                new_lines = head + lines[body_index[0] : body_index[1] + 1] + foot

            with open(full_path, 'w', encoding="utf-8") as f:
                f.writelines(new_lines)

            print(f"Processed file: {full_path}")

print("All HTML files processed successfully.")