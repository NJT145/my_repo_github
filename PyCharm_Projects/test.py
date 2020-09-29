# -*- coding: utf-8 -*-

import os
import copy
from typing import Dict, List, Tuple

#print("hello world")

path1 = os.path.join(os.getcwd(), "paths.txt")
dir_path1 = r"C:\Users\nejat.gunaydin\Desktop\folder1"


def cp_filename(path):
    replace_path = path
    dir_path, filename_full = os.path.split(path)
    filename, ext = os.path.splitext(filename_full)
    if os.path.exists(path):
        i = 1
        while os.path.exists(os.path.join(dir_path, (filename + "(" + str(i) + ")" + ext))):
            i += 1
        replace_path = os.path.join(dir_path, (filename + "(" + str(i) + ")" + ext))
    return replace_path


def is_valid(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        if s != path_replace(s):
            return False
        return True


def path_replace(path):
    replace_map = {
        ord(u"'"): u"",
        ord(u" "): u"",
        ord(u"ç"): u"c",
        ord(u"Ç"): u"C",
        ord(u"ğ"): u"g",
        ord(u"Ğ"): u"G",
        ord(u"ı"): u"i",
        ord(u"İ"): u"I",
        ord(u"ö"): u"o",
        ord(u"Ö"): u"O",
        ord(u"ş"): u"s",
        ord(u"Ş"): u"S",
        ord(u"ü"): u"u",
        ord(u"Ü"): u"U",
    }
    return path.translate(replace_map)

def main1(path):
    path_list_dict = {"Clip": [], "Photos": []}
    clip_start = "assets\\images\\Clip\\"
    photos_start = "assets\\images\\Photos\\"
    if os.path.exists(path):
        f = open(path, "r", encoding='utf-8')
        parts = f.read().split("        1 file(s) copied.\n")
        for part in parts:
            path_href, path_src, category, description, data_size = "", "", "", "", ""
            #
            txt_split = part.strip().split("\n##########\n")
            sizes_txt, paths_txt = txt_split[0], txt_split[1].rstrip("#").strip().split("\n")
            #
            w_size= sizes_txt.strip().split(",")[0].split(":")[1].lstrip("[").rstrip("]")
            h_size = sizes_txt.strip().split(",")[1].split(":")[1].lstrip("[").rstrip("]")
            data_size = w_size + "x" + h_size
            #
            path_href, path_src = paths_txt[0], paths_txt[1]
            description = path_href.rsplit("\\", 1)[1].split(".")[0]
            if path_href.startswith(photos_start):
                category = path_src[len(photos_start):].split("\\")[0].lower()
            #
            dict_key = None
            if path_href.startswith(clip_start): dict_key = "Clip"
            elif path_href.startswith(photos_start): dict_key = "Photos"
            if dict_key is not None:
                path_list_dict[dict_key].append((path_href, path_src, category, description, data_size))
        f.close()
    return path_list_dict


def main2(path_list: List[Tuple]) -> str:
    return_value = ""
    item_template = """
        <div class="grid__item hidden {{category}}" data-size="{{data_size}}">
            <div class="single-photo">
                <div class="photo-overlay">
                    <div aria-hidden="true" class="zoom-icon icon_zoom-in_alt"></div>
                </div>
                <a href="{{path_href}}" class="img-wrap">
                    <img src="{{path_src}}" alt="{{img_alt}}" />
                    <%--<div class="description description--grid">{{description}}</div>--%>
                </a>
            </div>
        </div>
        """
    #
    path_list.sort()
    count_num = 0
    for path_info in path_list:
        path_href, path_src, category, description, data_size = path_info
        filepath_href = os.path.join(dir_path1, path_href)
        filepath_src = os.path.join(dir_path1, path_src)
        if os.path.exists(filepath_href) or os.path.exists(filepath_src):
            if not os.path.exists(filepath_src): raise Exception("small image file not found")
            if not os.path.exists(filepath_href): raise Exception("big image file not found")
            count_num += 1
            if not is_valid(path_href):
                filepath_href_old = copy.copy(filepath_href)
                filepath_src_old = copy.copy(filepath_src)
                path_href = path_replace(path_href)
                path_src = path_replace(path_src)
                filepath_href = cp_filename(os.path.join(dir_path1, path_href))
                filepath_src = cp_filename(os.path.join(dir_path1, path_src))
                os.rename(filepath_href_old, filepath_href)
                os.rename(filepath_src_old, filepath_src)
            return_value += (item_template.strip()
                             .replace("{{path_href}}", path_href)
                             .replace("{{path_src}}", path_src)
                             .replace("{{category}}", category)
                             .replace("{{description}}", description)
                             .replace("{{data_size}}", data_size)
                             .replace("{{img_alt}}", "img" + str(count_num))
                             )
    return return_value

#print(main2(main1(path1)["Clip"]))
#print(main2(main1(path1)["Photos"]))
i1 = "WhatsApp Video 2020-08-03 at 15.17.46.mp4"
print(path_replace(i1))
print(path_replace(i1)==i1)