import qrcode
from tkinter import *
def generate_qr_code(text,file_name):
    qr=qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
                     box_size=10,
                     border=1,) 
    qr.add_data(text)        
    qr.make(fit=True) 
    img=qr.make_image(fill_color="green",back_color="black") 
    img.save(file_name)     
text="http:// 192.168.1.5:8000/"
file_name="sri.png"
generate_qr_code(text, file_name)
print("QR code saved as ",file_name)

#Tkinter
root=Tk()
root.title("Qr code")
img=PhotoImage(file=file_name)
label=Label(root,image=img,bg='white').place(x=550,y=200)
root.mainloop()