#  Import header files  
import pygame,sys,pygame.mixer,time
import mysql.connector
from datetime import datetime,timedelta
# Initializing pygame
pygame.init()

# cursor in database
obj = mysql.connector.connect(user='root',password='khokhar',
                              host='127.0.0.1',database ='test')
cursor = obj.cursor()
# Color Definitions
white =(255,255,255)
black =(0,0,0)
red = (255,0,0)
green =(0,255,0)
blue =(0,0,255)
bg = (255,255,255)
cyan = (0,255,255)

# Dimensions of Canvas
width = 1200
height = 710

# Output window (screen) named Station
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Station")



# Methods
# 1. For drawing tracks and notification boards on Canvas




class Canvas():
    def __init__(self,n,n1,n2,colour):
        ''' Constructor  '''
        self.n = n
        self.colour = colour
        self.n1=n1
        self.n2=n2
    def track(self):
        '''For drawing track lines'''
        i =1
        y=70
        while(self.n>0):
            if i == 1 or i == 10:
                self.colour = red
            elif i ==2 or i == 3 or i == 8 or i== 9 :
                self.colour = cyan
            elif i==5 or i==6 or i == 4 or i ==7 :
                self.colour = white
            pygame.draw.line(screen,self.colour,(600,y),(880,y),4)
            pygame.draw.line(screen,self.colour,(600,y+25),(880,y+25),4)
            y+=60
            self.n-=1
            i +=1

    def track1(self):
        '''For drawing track lines'''
        i =1
        y=340
        while(self.n1>0):
            
            pygame.draw.line(screen,white,(260,y),(550,y),4)
            pygame.draw.line(screen,white,(260,y+25),(550,y+25),4)
            y+=60
            self.n1-=1
            i +=1

    def track2(self):
        '''For drawing track lines'''
        i =1
        y=340
        while(self.n2>0):
            
            pygame.draw.line(screen,white,(920,y),(1200,y),4)
            pygame.draw.line(screen,white,(920,y+25),(1200,y+25),4)
            y+=60
            self.n2-=1
            i +=1
    def rungs(self,x):
        '''For drawing rungs'''
        y=70
        i=1
        while y<710 and self.n>0:
            if i == 1 or i == 10:
                self.colour = red
            elif i ==2 or i == 3 or i == 8 or i== 9 :
                self.colour = cyan
            elif i==5 or i==6 or i == 4 or i ==7 :
                self.colour = white
            k =610
            while k<880 and x >0:
                pygame.draw.line(screen,self.colour,(k,y-3),(k,y+29),15)
                k+=50
            y+=60
            x -=1
            i+=1

    def rungs1(self,x1):
        '''For drawing rungs'''
        y=340
        i=1
        while y<710 and self.n>0:
            
            k =280
            while k<580 and x1 >0:
                pygame.draw.line(screen,self.colour,(k,y-3),(k,y+29),15)
                k+=50
            y+=60
            x1 -=1
            i+=1

    def rungs2(self,x2):
        '''For drawing rungs'''
        y=340
        i=1
        while y<710 and self.n>0:
            
            k =935
            while k<1240 and x2 >0:
                pygame.draw.line(screen,self.colour,(k,y-3),(k,y+29),15)
                k+=50
            y+=60
            x2 -=1
            i+=1
            
