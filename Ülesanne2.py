import pygame   # impordime pygame
pygame.init()   # käivitan pygame

screen=pygame.display.set_mode([640,480])   # määran ekraani suuruse
pygame.display.set_caption("Ülesanne 2")    # määran akna nime

bg=pygame.image.load("bg_shop.png")     # laen üles taustapildi
screen.blit(bg,[0,0])   # üle kogu ekraani olev pilt

seller=pygame.image.load("seller.png")  # laen üles seller pildi
seller=pygame.transform.scale(seller, [255,305])    # määran seller'i suuruse
screen.blit(seller, [105,160])  # määran pildi asukoha

chat=pygame.image.load("chat.png")  # laen üles chat pildi
chat=pygame.transform.scale(chat, [258,200])    # chati kasti suuruse määramine
screen.blit(chat, [246,70])     # chat kasti asukoht

font=pygame.font.Font(None, 25)     # font ja selle suuruse määramine
text=font.render("Tere, olen Karin Marran", True, [255,255,255])    # teksti lisamine
screen.blit(text, [275,150])    # chat kasti asukoha määramine

pygame.display.flip()

running = True  # selleks, et avatav aken ka lahti jääks kuniks ise selle lugen, on vastav kood
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False