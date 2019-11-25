import os

# https://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python

from PIL import Image

bmp_ext = [".BMP"]
jpg_ext = [".JPG"]
png_ext = [".PNG"]
tif_ext = [".TIF"]
imageFiles_ext_list = tif_ext + bmp_ext + png_ext + jpg_ext

convertFiles_ext_list = tif_ext + bmp_ext + png_ext
convertTo_ext = ".JPG"


def delFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)
        return True
    return False


def doResize(filePath, baseWidth, background=False, bg_size=None, bg_colorRBG=(255, 255, 255)):
    img = Image.open(filePath)
    # fileName, ext = os.path.split(filePath)[1], os.path.splitext(filePath)[1]
    w_size, h_size = img.size[0], img.size[1]
    if (baseWidth is not None) and (w_size > baseWidth):
        # filePath_OLD = os.path.splitext(filePath)[0] + "-OLD" + os.path.splitext(filePath)[1]
        # img_old = img.copy()
        # img_old.save(filePath_OLD, 'jpeg')
        # img_old.close()
        w_percent = (baseWidth / float(w_size))
        w_size_new = baseWidth
        h_size_new = int((float(h_size) * float(w_percent)))
        img = img.resize((w_size_new, h_size_new), Image.LANCZOS)
        if background:
            img_w, img_h = img.size
            background = Image.new('RGB', bg_size, bg_colorRBG)
            bg_w, bg_h = background.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
            background.paste(img, offset)
            img = background
        img.save(filePath)
    img.close()

def img_resize_fitsize(img, size, background=False, bg_colorRBG=(255, 255, 255)):
    w_size, h_size = img.size[0], img.size[1]
    baseWidth = size[0]
    baseHeight = size[1]
    if (w_size > baseWidth):
        w_percent = (baseWidth / float(w_size))
        w_size = baseWidth
        h_size = int((float(h_size) * float(w_percent)))
    if (h_size > baseHeight):
        h_percent = (baseHeight / float(h_size))
        h_size = baseHeight
        w_size = int((float(w_size) * float(h_percent)))
    if (w_size > baseWidth):
        w_percent = (baseWidth / float(w_size))
        w_size = baseWidth
        h_size = int((float(h_size) * float(w_percent)))
    img = img.resize((w_size, h_size), Image.LANCZOS)
    if background:
        img_w, img_h = img.size
        background = Image.new('RGB', size, bg_colorRBG)
        bg_w, bg_h = background.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        background.paste(img, offset)
        img = background
    return img

def doResize2(filePath, width, height, resultPath=None):
    if resultPath is None:
        resultPath = filePath
    img = Image.open(filePath)
    # fileName, ext = os.path.split(filePath)[1], os.path.splitext(filePath)[1]
    w_size, h_size = img.size[0], img.size[1]
    img = img.resize((width, height), Image.LANCZOS)
    img.save(resultPath)
    img.close()

def convert2JPG(filePath):
    ext = os.path.splitext(filePath)[1]
    img = Image.open(filePath)
    img = img.convert('RGB')
    if ext.upper() in convertFiles_ext_list:
        filePath_new = os.path.splitext(filePath)[0] + convertTo_ext
        img.save(filePath_new, 'jpeg', optimize=True, progressive=True)
    else:
        filePath_new = filePath
    img.close()
    return filePath_new


def getListOfImageFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfImageFiles(fullPath)
        else:
            if os.path.splitext(fullPath)[1].upper() in imageFiles_ext_list:
                allFiles.append(fullPath)
    return allFiles


def convertFiles2JPG(folderPath, size, background=False, bg_colorRBG=(255, 255, 255)):
    listOfFiles = getListOfImageFiles(folderPath)
    for filePath in listOfFiles:
        filePath_new = convert2JPG(filePath)
        img = Image.open(filePath_new, 'r')
        img = img_resize_fitsize(img, size, background, bg_colorRBG)
        img.save(filePath_new)
        if os.path.splitext(filePath)[1].upper() != convertTo_ext:
            delFile(filePath)

def createEmptyImg(filePath, height, width, colorRBG=(255, 255, 255), fileType='PNG'):
    background = Image.new('RGB', (width, height), colorRBG)
    background.save(filePath, fileType)

def doFunctionForSomeFileTypes(function, fileTypes, *args, **kwargs):
    pass

baseWidth1 = 950
dirName = r"C:\Users\nejat.gunaydin\Desktop\folder"
dirName2 = r"C:\Users\nejat.gunaydin\Desktop\folder\DENEME.JPG"
dirName3 = r"C:\Users\nejat.gunaydin\Desktop\folder\KDENEME.JPG"
# convertFiles2JPG(dirName, baseWidth1)
#doResize(dirName2, 600)
#doResize2(dirName3, 59, 59)
# listOfFiles = getListOfImageFiles(dirName)
# for filePath in listOfFiles:
#     dirPath, fileNameWithExt = os.path.split(filePath)
#     fileName, ext = os.path.splitext(fileNameWithExt)
#     filePath2 = os.path.join(dirPath, fileName + '_k' + ext)
#     doResize2(filePath, 59, 59, resultPath=filePath2)
#createEmptyImg(r"C:\Users\nejat.gunaydin\Desktop\testIMG.JPG", 456, 961, colorRBG=(0, 0, 0), fileType="JPEG")
colorRBG=(0, 0, 0)
size = (500, 10000)
convertFiles2JPG(dirName, size, background=False, bg_colorRBG=colorRBG)