# to draw different notification boards
    def drawboards(self):
        '''For drawing notifications Boards'''
        font  = pygame.font.Font(None , 30)
        s= "TRACK"
        '''Header line'''
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (340,2))
        font  = pygame.font.Font(None , 30)
        s= "Train Information"
        '''Header line'''
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (10,2))
        pygame.draw.line(screen,white,(0,30),(1000,30),5)
        pygame.draw.line(screen,white,(250,0),(250,710),5)

        font  = pygame.font.Font(None , 30)
        s= "Arrival :"
        '''Arrival board'''
        text = font.render(s,1,(250,0,0),(0,250,250))
        screen.blit(text, (2,40))
        pygame.draw.rect(screen,white,(0,38,77,25),2)
        pygame.draw.rect(screen,cyan,(2,70,240,100))
        pygame.draw.rect(screen,white,(0,68,244,104),3)

        font  = pygame.font.Font(None , 30)
        s= "Departure :"
        '''Departure board'''
        text = font.render(s,1,(250,0,0),(0,255,255))
        screen.blit(text, (2,180))
        pygame.draw.rect(screen,white,(0,178,110,25),2)
        pygame.draw.rect(screen,cyan,(2,210,244,100))
        pygame.draw.rect(screen,white,(0,210,245,102),3)

        font  = pygame.font.Font(None , 30)
        s= "Warning :"
        '''Warning Board'''
        text = font.render(s,1,(250,0,0),(0,255,255))
        screen.blit(text, (2,330))
        pygame.draw.rect(screen,white,(0,328,93,25),2)
        pygame.draw.rect(screen,cyan,(2,360,244,100))
        pygame.draw.rect(screen,white,(0,360,245,102),3)

        font  = pygame.font.Font(None , 30)
        s= "Track types:"
        text = font.render(s,1,(250,0,0),(0,255,255))
        screen.blit(text, (2,610))

        font  = pygame.font.Font(None , 30)
        '''Track type description'''
        s= "Outer-> red"                              
        text = font.render(s,1,(250,0,0),(0,255,255))
        screen.blit(text, (2,650))
        font  = pygame.font.Font(None , 30)
        s= "Main-> white"
        text = font.render(s,1,(250,0,0),(0,255,255))
        screen.blit(text, (2,690))
        font  = pygame.font.Font(None , 30)
        s= "Loop-> cyan"
        text = font.render(s,1,(250,0,0),(0,255,255))
        screen.blit(text, (2,670))
# places clock on canvas        
def clock_on_canvas():
    font  = pygame.font.Font(None , 30)
    s=  str(time.strftime("%H:%M:%S"))
    text = font.render(s,1,red,cyan)
    screen.blit(text, (920,2))
    pygame.draw.rect(screen,white,(0,178,110,25),2)
    pygame.draw.rect(screen,cyan,(2,210,244,100))
    pygame.draw.rect(screen,white,(0,210,245,102),3)
        
# to  move passing  up_trains
def move_train_up(plt):
    img  = pygame.image.load('cat.jpg')
    imgx =250
    
    if plt == 5:
        imgy = 70
    elif plt ==4:
        imgy = 130

    elif plt == 3:
        imgy = 190

    elif plt == 2:
        imgy = 250

    elif plt == 1:
        imgy = 310
    FPS = 30
    pixmov =4
    fpsTime = pygame.time.Clock()
    run =True
    while run:
        screen.fill((0,0,0))
        mycanvas = Canvas(10,2,2,white)
        mycanvas.drawboards()
        mycanvas.rungs(10)
        mycanvas.rungs1(2)
        mycanvas.rungs2(2)
        mycanvas.track()
        mycanvas.track1()
        mycanvas.track2()
        imgx +=pixmov
        screen.blit(img,(imgx,imgy))
        pygame.display.update()
        fpsTime.tick(FPS)
        if imgx>1000:
            run =False
# to  move passing down_trains 
def move_train_down(plt):
    img  = pygame.image.load('cat.jpg')
    imgx =1000.
    
    if plt == 6:
        imgy = 370
    elif plt ==7:
        imgy = 430

    elif plt == 8:
        imgy = 490

    elif plt == 9:
        imgy = 550
    elif plt == 10:
        imgy = 610
    FPS = 30
    pixmov =4
    fpsTime = pygame.time.Clock()
    run =True
    while run:
        screen.fill((0,0,0))
        mycanvas = Canvas(10,2,2,white)
        mycanvas.drawboards()
        mycanvas.rungs(10)
        mycanvas.rungs1(2)
        mycanvas.rungs2(2)
        mycanvas.track()
        mycanvas.track1()
        mycanvas.track2()
        imgx -=pixmov
        screen.blit(img,(imgx,imgy))
        pygame.display.update()
        fpsTime.tick(FPS)
        if imgx<250:
            run =False
    screen.fill((0,0,0))
    mycanvas = Canvas(10,2,2,white)
    mycanvas.drawboards()
    mycanvas.rungs(10)
    mycanvas.track()
