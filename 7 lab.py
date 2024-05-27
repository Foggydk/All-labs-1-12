from PIL import Image
def task_1():

    file_path = "C:/Users/dkeyd/OneDrive/Desktop/Абобы/Обои/1x/Обои.png"

    img = Image.open(file_path)

    print("Размер изображения:", img.size)
    print("Формат:", img.format)
    print("Цветовая модель:", img.mode)

    img.show()

def task_2():
    original = Image.open("C:/Users/dkeyd/OneDrive/Desktop/Абобы/Обои/1x/Обои.png")

    smaller = original.resize((int(original.width / 3), int(original.height / 3)))

    mirror1 = original.transpose(Image.FLIP_LEFT_RIGHT)

    mirror2 = original.transpose(Image.FLIP_TOP_BOTTOM)

    smaller = smaller.convert('RGB')
    smaller.save("smaller.jpg")

    mirror1 = mirror1.convert('RGB')
    mirror1.save("mirror1.jpg")

    mirror2 = mirror2.convert('RGB')
    mirror2.save("mirror2.jpg")

    print("Изображения успешно сохранены.")

def task_3():
    filename = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in filename:
        with Image.open(file) as img:
            img.load()
            new_file = img.filter(img.SHARPEN)
            new_file.show()

def task_4():
    water_path = "C:/Users/dkeyd/OneDrive/Desktop/Абобы/Обои/1x/Обои.png"
    base2 = "4.jpg"
    output_image_path = "water_4.jpg"

    with Image.open(water_path) as water:
        water.load()

    base = Image.open(base2)
    base = base.resize((water.size[0], water.size[1])).convert("L")

    base1 = base.resize((100, 100))

    with Image.open(base2) as background:
        background.load()

        background.paste(base1, (50, 50))

        background.save(output_image_path)
        background.show()

print(task_4())