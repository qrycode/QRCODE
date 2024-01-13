import qrcode
from PIL import Image

#가운데 이미지 추가용
# 국민연금 이미지 경로 211.254.72.240/ D:\Qrcode\nps

#썸네이 만들기
#iu_img.thumbnail((100,100))
QR = qrcode.QRCode(box_size=10, border = 1)  #Qrcode size 

#국민연금
QR.add_data('http://211.254.72.240/nps/nps_Main.html')


QR.make(fit=True) # 정보량에 따라 version, 크기변경
Gen_Qr = QR.make_image().convert('RGB')
#Gen_Qr = QR.make_image(fill_color = "lightgreen",back_color = "black")
Gen_Qr.save("nps_QR.png")