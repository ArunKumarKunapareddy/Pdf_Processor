import PyPDF2
import tkinter
from datetime import datetime
from _datetime import timedelta
from tkinter import filedialog
import sqlite3
class PDFProcessing:
    def Encry(self):
        # pdf_in_file = open("sample_one.pdf", 'rb')
        connection = sqlite3.connect("BBI.db")
        # query = """Create table Pdf_Processor("file_name" text, "file_size" integer,"time_of_encry" time)"""
        # execution = connection.execute(query)
        # connection.commit()
        # connection.close()
        root = tkinter.Tk()
        root.withdraw()
        f_name = filedialog.askopenfilename()
        try:

            pdf_in_file = open(f_name,'rb')

            inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
            pages_no = inputpdf.numPages
            output = PyPDF2.PdfFileWriter()

            for i in range(pages_no):
                inputpdf = PyPDF2.PdfFileReader(pdf_in_file)

                output.addPage(inputpdf.getPage(i))
                output.encrypt('password')

                with open("Sample_Protected.pdf","wb") as outputStream:
                    output.write(outputStream)
        except:
            print("File open Error")
        size = os.path.getsize("Sample_Protected.PDF")
        print(size)
        current_time = datetime.now()
        # print(current_time)
        # print(type(current_time))

        Modified_time = current_time.replace(microsecond=0)
        #print(Modified_time)

        added_current_time = Modified_time + timedelta(minutes=330)
        # print(added_current_time)
        # print(type(added_current_time))

        my_time_format = "%y_%m_%d_%H_%M_%S"
        converted_format_time = datetime.strftime(added_current_time, my_time_format)
        print(converted_format_time)
        # print(type(converted_format_time))
        file_name=os.path.basename(f_name)
        print(file_name)
        print(f_name)
        connection.execute("insert into Pdf_Processor values(?,?,?)", (file_name, size, converted_format_time))
        connection.commit()
        connection.close()
        pdf_in_file.close()


pdf_Process=PDFProcessing()
pdf_Process.Encry()