# will return first available platform for up trains if there exits, other wise -1 will be returned      
def first_avail_plat_up():
    flag =0
    x = 0
    cursor.execute("""SELECT status FROM PLATFORM
                  WHERE id<6
                  ORDER BY id DESC
                  LIMIT 5
               """)
    mylist = cursor.fetchall()
    obj.commit()
    while x<5:
        t = mylist[x]
        if t[0] == 0:
            flag = 1
            if x == 0:
                return 1
            elif x == 1:
                return 2
            elif x==2:
                return 3
            elif x == 3:
                return 4
            elif x == 4:
                return 5
            break
        x+=1
    if flag == 0:
        return -1
# will return first available platform for down trains if there exits, other wise -1 will be returned
def first_avail_plat_down():
    flag =0
    x =0
    cursor.execute("""SELECT status FROM PLATFORM
                  WHERE id>5
                  ORDER BY id 
                  LIMIT 5
               """)
    mylist = cursor.fetchall()
    obj.commit()
    while x<5:
        t = mylist[x]
        if t[0] == 0:
            flag = 1
            if x == 0:
                return 6
            elif x == 1:
                return 7
            elif x==2:
                return 8
            elif x == 3:
                return 9
            elif x == 4:
                return 10
            break
        x+=1
    if flag == 0:
        return -1
    print mylist
# arrival time of up trains
def up_trains_arr_time():
    cursor.execute("""SELECT arr_time FROM UP
                  ORDER BY id 
               """)
    mylist = cursor.fetchall()
    obj.commit()
    print mylist
# departure time of up trains
def up_trains_dep_time():
    cursor.execute("""SELECT dep_time FROM UP
                  ORDER BY id 
               """)
    mylist = cursor.fetchall()
    obj.commit()
    print mylist

# departure time of down trains
def down_trains_dep_time():
    cursor.execute("""SELECT dep_time FROM DOWN
                  ORDER BY id 
               """)
    mylist = cursor.fetchall()
    obj.commit()
    print mylist

# arrival time of down trains
def down_trains_arr_time():
    cursor.execute("""SELECT arr_time FROM DOWN
                  ORDER BY id 
               """)
    mylist = cursor.fetchall()
    obj.commit()
    print mylist

# for stopping trains
def stop_local_trains_up(plt):
    img  = pygame.image.load('123.jpg')
    imgx =250
    
    if plt == 1:
        imgy = 70
    elif plt ==2:
        imgy = 130

    elif plt == 3:
        imgy = 190

    elif plt == 4:
        imgy = 250

    elif plt == 5:
        imgy = 310
    FPS = 20
    pixmov =3
    fpsTime = pygame.time.Clock()
    run =True
    while run:

        screen.fill((0,0,0))
        mycanvas = Canvas(10,2,2,white)
        mycanvas.drawboards()
        mycanvas.rungs(10)
        mycanvas.rungs1(2)
        mycanvas.rungs2(2)
        mycanvas.track()
        mycanvas.track1()
        mycanvas.track2()
        imgx +=pixmov
        screen.blit(img,(imgx,imgy))
        pygame.display.update()
        fpsTime.tick(FPS)
        if imgx>600:
            run =False

def move_local_trains_up(plt):
    img  = pygame.image.load('123.jpg')
    imgx =600
    
    if plt == 1:
        imgy = 70
    elif plt ==2:
        imgy = 130

    elif plt == 3:
        imgy = 190

    elif plt == 4:
        imgy = 250

    elif plt == 5:
        imgy = 310
    FPS = 20
    pixmov =3
    fpsTime = pygame.time.Clock()
    run =True
    while run:
        screen.fill((0,0,0))
        mycanvas = Canvas(10,2,2,white)
        mycanvas.drawboards()
        mycanvas.rungs(10)
        mycanvas.rungs1(2)
        mycanvas.rungs2(2)
        mycanvas.track()
        mycanvas.track1()
        mycanvas.track2()
        imgx +=pixmov
        screen.blit(img,(imgx,imgy))
        pygame.display.update()
        fpsTime.tick(FPS)
        if imgx>1000:
            run =False
