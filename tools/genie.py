#!/Users/sdasan/abc/venv/bin/python3
import json 
import os
from os import listdir
import cv2
from PIL import Image
import numpy as np
import argparse
import sys


def text_to_img(args):
    if not os.path.exists(args['outDir']):
        os.makedirs(args["outDir"])
    content_file = open(args['template'],'r')
    content = content_file.read()
    with open(args["data"]) as data_file:
        lines = data_file.readlines()
        indx = 1
        for line in lines:
            tmp = content.replace("{LETTER}", line.strip())
            file_name = str(indx) + "_"+args['outFileSuffix']
            indx = indx + 1
            f = open("_temp.html", "w")
            f.write(tmp)
            f.close()
            cmd = 'webkit2png _temp.html -F -o '+os.path.join(args['outDir'],file_name)
            os.system(cmd)
    if os.path.exists("_temp.html"):
        os.remove("_temp.html")

def edge_detection(args):
    if args["verbose"]: print("Executing edge detection.")
    if not os.path.exists(args['outDir']):
        os.makedirs(args["outDir"])
    onlyfiles = [f for f in os.listdir(args['inDir']) if f.endswith('.png')]
    for file_name in onlyfiles:
        file_path = os.path.join(args['inDir'],file_name)
        if args["verbose"]: print("input img : ", file_path)
        img_obj = Image.open(file_path)
        img_arr = np.array(img_obj)
        # compute the median of the single channel pixel intensities
        v = np.median(img_arr)
        # apply automatic Canny edge detection using the computed median
        edges_arr = cv2.Canny(img_arr,10,200)
        inverted_img_arr = cv2.bitwise_not(edges_arr)
        final_img_obj = Image.fromarray(np.uint8(inverted_img_arr))
        output_file = os.path.join(args['outDir'],file_name)
        if args["verbose"]: print("output img : ", output_file)
        final_img_obj.save(output_file)

def trim_img(args):
    if args["verbose"]: print("Trim the image.")
    cmd = "mogrify -trim -bordercolor White -border 10x10 -colorspace RGB "+os.path.join(args['inDir'],"*.png")
    os.system(cmd)


def set_transparent(args):
    if args["verbose"]: print("Setting the transparent image.")
    cmd = "mogrify "+os.path.join(args['inDir'],"*.png")+" -transparent white "+os.path.join(args['inDir'],"*.png")
    os.system(cmd)

def main():
    parser = argparse.ArgumentParser(description='Genie Tool Help')
    parser.add_argument('--inDir', help='Input directory path Eg. --inDir=imgdir')
    parser.add_argument('--outDir', help='output directory path Eg. --outDir=imgdir')
    parser.add_argument('--data', help='config data.json Eg. --data=data.json')
    parser.add_argument('--template', help='template file Eg. --template=template.html')
    parser.add_argument('--outFileSuffix', help='template file Eg. --outFileSuffix=img', default="out_img")
    parser.add_argument('--verbose', help='Enable console log output. Eg. --verbose=True', default=False, type=bool)
    parser.add_argument('--do', help='Eg. edge_detection, trim, set_transparent, text_to_img --do=edge_detection', required=True)
    args = vars(parser.parse_args())    
    if args['do'] not in ['edge_detection', 'trim', 'set_transparent','text_to_img']:
        print("Unsupported operation - ", args['do'])
    if args['do'] == "edge_detection":
        edge_detection(args)
    if args['do'] == "trim":
        trim_img(args)
    if args['do'] == "set_transparent":
        set_transparent(args)
    if args['do'] == "text_to_img":
        text_to_img(args)

if __name__== "__main__":
     main()

