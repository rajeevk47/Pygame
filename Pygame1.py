import sys, pygame,random
while True:  
   
   # list = [40,60,80,100,120,140,160,180,200,220,240]
   pygame.init()
   main = pygame.display.set_mode((600,300))
   main.fill('black')
   pygame.display.set_caption('First pygame')
   clock = pygame.time.Clock()
   font = pygame.font.Font('comici.ttf',30)
   font1 = pygame.font.Font('comici.ttf',15) 
   BackG = pygame.image.load('bg.jpg').convert()
   Title = font.render('My Game', False , 'Black')
   Helic= pygame.image.load('bullet.png').convert_alpha()
   Helic1= pygame.image.load('bullet.png').convert_alpha()
   Helic2= pygame.image.load('bullet.png').convert_alpha()
   Helic3= pygame.image.load('bullet.png').convert_alpha()
   Helic4= pygame.image.load('bullet.png').convert_alpha()
   char = pygame.image.load('char.png').convert_alpha()
   char_rect =char.get_rect(midleft=(100,300) ) 
   heli_rect = Helic.get_rect(topleft=(600,40))
   title_rect = Title.get_rect(center = (300,20))
   heli_rect1 = Helic1.get_rect(topleft=(100,140))
   heli_rect2 = Helic2.get_rect(topleft=(300,220))
   heli_rect3 = Helic3.get_rect(topleft=(800,260))
   heli_rect4 = Helic4.get_rect(topleft=(700,200))
   scorec=0
   cha =3 
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT: 
            pygame.quit()   
            sys.exit()
      main.blit(BackG,(0,0))#background 
      main.blit(char,char_rect)#playermovement
      # pygame.draw.rect(main,'Pink',title_rect)
      main.blit(Title,title_rect) #Title

      main.blit(Helic,heli_rect)#helicopter
      main.blit(Helic1,heli_rect1)#helicopter1
      main.blit(Helic2,heli_rect2)#helicopter2
      main.blit(Helic3,heli_rect3)#helicopter3
      main.blit(Helic4,heli_rect4)#helicopter4
      
      scorec+=1
      
      score = font.render(f'{int(scorec/13)}',False,'Red')
      score_rec = score.get_rect(center = (100,20))
      main.blit(score,score_rec) #Title
      key = pygame.key.get_pressed()
      if key[pygame.K_UP]:
         char_rect.top-=4
         if char_rect.top<=30:
          char_rect.top=30
      if key[pygame.K_DOWN]:
         char_rect.top+=4
         if char_rect.bottom>=300:
          char_rect.bottom=300
      if key[pygame.K_LEFT]:
         char_rect.right-=4
         if char_rect.left<=0:
          char_rect.left=0
      if key[pygame.K_RIGHT]:
         char_rect.left+=4
         if char_rect.right>600:
          char_rect.right=600
      chance = font1.render(f'Chances Left: {int(cha)}', False , 'Black')  
      chance_rect = chance.get_rect(center = (500,20))
      main.blit(chance,chance_rect)
      heli_rect.right-=6
      if heli_rect.right<=0:
         heli_rect.left=600
         heli_rect.top= random.randint(40,80)
      heli_rect1.right-=6
      if heli_rect1.right<=0:
         heli_rect1.left=600
         heli_rect1.top= random.randint(80,120)
      heli_rect2.right-=6
      if heli_rect2.right<=0:
         heli_rect2.left=600
         heli_rect2.top= random.randint(100,160)
      heli_rect3.right-=6
      if heli_rect3.right<=0:
         heli_rect3.left=600
         heli_rect3.top= random.randint(160,220)
      heli_rect4.right-=8
      if heli_rect4.right<=0:
         heli_rect4.left=600
         heli_rect4.top= random.randint(190,260)
      current_time = pygame.time.get_ticks()
      if char_rect.colliderect(heli_rect ) or char_rect.colliderect(heli_rect1) or char_rect.colliderect(heli_rect2) or char_rect.colliderect(heli_rect3 )or char_rect.colliderect(heli_rect4):
         main.fill('black')
         cha-=(1/12)
         if(int(cha)==0):
           break              
      pygame.display.update()
      clock.tick(60)

   while True:
      score = int(scorec/13)
      for event in pygame.event.get():
            if event.type == pygame.QUIT: 
               pygame.quit()   
               sys.exit()
                           
      pygame.display.set_caption('Game over')
      with open('high.txt','r') as f:
             a=f.readline()
             if a:
              b= int(a)
      BackG1 = pygame.image.load('bg.jpg').convert_alpha() 
      title1 = font.render('GAME OVER',False,'blue')
      title3 = font.render('PRESS Q TO RESTART ',False,'red')
      title4 = font1.render(f'Highest Score :{a}',False,'red')
      title1_rect = title1.get_rect(center = (300,150))
      title3_rect = title3.get_rect(center = (300,260))
      title2 = font1.render(f'Score :{int(scorec/13)}',False,'blue')
      title2_rect = title2.get_rect(center = (300,200))
      title4_rect = title4.get_rect(center= (300,180))
      main.blit(BackG1,(0,0))
      main.blit(title1,title1_rect)
      main.blit(title2,title2_rect)
      main.blit(title3,title3_rect)  
      main.blit(title4,title4_rect)       
      pygame.display.update()
      clock.tick(60)
      key = pygame.key.get_pressed()
      if score>=b:
         with open('high.txt','w') as f:
                pass
         with open('high.txt','a') as f:
             f.write(f'{int(scorec/13)}')
      if key[pygame.K_q]:
         break
      else:
         continue

         

      