from io import BytesIO
from tkinter import *
from tkinter import Label
import requests
from PIL import ImageTk
from pygame.display import update


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None


def open_new_window():
    img = load_image(url)

    if img:
        new_widow = Toplevel()
        new_widow.title('Картинка с котиком')
        new_widow.geometry('600x480')
        label = Label(new_widow, image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()

window = Tk()
window.title('Cats!')
window.geometry('600x480')



# update_button = Button(text = 'Обновить', command=set_image)
# update_button.pack()

menu_bar = Menu(window)
window.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=set_image)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)

url = 'https://cataas.com/cat'

img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

set_image()
window.mainloop()
