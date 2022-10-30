from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfile
from PyPDF2 import PdfFileReader
#=================open file method======================
def openFile(): 
              
    file = askopenfilename(defaultextension=".pdf", 
                                          filetypes=[("Pdf files","*.pdf")])
    if file == "":  
        file = None
    else:
        fileEntry.delete(0,END)
        fileEntry.config(fg="blue")
        fileEntry.insert(0,file)
def convert():
    try:
        pdf = fileEntry.get()
        pdfFile = open(pdf, 'rb')
        # creating a pdf reader object
        pdfReader = PdfFileReader(pdfFile) 

        # creating a page object 
        pageObj = pdfReader.getPage(0) 
      
        # extracting text from page 
        extractedText= pageObj.extractText()
        readPdf.delete(1.0,END)
        readPdf.insert(INSERT,extractedText)

        # closing the pdf file object 
        pdfFile.close()
    except FileNotFoundError:
        fileEntry.delete(0,END)
        fileEntry.config(fg="red")
        fileEntry.insert(0,"Please select a pdf file first")
    except:
        pass

    
def save2word():
    text = str(readPdf.get(1.0,END))
    wordfile = asksaveasfile(mode='w',defaultextension=".doc", 
                                          filetypes=[("word file","*.doc"),
                                                     ("text file","*.txt"),
                                                     ("Python file","*.py")])
    
    if wordfile is None:
        return
    wordfile.write(text)
    wordfile.close()
    print("saved")
    fileEntry.delete(0,END)
    fileEntry.insert(0,"pdf Extracted and Saved...")



    
#=================== Front End Design
root = Tk()
root.geometry("600x350")
root.config(bg="light blue")
root.title("PDF Converter : SUPERTOOL")
root.resizable(0,0)
try:
    root.wm_iconbitmap("pdf2.ico")
except:
    print('icon file is not available')
    pass
file= ""
defaultText = "\n\n\n\n\t\t Your extracted text will apear here.\n \t\t     you can modify that text too."
#==============App Name==============================================================>>
appName = Label(root,text="PDF to WORD Converter ",font=('arial',20,'bold'),
                bg="light blue",fg='maroon')
appName.place(x=150,y=5)
#Select pdf file
labelFile = Label(root,text="Select Pdf File",font=('arial',12,'bold'))
labelFile.place(x=30,y=50)
fileEntry = Entry(root,font=('calibri',12),width=40)
fileEntry.pack(ipadx=200,pady=50,padx=150)
#===========button to access openFile method=================================
openFileButton = Button(root,text=" Open ",font=('arial',12,'bold'),width=30,
                    bg="sky blue",fg='green',command=openFile)
openFileButton.place(x=150,y=80)
#===========button to access convert method=================================
convert2Text = Button(root,text="Read",font=('arial',8,'bold'),
                   bg="RED",fg='WHITE',width=20,command=convert)
convert2Text.place(x=250,y=120)
#======================= Text Box to read pdf file and modify ===================>>
readPdf = Text(root,font=('calibri',12),fg='light green',bg='black',width=60,height=30,bd=10)
readPdf.pack(padx=20,ipadx=20,pady=20,ipady=20)
readPdf.insert(INSERT,defaultText)
#===============================Button to access save2word method=================
save2Word = Button(root,text="Save to Word File",font=('arial',10,'bold'),
                   bg="RED",fg='WHITE',command=save2word)
save2Word.place(x=255,y=320)

#===================halt window=============================>>
if __name__ == "__main__":
    root.mainloop()