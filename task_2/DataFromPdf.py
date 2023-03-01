# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:12:51 2023

@author: elham.nourghassemi
"""

from PyPDF2 import PdfReader

#Now give the pdf name
path = "C:/Users/elham.nourghassemi/Documents/Python Scripts/assignments/tasks/task_2/"

reader = PdfReader("GeoBase_NHNC1_Data_Model_UML_EN.pdf")
page = reader.pages[3]
print(page.extract_text())

print(page.extract_text((0, 90)))

parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)


page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)

# pdfFileObj = open(path+'GS-Revenue-collection-for-July-2020.pdf', 'rb')

# pdfReader = PyPDF2.PdfReader(pdfFileObj)
# print(len(pdfReader.pages)) # will give total number of pages in pdf

# pageObj = pdfReader.pages[0]
# print(pageObj)

# print("my", pageObj.extract_text(0))

# text = (pageObj.extract_text())
# text = text.split(".")
# print(text)

# search_keywords=['GST','Ministry ','%','Revenue ','Year','Growth']

# for sentence in sentences:
#     lst = []
#     for word in search_keywords:
#         if word in sentence:
#             lst.append(word)
#     print('{0} key word(s) in sentence: {1}'.format(len(lst), ', '.join(lst)))
#     print(sentence + "\n")