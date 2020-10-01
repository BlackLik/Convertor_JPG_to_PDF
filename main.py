import os
from PIL import Image
from PyPDF2 import PdfFileMerger


def img_to_pdf(file_name):
    file_name = file_name
    name = file_name.split('.')[0]
    im = Image.open(file_name)
    size = 1920, 1080
    im.thumbnail(size)
    if not os.path.exists('img2pdf'):
        os.makedirs("img2pdf")
    new_file = ''.join(['img2pdf/', name, '.pdf'])
    Image.Image.save(im, new_file, "PDF", resolution=100.0)
    print("Файл обработан")


files = [f for f in os.listdir('./') if f.endswith('.jpg')]
files.sort(key=lambda name: int(name.split('.')[0]))
for file in files:
    img_to_pdf(file)

files = [f for f in os.listdir('./img2pdf/') if f.endswith('.pdf')]
files.sort(key=lambda name: int(name.split('.')[0]))

merger = PdfFileMerger()
for file in files:
    merger.append("./img2pdf/" + file)

merger.write('result.pdf')
merger.close()
print('Процесс завершён')
