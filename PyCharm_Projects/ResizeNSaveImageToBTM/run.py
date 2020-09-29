# -*- coding: utf-8 -*-

"""
# https://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python
copy için şunlara bir bak: ("python file copy")
    https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
    https://datatofish.com/copy-file-python/
    https://www.techbeamers.com/python-copy-file/
"""

import os
from PIL import Image


bmp_ext = [".BMP"]
jpg_ext = [".JPG", ".JPEG"] #JPEG için dikkatli ol
png_ext = [".PNG"]
tif_ext = [".TIF"]
images_ext_list = tif_ext + bmp_ext + png_ext + jpg_ext

convertFiles_ext_list = tif_ext + bmp_ext + png_ext + [".JPEG"]
convertTo_ext = ".JPG"
convertTo_type = 'jpeg'


def del_file(path):
    if os.path.exists(path):
        os.remove(path)
        return True
    return False


def do_resize(path, base_width, background=False, bg_size=None, bg_color_rgb=(255, 255, 255)):
    img = Image.open(path)
    # dir_path, filename_full = os.path.split(path)
    # filename, ext = os.path.splitext(filename_full)
    w_size, h_size = img.size[0], img.size[1]
    if (base_width is not None) and (w_size > base_width):
        # path_OLD = os.path.splitext(path)[0] + "-OLD" + os.path.splitext(path)[1]
        # img_old = img.copy()
        # img_old.save(path_OLD, 'jpeg')
        # img_old.close()
        w_percent = (base_width / float(w_size))
        w_size_new = base_width
        h_size_new = int((float(h_size) * float(w_percent)))
        img = img.resize((w_size_new, h_size_new), Image.LANCZOS)
        if background:
            img_w, img_h = img.size
            background = Image.new('RGB', bg_size, bg_color_rgb)
            bg_w, bg_h = background.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
            background.paste(img, offset)
            img = background
        img.save(path)
    img.close()


def convert2jpg(filepath):
    ext = os.path.splitext(filepath)[1]
    img = Image.open(filepath)
    #
    w_size, h_size = img.size[0], img.size[1]
    print("## w_size:["+str(w_size)+"], h_size:["+str(h_size)+"]")
    #
    img = img.convert('RGB')
    if ext.upper() in convertFiles_ext_list:
        filepath_new = os.path.splitext(filepath)[0] + convertTo_ext
        img.save(filepath_new, convertTo_type, optimize=True, progressive=True)
    else:
        filepath_new = filepath
    img.close()
    return filepath_new


def get_image_path_list(dir_path):
    """
    For the given path, get the List of all files in the directory tree.
    :param dir_path:
    :return:
    :rtype: list
    """
    # create a list of file and sub directories
    # names in the given directory
    filepath_list = os.listdir(dir_path)
    all_files = list()
    # Iterate over all the entries
    for entry in filepath_list:
        # Create full path
        full_path = os.path.join(dir_path, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_image_path_list(full_path)
        else:
            if os.path.splitext(full_path)[1].upper() in images_ext_list:
                all_files.append(full_path)
    return all_files


def convert2jpg_dir(dir_path, base_width):
    filepath_list = get_image_path_list(dir_path)
    for filepath in filepath_list:
        #
        filepathBig = filepath
        filepathSmall = os.path.splitext(filepath)[0] + ".small" + os.path.splitext(filepath)[1]
        os.system('COPY /B "' + filepathBig + '" "' + filepathSmall + '"')
        #
        filepath_new = convert2jpg(filepathSmall)
        #
        print(("#" * 10) + "\n" + filepathBig + "\n" + filepath_new + "\n" + ("#" * 10))
        #
        do_resize(filepath_new, base_width)
        if os.path.splitext(filepathSmall)[1].upper() != convertTo_ext:
            del_file(filepathSmall)


base_width1 = 250
dir_path1 = r"C:\Users\nejat.gunaydin\Desktop\folder"
convert2jpg_dir(dir_path1, base_width1)
