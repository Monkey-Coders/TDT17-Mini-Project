from PIL import Image, ImageFont, ImageDraw, ImageEnhance
name = Norway_000001
img_path=f"RDD_yolo_v2/images/{name}.jpg"
lbl_path=f"RDD_yolo_v2/labels/{name}.txt"
classes = ["D00", "D10", "D20", "D40"]

source_img = Image.open(img_path).convert("RGB")

draw = ImageDraw.Draw(source_img)

with open(lbl_path) as f:
    for line in f.readlines():
        c, x, y, w, h = map(float, line.split(' '))
        x_min = x - (w//2)
        x_max = x + (w//2)
        y_min = y - (h//2)
        y_max = y + (h//2)
        draw.rectangle(((x_min, y_min), (x_max, y_max)), outline ="red", width=5)
        draw.text((x, y), classes[int(c)])

source_img.save("output.jpg", "JPEG")