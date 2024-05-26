import pygame

# PENCERE 
pygame.init()
clock = pygame.time.Clock()
genislik = 800
yukseklik = 600
pencere = pygame.display.set_mode((genislik,yukseklik))
pygame.display.set_caption("Blok Kırıcı :)")

# RENKLER 
siyah = (0,0,0)
beyaz = (255,255,255)
yesil = (0,255,0)

# RAKET 
raket = pygame.Rect(genislik/2,yukseklik-50,100,20)
raket_hiz = 0

# TOP 
top = pygame.Rect(genislik/2-10,yukseklik/2-10,20,20)
top_x_hiz = 6
top_y_hiz = 6

# BLOK 
blok_genislik = 80
blok_yukseklik = 20
bloklar = []

for satir in range(5):
    for sutun in range(10):
        blok_x = sutun * (blok_genislik + 10)
        blok_y = satir * (blok_yukseklik + 10)
        bloklar.append(pygame.Rect(blok_x,blok_y,blok_genislik,blok_yukseklik))

# OYUN DÖNGÜSÜ
oyun = True
while oyun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                raket_hiz -= 10
            if event.key == pygame.K_RIGHT:
                raket_hiz += 10
        if event.type == pygame.KEYUP:
            raket_hiz = 0

    # Raket ekrandan çıkmasın
    if raket.left <= 0:
        raket.left = 0
    if raket.right >= genislik:
        raket.right = genislik

    # Top pencereden çıkmasın
    if top.top <= 0:
        top_y_hiz *= -1
    if top.left <= 0 or top.right >= genislik:
        top_x_hiz *= -1
    
    # Top aşağıya çarparsa
    if top.bottom >= yukseklik:
        oyun = False

    # Top-raket etkileşimi 
    if top.colliderect(raket):
        top_y_hiz *= -1

    raket.x += raket_hiz
    top.x += top_x_hiz
    top.y += top_y_hiz

    # Top-blok etkileşimi
    for blok in bloklar:
        if blok.colliderect(top):
            bloklar.remove(blok)
            top_y_hiz *= -1

    # Pencereye çizme
    pencere.fill(siyah)

    for blok in bloklar:
        pygame.draw.rect(pencere,yesil,blok)

    pygame.draw.rect(pencere,beyaz,raket)
    pygame.draw.ellipse(pencere,beyaz,top)

    # Pencereyi güncelleme
    clock.tick(60)
    pygame.display.update()

pygame.quit()