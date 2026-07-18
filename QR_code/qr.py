import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=1xuhxVo8v60&list=RD1xuhxVo8v60&start_radio=1")
img.save("youtube_qr.png")