import pyttsx3,PyPDF2



pdfreadObj = open('book.pdf', 'rb')
pdfReader= PyPDF2.PdfFileReader(pdfreadObj)
speaker = pyttsx3.init()

for page_number in range(pdfReader.numPages):
    text = pdfread.getPage(page_num).extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text,'voice.mp3')
speaker.runAndWait()
speaker.stop()