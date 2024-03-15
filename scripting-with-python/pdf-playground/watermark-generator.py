from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader('merge_file.pdf')
page_indices = list(range(0, len(reader.pages)))

writer = PdfWriter()
for index in page_indices:
    content_page = reader.pages[index]
    mediabox = content_page.mediabox

    # You need to load it again, as the last time it was overwritten
    watermark = PdfReader('wtr.pdf')
    image_page = watermark.pages[0]

    image_page.merge_page(content_page)
    image_page.mediabox = mediabox
    writer.add_page(image_page)
    print(f'Processing Done... page {index+1}')

with open('watermark.pdf', "wb") as fp:
    writer.write(fp)
