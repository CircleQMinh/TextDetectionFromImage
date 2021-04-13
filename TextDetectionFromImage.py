# Import required packages
import cv2
import pytesseract
import regex as re

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

# Read image from which text needs to be extracted
img = cv2.imread("IMG/2.png")

img = cv2.resize(img, dsize=None, fx=1, fy=1)
# Preprocessing the image starts
# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Appplying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()
open('mytext.txt', 'w').close()

checkRec = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #cv2.imshow('111', rect)
    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]
    checkRec.append(cropped)

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped , lang='ENG')
    # Appending the text into file
    with open("mytext.txt", "a", encoding="utf-8") as f:
        f.write(text)
        f.write("\n")
        f.close
    #print(text)
i=0
for img in checkRec:
    cv2.imwrite('logo/logo'+str(i)+'.png',img)
    i = i + 1
   


def checkemail(email):
    # pass the regular expression
    # and the string in search() method
    regex = '([@]|(^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$) )'
    if(re.search(regex, email)):
        return True
    else:
        return False
    

def checkphone(e):
    # pass the regular expression
    # and the string in search() method
    regex = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}|\d{4}[-\.\s]??\d{3})'
    
    if(re.search(regex, e)):
        return True
    else:
        return False
def checkweb(e):
    # pass the regular expression
    # and the string in search() method
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))|(www+)"     
    if(re.search(regex, e)):
        return True
    else:
        return False
def checkAddress(e):
    regex = r"(\d{1,4}( \w+){1,5}, (.*), ( \w+){1,5}, (AZ|CA|CO|NH), [0-9]{5}(-[0-9]{4})?)|(add+)|(Add+)|(Dia+)|(\d{,4}[-\.\s]+\D)"
    if(re.search(regex,e)):
        return True
    else:
        return False
def checkName(e):
    regex = r"((^[A-z]{2,10}[\s]+[A-z]{3,10}[\s]+[A-z]{3,10}[\s]+[A-z]{3,10}$)|(^[A-z]{2,10}[\s]+[A-z]{3,10}[\s]+[A-z]{3,10}$)|(^[A-z]{3,10}[\s]+[A-z]{3,10}$))"
    if(re.search(regex,e)):
        return True
    else:
        return False

arrText = []

file = open('mytext.txt', 'r',encoding="utf-8")
Lines = file.readlines()

for line in Lines:
    if len(line.strip()) != 0 and line.strip() not in arrText:
        arrText.append(line.strip())

arrDes = []
print("\nWebsite Found :")
for line in arrText:
    if  line.strip() not in arrDes and checkweb(line.strip()):
        arrDes.append(line.strip())
        print('\t' + line.strip())
print("\nPhone Found :")
for line in arrText:
    if line.strip() not in arrDes and checkphone(line.strip()):
        arrDes.append(line.strip())
        print('\t' + line.strip())
print("\nEmail Found :")
for line in arrText:
    if line.strip() not in arrDes and checkemail(line.strip()):
        arrDes.append(line.strip())
        print('\t' + line.strip())
print("\nName Found :")
for line in arrText:
    if line.strip() not in arrDes and checkName(line.strip()):
        arrDes.append(line.strip())
        print('\t' + line.strip())

print("\nAddress Found :")
for line in arrText:
    if line.strip() not in arrDes and checkAddress(line.strip()):
        arrDes.append(line.strip())
        print('\t' + line.strip())

print('\n\n\n\n')
print("All Result :")

for line in arrText:
     print('\t' + line.strip())
cv2.imshow('Pic',im2)
cv2.waitKey()


