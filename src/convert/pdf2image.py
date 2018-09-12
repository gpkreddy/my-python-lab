# from pdf2image import convert_from_path

# pages = convert_from_path(r'C:\code\trust-tax\Interns Work\pipenv-test\assets\in\pdf', 500)

# for page in pages:
#     page.save('out.jpg', 'JPEG')



# from pdf2jpg import pdf2jpg
# inputpath = r"C:\code\trust-tax\Interns Work\pipenv-test\assets\in\pdf"
# outputpath = r"C:\code\trust-tax\Interns Work\pipenv-test\assets\out"
# # To convert single page
# result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="1")
# print(result)

# # To convert multiple pages
# result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="1,0,3")
# print(result)

# # to convert all pages
# result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")
# print(result)

from wand.image import Image
# Converting first page into JPG
with Image(filename=r"C:\code\trust-tax\Interns Work\pipenv-test\files\in\pdf\allnormal.pdf") as img:
     img.save(filename=r"\temp.jpg")
# Resizing this image
with Image(filename=r"\temp.jpg") as img:
     img.resize(200, 150)
     img.save(filename=r"\thumbnail_resize.jpg")