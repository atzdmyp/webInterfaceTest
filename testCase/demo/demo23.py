import PIL.Image
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

"""
    图片转字符画
"""
root = Tk(className="图片转字符画")
path = StringVar()


def callback():
    """
    select directory
    :return:
    """
    global path
    path.set(askopenfilename())

Label(root, text="图片路径：").grid(row=0)
e2 = Entry(root, textvariable=path, width=25)
e2.grid(row=0, column=1)
Button(root, text="选择", command=callback).grid(row=0, column=2, padx=10, pady=5)

WIDTH = 100
HEIGHT = 80
ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!1I;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]


def get_img():
    # print(path1)
    # 在下方预览图片
    path1 = e2.get()
    # photo = PIL.Image.open(path1)
    # photo.resize((50, 50), PIL.Image.ANTIALIAS)
    # photo1 = ImageTk.PhotoImage(PIL.Image.open(path1))
    # Label(root, image=photo1).grid(row=2, columnspan=3, padx=10, pady=5)

    im = PIL.Image.open(path1)
    im = im.resize((WIDTH, HEIGHT), PIL.Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    Label(root, text="字符画已生成，请保存查看。").grid(row=3, columnspan=3, padx=10, pady=5)
    Button(root, text="保存", width=10, command=save_img).grid(row=1, column=1, sticky=W, padx=10, pady=5)
    return txt


def save_img():
    txt = get_img()
    filename = asksaveasfilename(
        title=("图片保存路径"),
        initialdir=r"C:\Users\Administrator\Desktop",
        filetypes=[('Text file', '.txt'), ('All files', '*')],
    )
    if filename:
        with open(filename, 'w') as f:
            f.write(txt)

Button(root, text="生成字符画", width=15, command=get_img).grid(row=1, column=0, sticky=W, padx=15, pady=5)
Button(root, text="退出", width=10, command=root.quit).grid(row=1, column=2, sticky=E, padx=10, pady=5)

mainloop()
