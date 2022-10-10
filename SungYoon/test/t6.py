from stegano import lsb

secret = lsb.hide("./img/test.png", "goodday")
secret.save("goodday.png")