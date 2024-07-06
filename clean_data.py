import os
import re
from bs4 import BeautifulSoup

input_folder = '/home/kali/Desktop/webscrap'
output_folder = '/home/kali/Desktop/clean'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.html'):
        with open(os.path.join(input_folder, filename), 'r') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        main_col = soup.find('div', {'class': 'main-col'})

        if main_col:
            text = main_col.get_text()
            member_id_match = re.search(r'Member ID: (\d+)', text)

            if member_id_match:
                member_id = member_id_match.group(1)
                output_text = text[:text.index(f'Member ID: {member_id}')]

                with open(os.path.join(output_folder, f'{member_id}.txt'), 'w') as f:
                    f.write(output_text)

        print(f'Cleaned {filename}')
