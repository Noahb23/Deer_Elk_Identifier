#!/usr/bin/python3
import jetson_inference
import jetson_utils
import random

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
opt = parser.parse_args()
img = jetson_utils.loadImage(opt.filename)
net = jetson_inference.imageNet(model="model.onnx",labels="labels.txt",input_blob="input_0",output_blob="output_0")
class_idx, confidence = net.Classify(img)
class_desc = net.GetClassDesc(class_idx)
if class_desc=="deer":
    deerfacts = ["A female deer is called a doe",
                 "Deer antler are the fastest growing tissue on Earth", 
                 "Deer antlers grow a inch every two days", 
                 "Deers are herbivores", 
                 "Deers can jump to up to 10 feet in the air",
                 "There are 30 million deer in the world",
                 "There are around 40 species of deer",
                 ]
    rand=random.randint(0,len(deerfacts)-1)
    print(deerfacts[rand])

if class_desc=="elk":
    elkfacts = ["Elk can live up to 20 years old",
                "Male elk usually weight around 700 pounds",
                "Elk are great swimmers",
                "Elk have incredible hearing",
                "Elk antlers grow to 4 feet long",
                "Elk are very fast runners",
                "Elk perfer to live in big groups"]
    rand=random.randint(0,len(elkfacts)-1)
    print(elkfacts[rand])
print("image is recognized as "+ str(class_desc) +" (class #"+ str(class_idx) +") with " + str(confidence*100)+"% confidence")