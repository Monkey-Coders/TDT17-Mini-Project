import os
import torch

from xml.etree import ElementTree
from xml.dom import minidom
import collections
import shutil
from random import randrange, sample
from PIL import Image
from tqdm import tqdm

# D00 = Longitudinal Crack
# D10 = Transverse Crack
# D20 = Alligator Crack
# D40 = Potholes

SIZE = 1000

classes = ["D00", "D10", "D20", "D40"]
idx_to_class = {i:j for i, j in enumerate(classes)}
class_to_idx = {value:key for key,value in idx_to_class.items()}

chosen_countries = ["Norway", "Japan"]

dataset_path = "../../../../projects/vc/courses/TDT17/2022/open/RDD2022/"

if not os.path.exists("RDD_TO_YOLO"):
   os.makedirs("RDD_TO_YOLO")
   os.makedirs("RDD_TO_YOLO/images")
   os.makedirs("RDD_TO_YOLO/labels")


for country in tqdm(os.listdir(dataset_path), desc=f"Country: "):
  if country.endswith(".zip"):
    continue
  if country not in chosen_countries:
    continue
  print(f"Creating annotations for country {country}") 
  for image in tqdm(os.listdir(f"{dataset_path}/{country}/train/images"), desc=f"Image in {country}: "):
    image_name = image.split(".")[0]
    annotation_path = f"{dataset_path}/{country}/train/annotations/xmls/{image_name}.xml"
    
    try:
      infile_xml = open(annotation_path)
    except FileNotFoundError:
      continue
    tree = ElementTree.parse(infile_xml)
    root = tree.getroot()

    print_buffer = []

    im = Image.open(f"{dataset_path}/{country}/train/images/{image}").convert('RGB')
    im_w, im_h = im.size
    for obj in root.iter('object'):
      damage_type = obj.find("name").text
      bbox = obj.find("bndbox")
      xmin = int(float(bbox.find("xmin").text))
      ymin = int(float(bbox.find("ymin").text))
      xmax = int(float(bbox.find("xmax").text))
      ymax = int(float(bbox.find("ymax").text))

      center_x = (xmin + xmax) / 2 
      center_y = (ymin + ymax) / 2
      width = xmax - xmin
      height = ymax - ymin
      
      if damage_type in class_to_idx:
        class_id = class_to_idx[damage_type]

        print_buffer.append("{} {} {} {} {}".format(class_id, center_x/im_w, center_y/im_h, width/im_w, height/im_h))
    if len(print_buffer) > 0:
      annotation_file = open(f"RDD_TO_YOLO/labels/{image_name}.txt", "w")
      annotation_file.write("\n".join(print_buffer))
      annotation_file.close()
      im.thumbnail((SIZE,SIZE), Image.LANCZOS)
      im.save(f"RDD_TO_YOLO/images/{image_name}.jpg", "JPEG")
print("Done annotating file")