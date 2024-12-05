default rosalindName = "???"

define 로잘린드 = Character('rosalindName', dynamic=True, color="#4d4843", image="로잘린드")

image 로잘린드 몬무스 = "images/characters/rosalind/monmusu.png"

image side 로잘린드 몬무스 = Transform(Crop((600, 0, 1900, 2100), "images/characters/rosalind/monmusu.png"), zoom=.4)