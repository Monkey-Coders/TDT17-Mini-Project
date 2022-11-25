import os

from PIL import Image
from tqdm import tqdm

dataset_path = "../../../../projects/vc/courses/TDT17/2022/open/RDD2022/Norway/test/images"
label_path = "../RDD_YOLO_TEST/TEST_x/labels"

classes = ["D00", "D10", "D20", "D40"]
CLASS_TO_ID = {
    "D00": 1,
    "D10": 3,
    "D20": 5,
    "D40": 6,
}

with open(f'output.txt', 'w') as f:
    f.write("")

for label in tqdm(os.listdir(f"{label_path}"), desc=f"Image in Norway: "):
    name = label.split(".")[0]
    im = Image.open(f"{dataset_path}/{name}.jpg").convert('RGB')
    im_w, im_h = im.size
    
    with open(f'output.txt', 'a') as f:
        f.write(f'{name}.jpg,')
        
        with open(f"{label_path}/{label}", "r") as l:
            for line in l.readlines():
                data = line.split(" ")
                c = int(data[0])
                cx = float(data[1])
                cy = float(data[2])
                w = float(data[3])
                h = float(data[4])
                minx = int((cx - w/2) * im_w)
                maxx = int((cx + w/2) * im_w)
                miny = int((cy - h/2) * im_h)
                maxy = int((cy + h/2) * im_h)
                text = f'{CLASS_TO_ID[classes[c]]} {minx} {miny} {maxx} {maxy} '
                f.write(text)
            
        f.write(f'\n')