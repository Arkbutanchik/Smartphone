from tkinter import*
from datetime import datetime, time
import cv2
import os


root=Tk()
c=Canvas(width=393,height=673)
root.geometry("393x673")
c.place(x=0,y=0)

#main photos
wallpaper_file=PhotoImage(file="D:\\Python\\Pазные программы\\Smartphone\\assets\\wallpaper.png")
home_btn_file=PhotoImage(file="D:\\Python\\Pазные программы\\Smartphone\\assets\\home-btn.png")
border_file=PhotoImage(file="D:\\Python\\Pазные программы\\Smartphone\\assets\\smartphone-border-with-camera.png")

#camera photos
camera_icon_file=PhotoImage(file="D:\\Python\\Pазные программы\\Smartphone\\assets\\camera-app-icon.png")
camera_gui_file=PhotoImage(file="D:\\Python\\Pазные программы\\Smartphone\\assets\\camera-app-gui.png")
take_a_photo_btn_file=PhotoImage(file="D:\\Python\\Pазные программы\\Smartphone\\assets\\take-a-photo-btn.png")

#gallery photos
gallery_icon_file=PhotoImage(file="D:\\Python\\Pазные программы\\Smartphone\\assets\\gallery-app-icon.png")



def home():
    global camera_icon_img
    try:
        take_a_photo_btn_img.place_forget()
        camera.release()
    except:
        pass
    wallpaper_img=c.create_image(16,16,image=wallpaper_file,anchor='nw')
    border_img=c.create_image(0,0,image=border_file,anchor='nw')

    camera_icon_img=c.create_image(26,57,image=camera_icon_file,anchor='nw')
    c.tag_bind(camera_icon_img,'<Button-1>',func=lambda event: open_camera())

    gallery_icon_img=c.create_image(116,57,image=gallery_icon_file,anchor='nw')
    c.tag_bind(gallery_icon_img,'<Button-1>',func=lambda event: open_gallery())

    home_btn_img=c.create_image(136,624,image=home_btn_file,anchor='nw')
    c.tag_bind(home_btn_img,'<Button-1>',func=lambda event: home())
    

def open_camera():
    global take_a_photo_btn_img

    camera_gui_img=c.create_image(16,16,image=camera_gui_file,anchor='nw')

    home_btn_img=c.create_image(136,624,image=home_btn_file,anchor='nw')
    c.tag_bind(home_btn_img,'<Button-1>',func=lambda event: home())

    take_a_photo_btn_img=c.create_image(157,492,image=take_a_photo_btn_file,anchor='nw')
    c.tag_bind(take_a_photo_btn_img,'<Button-1>',func=lambda event: take_a_photo())


def open_gallery():
    pass


def take_a_photo():
    global camera
    camera=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    ret,img=camera.read()
    now=datetime.now()
    time_=now.strftime("%S_%M_%H_%d_%m_%Y")
    directory=r"D:\\Python\\Pазные программы\\Smartphone\\data\\Photos"
    image_name=f"Photo_{time_}.jpeg"
    os.chdir(directory)
    cv2.imwrite(image_name,img)
    camera.release()


def change_time():
    time_now=datetime.now().strftime("%H:%M")
    c.create_text(34,18,text=time_now,anchor='nw',font="Arial 18")


home()
root.mainloop()