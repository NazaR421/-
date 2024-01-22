from PIL import Image
from PIL import ImageFilter


file_path = "pes.jpg"  # Update with the correct path

try:
    with Image.open(file_path) as pic_original:
        print("Розмір:", pic_original.size)
        print("Формат:", pic_original.format)
        print("Тип:", pic_original.mode)
        pic_original.show()

        pes_gray = pic_original.convert("L")
        pes_gray.save("pes1.jpg")
        pes_gray.show()

        pes_blured=pic_original.filter(ImageFilter.BLUR)
        pes_blured.save("pes2.jpg")
        pes_blured.show()

        pes_up=pic_original.transpose(Image.ROTATE_180)
        pes_up.save("pes3.jpg")
        pes_up.show()


except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