def stop_local_trains_down(plt):
    img  = pygame.image.load('123.jpg')
    imgx =1000.
    
    if plt == 6:
        imgy = 370
    elif plt ==7:
        imgy = 430

    elif plt == 8:
        imgy = 490

    elif plt == 9:
        imgy = 550
    elif plt == 10:
        imgy = 610
    FPS = 20
    pixmov =3
    fpsTime = pygame.time.Clock()
    run =True
    while run:
        screen.fill((0,0,0))
        mycanvas = Canvas(10,2,2,white)
        mycanvas.drawboards()
        mycanvas.rungs(10)
        mycanvas.rungs1(2)
        mycanvas.rungs2(2)
        mycanvas.track()
        mycanvas.track1()
        mycanvas.track2()
        imgx -=pixmov
        screen.blit(img,(imgx,imgy))
        pygame.display.update()
        fpsTime.tick(FPS)
        if imgx<600:
            run =False
def move_local_trains_down(plt):
    img  = pygame.image.load('123.jpg')
    imgx =600.
    
    if plt == 6:
        imgy = 370
    elif plt ==7:
        imgy = 430

    elif plt == 8:
        imgy = 490

    elif plt == 9:
        imgy = 550
    elif plt == 10:
        imgy = 610
    FPS = 20
    pixmov =3
    fpsTime = pygame.time.Clock()
    run =True
    while run:
        screen.fill((0,0,0))
        mycanvas = Canvas(10,2,2,white)
        mycanvas.drawboards()
        mycanvas.rungs(10)
        mycanvas.rungs1(2)
        mycanvas.rungs2(2)
        mycanvas.track()
        mycanvas.track1()
        mycanvas.track2()
        imgx -=pixmov
        screen.blit(img,(imgx,imgy))
        pygame.display.update()
        fpsTime.tick(FPS)
        if imgx<250:
            run =False
    screen.fill((0,0,0))
    mycanvas = Canvas(10,2,2,white)
    mycanvas.drawboards()
    mycanvas.rungs(10)
    mycanvas.rungs1(2)
    mycanvas.rungs2(2)
    mycanvas.track()
    mycanvas.track1()
    mycanvas.track2()

def display_info(s1,x,y):
    font  = pygame.font.Font(None , 30)
    s= str(s1)
    text = font.render(s,1,(250,0,0))
    screen.blit(text, (x,y))
'''print first_avail_plat_up()
print first_avail_plat_down()
stop_local_trains_up(3)
time.sleep(3)
move_local_trains_up(3)
stop_local_trains_down(8)
time.sleep(3)
move_local_trains_down(8)
down_trains_arr_time()'''
display_info("abc",10,150)
stop_local_trains_up(1)
time.sleep(3)
move_local_trains_up(1)
while True:
    
    # Placing clock:
    clock_on_canvas()
    
    mycanvas = Canvas(10,2,2,white)
    mycanvas.drawboards()
    mycanvas.rungs(10)
    mycanvas.rungs1(2)
    mycanvas.rungs2(2)
    mycanvas.track()
    mycanvas.track1()
    mycanvas.track2()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    cursor.execute("""SELECT arr_time FROM UP""")
    upartime = cursor.fetchall()
    obj.commit()
    j = len(upartime)
    cursor.execute("""SELECT train_type FROM UP""")
    uptype = cursor.fetchall()
    obj.commit()
    print uptype
    cursor.execute("""SELECT arr_time FROM DOWN""")
    dnartime = cursor.fetchall()
    obj.commit()
    k = len(dnartime)
    cursor.execute("""SELECT train_type FROM DOWN""")
    dntype = cursor.fetchall()
    obj.commit()
    #print j,k
    size1 = j
    size2 = k
    now = datetime.now().time()
    d1 = datetime(2014, 9, 10, now.hour, now.minute)
    #print str(d1.time())
    while j!=0 or k!=0:
        
        if j>0:
            x=0
            
            while(x<size1):
                print "asheet"
                move_train_up(first_avail_plat_up())
                t=upartime[x]
                '''if str(d1.time()) == str(t[0]):
                    if uptype[x] == 1:
                        move_train_up(first_avail_plat_up())'''
                x+=1
        j -=1
        k -=1
                        
            

    pygame.display.update()

