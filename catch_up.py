from pygame import*


window=display.set_mode((700,500))
display.set_caption("Догонялки")
background=transform.scale(image.load("background.jpg"),(700,500))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

x1=100
y1=300
x2=500
y2=300
x3=500
y3=400


sprite3 = transform.scale(image.load("treasure.png"),(70,70))
sprite2 = transform.scale(image.load("cyborg.png"),(70,70))
sprite1 = transform.scale(image.load("sprite1.jpg"),(50,50))
speed=10



run=True
clock=time.Clock()
FPS=60

while run:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    window.blit(sprite3,(x3,y3))

    for e in event.get():
        if e.type ==QUIT:
            run=False

    keys_pressed=key.get_pressed()
    if keys_pressed[K_LEFT] and x1>5:
        x1 -=speed
    if keys_pressed[K_RIGHT] and x1<595:
       x1 +=speed
    if keys_pressed[K_UP] and y1>5:
        y1 -=speed
    if keys_pressed[K_DOWN] and y1<395:
        y1 +=speed

    display.update()
    clock.tick(FPS) 
