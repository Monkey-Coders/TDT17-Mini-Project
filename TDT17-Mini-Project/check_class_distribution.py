import os
from tqdm import tqdm

folder_name = "RDD_TO_YOLO_ALL"
if not os.path.exists(f"{folder_name}"):
    print("FOLDER DOES NOT EXIST")
    exit()
classes = ["D00", "D10", "D20", "D40"]
for datasplit in os.listdir(folder_name):
    classes_count = {}
    for label in os.listdir(f"{folder_name}/{datasplit}/labels"):
        with open(f"{folder_name}/{datasplit}/labels/{label}", "r") as f:
            lines = f.readlines()
            for line in lines:
                class_id = int(line.split(" ")[0])
                _class = classes[int(class_id)]
                if _class not in classes_count:
                    classes_count[_class] = 1
                else:
                    classes_count[_class] += 1
    print(datasplit, classes_count)