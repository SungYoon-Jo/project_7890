from PIL import Image, ImageDraw, ImageFont
                    #(가로, 세로)
img = Image.new("RGBA", (100,100), 0) #워터마크 생성

soimg = Image.open(f"./img/so/2.jpg")

fnt = ImageFont.truetype("arial.ttf", 30)

draw = ImageDraw.Draw(soimg) #원본 이미지
        #(좌표 : x, y)
draw.text((0,0), "20220919", font=fnt, fill=(0,0,0))

draw = ImageDraw.Draw(soimg)

img.save('./img/save/text.png')

soimg.save('./img/save/soimg.png')

soimg.show()