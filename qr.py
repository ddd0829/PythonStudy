import qrcode

qr_data = 'https://theuselessweb.com/'
qr_img = qrcode.make(qr_data)

save_path = 'myqr.png'
qr_img.save(save_path)