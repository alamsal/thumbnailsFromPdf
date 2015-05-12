#Install Ghost script before python package's installation from: http://www.a-pdf.com/convert-to-pdf/gs.exe
import sys,os
from wand.image import Image
from wand.display import display
from wand.color import Color

fileDirectory = "D:/files/"
inFileName = "infile.pdf"
outFileName = "outfile.png"

filesInDir = os.listdir(fileDirectory)

for file in filesInDir:
    if file.endswith(".pdf"):
        print(file)
        imageFromPdf = Image(filename=fileDirectory+file)

        pages = len(imageFromPdf.sequence)
        print(pages)

        pages = 1
        
        image = Image(
            width = imageFromPdf.width,
            height = imageFromPdf.height*pages          
           
        )
        
        for i in range(pages):
            image.composite(
                imageFromPdf.sequence[i],
                top = imageFromPdf.height * i,
                left = 0
            )
            
        image.resize(250,250)
        image.alpha_channel = False
        image.format = 'png'
        print(image.size)
        image.background_color = Color('pink')
        
        image.type = 'grayscale'
        image.caption = file.split('.')[0]
        image.save(filename = fileDirectory+file.split('.')[0]+".png")

        image.clear()
        image.close()

        #display(image)
