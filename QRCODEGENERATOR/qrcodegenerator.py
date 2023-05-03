import qrcode
import image
qr = qrcode.QRCode(
    version = 15,  # versão do qrcode, quanto maior, maior  a complexidade
    box_size = 10, # tamanho da box
    border = 5 #parte branca da imagem
)

data = "COLOQUE O SITE OU INFORMAÇÃO AQUI"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color = "white")
img.save("qrcodelinkedin.png")