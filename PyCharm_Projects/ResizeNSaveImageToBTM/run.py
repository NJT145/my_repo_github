import os

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


def doResize(filePath, baseWidth):
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
        img.save(filePath)
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


'''
For the given path, get the List of all files in the directory tree 
'''


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


def convertFiles2JPG(folderPath, baseWidth):
    listOfFiles = getListOfImageFiles(folderPath)
    for filePath in listOfFiles:
        filePath_new = convert2JPG(filePath)
        doResize(filePath_new, baseWidth)
        if os.path.splitext(filePath)[1].upper() != convertTo_ext:
            delFile(filePath)


baseWidth1 = 1000
dirName = r"C:\Users\nejat.gunaydin\Desktop\folder"
convertFiles2JPG(dirName, baseWidth1)
