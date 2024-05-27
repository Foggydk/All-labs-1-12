from PIL  import Image
def task_1():
    def imageobr(input_image, output_image, left, top, right, bottom):
        image = Image.open(input_image)
        image1 = image.crop((left, top, right, bottom))
        image1.save(output_image)

    image2 = "7ae9a03e9eadb755ff7d4cd340e40fee.jpg"

    left = 180
    top = 70
    right = 385
    bottom = 363

    image3 = "обрезанная_открытка.jpg"

    imageobr(image2, image3, left, top, right, bottom)

    print("Изображение успешно обрезано и сохранено")

def task_2():
    otkritki = {
        "День рождения": "dr.jpg",
        "Новый год": "ng.jpg",
        "8 Марта": "8 mar.jpg",
        "День победы": "denpob.jpg"
    }

    prazdnik = input("К какому празднику вам нужна открытка? ")

    if prazdnik in otkritki:
        print(f"Вы выбрали праздник '{prazdnik}'. Открытка к этому празднику: {otkritki[prazdnik]}")
    else:
        print("Извините, у нас нет открытки к указанному празднику.")

def task_3():
    image = Image.open(r'8 mar.jpg')
    draw = ImageDraw.Draw(party)
    x = input("введите имя которое нужно вписать: ")
    text = str(x) + ', поздравляю! '
    font = r"ofont.ru_Bubblez-Graffiti.ttf"
    font = ImageFont.truetype(font_path, size=20)
    y = draw.textlength(text, font=font)
    z = image.size
    w = (z[0] // 2) - (y // 2)
    image.text((w, 10), text, font=font, fill=("#EEE8AA"))
    image.save(r'C:\Users\Danil\Pycharm\lab8')
    image.show()


print(task_3())