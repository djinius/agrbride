define 꼭지 = Character('꼭지', color="#fe8040", hcolor="#7e4020", image="꼭지")

image 꼭지 몬무스 = "images/ai/characters/standings/coggi.png"

image 꼭지 로비_시트 000 = im.Crop("images/characters/animations/coggi.png", (241 *  0 + 1, 274, 240, 240))
image 꼭지 로비_시트 001 = im.Crop("images/characters/animations/coggi.png", (241 *  1 + 1, 274, 240, 240))
image 꼭지 로비_시트 002 = im.Crop("images/characters/animations/coggi.png", (241 *  2 + 1, 274, 240, 240))
image 꼭지 로비_시트 003 = im.Crop("images/characters/animations/coggi.png", (241 *  3 + 1, 274, 240, 240))

image 꼭지 로비 = Animation(
    "꼭지 로비_시트 000", .2,
    "꼭지 로비_시트 001", .2,
    "꼭지 로비_시트 002", .2,
    "꼭지 로비_시트 003", .2)
