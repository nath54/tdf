#NE LANCEZ PAS CE PROGRAMME AVEC PYTHON 3
#coding:utf-8
import random,pygame,time,os
from pygame.locals import *
from PIL import Image
from threading import Thread

fps=60
pla=1000

def cn():
    vc,cc,v,c={"a":8,"e":8,"y":1,"u":3,"i":4,"o":4},{"z":1,"r":7,"t":6,"p":6,"q":1,"s":7,"d":8,"f":5,"g":4,"h":1,"j":2,"k":2,"l":5,"m":4,"w":1,"x":1,"c":5,"v":2,"b":2,"n":6},[],[]
    for d in vc:
        for e in range(vc[d]): v.append(d)
    for d in cc:
            for e in range(cc[d]): c.append(d)
    cprenoms,cnoms,prenom,nom=["cvcv","cvvcvc","cvccvc","ccvv","cvv","cvc","vccvc","vcvcvc"],["cvcvcvcv"],"",""
    for d in random.choice(cprenoms):
        if d == "v": prenom+=random.choice(v)
        else: prenom+=random.choice(c)
    for d in random.choice(cnoms):
        if d == "v": nom+=random.choice(v)
        else: nom+=random.choice(c)
    return prenom,nom


def tsp(sp):
    spp=[]
    da=len(sp)
    while len(spp) != da:
        ss=sp[0]
        for s in sp:
            if s.py < ss.py: ss=s
        spp.append(s)
        del(sp[sp.index(s)])
    return spp

cos=[]
cim=[]
termines=[]
nb_crs=20
tt_crs=60   
crs=[]
ddd="images/"
nb_ic=11
nb_iv=2
imgat=[]
mgats=[]
imgsc=[]
imgsv=[]
for x in range(1,nb_ic):
    imgat.append("cycliste_"+str(x)+"_1.png")
    imgat.append("cycliste_"+str(x)+"_2.png")
    imgat.append("cycliste_"+str(x)+"_3.png")
    mgats.append("cyclist_"+str(x)+"_1.png")
    mgats.append("cyclist_"+str(x)+"_2.png")
    mgats.append("cyclist_"+str(x)+"_3.png")
    imgsc.append(["cyclist_"+str(x)+"_1.png","cyclist_"+str(x)+"_2.png","cyclist_"+str(x)+"_1.png","cyclist_"+str(x)+"_3.png"])
    imgsc[x-1].append("images/pocy_"+str(x)+"_1.png")
for x in range(1,nb_iv):
    imgat.append("velo_"+str(x)+"_1.png")
    imgat.append("velo_"+str(x)+"_2.png")
    imgat.append("velo_"+str(x)+"_3.png")
    mgats.append("vel_"+str(x)+"_1.png")
    mgats.append("vel_"+str(x)+"_2.png")
    mgats.append("vel_"+str(x)+"_3.png")
    imgsv.append(["vel_"+str(x)+"_1.png","vel_"+str(x)+"_2.png","vel_"+str(x)+"_1.png","vel_"+str(x)+"_3.png"])
for x in range(0,len(imgat)):
    img=Image.open(ddd+imgat[x])
    img=img.resize([tt_crs,tt_crs])
    img.save(mgats[x])

class Coureur:
    def __init__(self,y):
        self.prenom,self.nom=cn()
        self.c1=(random.randint(100,255),random.randint(100,255),random.randint(100,255))
        self.imgs_c,self.imgs_v=random.choice(imgsc),random.choice(imgsv)
        self.im,self.imm=0,0
        self.img_actu_c,self.img_actu_v=self.imgs_c[self.im],self.imgs_v[self.im]
        self.vit=float(random.randint(1.0,3.0))
        ae=random.randint(500,1500)
        self.endurance,self.tot_endurance=ae,ae
        self.a1,self.a2=0.0-(0.0-float(self.vit)),float(random.randint(1.0,5.0))
        self.tt=tt_crs
        self.px,self.py=90.0-float(self.tt),float(y)
        self.trmn=False
    def avancer(self):
        if self.trmn == False and self.px >= pla+2:
            self.trmn=True
            termines.append(self)
        elif self.trmn == False and self.px <= pla+2:
            ff=random.randint(self.vit-self.a1,self.vit+self.a2)
            self.endurance-=ff
            fe=float(float(ff)*float(float(self.endurance)/float(self.tot_endurance)))
            if fe <= 0: fe = float(random.randint(5,20)/10)
            self.px+=float(fe)
            self.imm+=1
            if self.imm >= 5:
                self.imm=0
                self.im+=1
                if self.im >= len(self.imgs_c)-1: self.im=0
            self.img_actu_c,self.img_actu_v=self.imgs_c[self.im],self.imgs_v[self.im]

class Spect:
    def __init__(self,x,y,imgsg):
        self.px,self.py=x,y
        self.imgs=imgsg
        self.im=random.randint(0,len(self.imgs)-1)
        self.img_actu=self.imgs[self.im]
    def aff(self):
        self.im+=1
        if self.im >= len(self.imgs): self.im=0
        self.img_actu=self.imgs[self.im]

imgs_sp1=[ ["images/sp_1_1.png","images/sp_1_2.png","images/sp_1_3.png","images/sp_1_2.png","images/sp_1_1.png"]
]

imgs_sp2=[ ["images/sp_2_1.png","images/sp_2_2.png","images/sp_2_3.png","images/sp_2_2.png","images/sp_2_1.png"]
]
imgs_sp3=[ ["images/sp_3_1.png","images/sp_3_2.png","images/sp_3_3.png","images/sp_3_2.png","images/sp_3_1.png"]
]
spct=[]
nb_spct=100
for x in range(nb_spct):
    spct.append( Spect(random.randint(0,1100),random.randint(-5,15),random.choice(imgs_sp1)) )

for x in range(nb_spct):
    spct.append( Spect(random.randint(0,1100),random.randint(700,800),random.choice(imgs_sp2)) )

for x in range(nb_crs):
    a=100+x*(((640-60)/tt_crs)+20)
    crs.append( Coureur(a) )

spct=tsp(spct)

pygame.init()
fenetre = pygame.display.set_mode((1200,900))
pygame.display.set_caption("TDF 2018 :)")

pygame.key.set_repeat(400, 30)
fpsClock = pygame.time.Clock()

pause=True

def aff_podium():
    global cos
    cim=[]
    fenetre.fill((0,0,0))
    img_fond=pygame.image.load("images/podium.png") 
    fenetre.blit (img_fond, (0,0))
    myfont = pygame.font.SysFont("monospace", 15)
    img_c1=pygame.image.load(termines[0].imgs_c[len(termines[0].imgs_c)-1]) 
    fenetre.blit (img_c1, (530,400-180))
    t1t = myfont.render(termines[0].prenom+" "+termines[0].nom, 1, (0,0,0))
    fenetre.blit(t1t, (530,400-200))
    img_c2=pygame.image.load(termines[1].imgs_c[len(termines[1].imgs_c)-1]) 
    fenetre.blit (img_c2, (305,520-200))
    t2t = myfont.render(termines[1].prenom+" "+termines[1].nom, 1, (0,0,0))
    fenetre.blit(t2t, (305,520-220))
    img_c3=pygame.image.load(termines[2].imgs_c[len(termines[2].imgs_c)-1]) 
    fenetre.blit (img_c3, (705,520-200))
    t3t = myfont.render(termines[2].prenom+" "+termines[2].nom, 1, (0,0,0))
    fenetre.blit(t3t, (705,520-220))
    for s in spct:
        s.img=pygame.image.load(s.img_actu)
        fenetre.blit(s.img,(s.px,s.py))
        s.aff()
    for x in range(1): cos.append([random.randint(0,1000),0])
    for s in cos:
        cim.append(  pygame.draw.rect(fenetre, (100,105,10), (s[0],s[1],5,5), 0) )
        s[1]+=random.randint(15,20)
    for c in cos:
        if c[1] >= 500: del(cos[cos.index(c)])

def affichage():
    global termines
    if pause == False:
        if len(termines) < tt_crs:
            fenetre.fill((0,155,0))
            fr=pygame.draw.rect(fenetre,(100,100,100),(0,50,1200,650))
            fla=pygame.draw.lines(fenetre, (255,255,255), 5, ((pla,50),(pla,700)), 5)
            for c in crs:
                c.avancer()
                #c.img=pygame.draw.circle(fenetre, c.c1, (c.px,c.py), c.tt)
                c.imgc=pygame.image.load(c.img_actu_v) 
                fenetre.blit (c.imgc, (c.px,c.py-(c.tt/2)))
                c.imgv=pygame.image.load(c.img_actu_c) 
                fenetre.blit (c.imgv, (c.px,c.py-(c.tt/2)))
                myfont = pygame.font.SysFont("monospace", 15)
                c.imgtxt = myfont.render(c.prenom+" "+c.nom, 1, (0,0,0))
                aa=len((c.prenom+" "+c.nom))
                fenetre.blit(c.imgtxt, (c.px-aa*11, c.py))
            for s in spct:
                s.img=pygame.image.load(s.img_actu)
                fenetre.blit(s.img,(s.px,s.py))
                s.aff()
            txxt="top 3 termines = "
            for x in range(0,len(termines)):
                if x < 3:
                    tt=termines[x]
                    txxt+=str(x+1)+" "+tt.prenom+" "+tt.nom+"  "
                t=termines[x]
                if   x == 0 : ctc=(157,132,17)
                elif x == 1 : ctc=(207,206,202)
                elif x == 2 : ctc=(124,65,33)
                else        : ctc=(0,0,0)
                t.img2txt= myfont.render(str(x+1),1,ctc)
                fenetre.blit(t.img2txt, (t.px+10+tt_crs,t.py))
            ttxt = myfont.render(txxt, 1, (200,0,0))
            fenetre.blit(ttxt, (100,860))
            pygame.display.flip()
            pygame.display.update()
            fpsClock.tick(60)
        elif len(termines) >= tt_crs:
            print("podium")
            aff_podium()
    else:
        myfonta = pygame.font.SysFont("monospace", 30)
        ttts = myfonta.render("press a to start", 10, (255,0,0))
        fenetre.blit(ttts, (400,450))
        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(fps)

encour=True
h=False
while encour:
    for event in pygame.event.get():
        if event.type == QUIT: encour=0
        if event.type == KEYDOWN:
            if event.key == K_q: encour=0
            if event.key == K_a: pause=not pause
            if event.key == K_z: print(len(termines))
    if len(termines) >= 20 and not h:
        h=True
        time.sleep(2)
        fps=2
        spct=[]
        for x in range(20):
            spct.append( Spect(random.randint(0,1100),random.randint(600,800),random.choice(imgs_sp3)) )
        spct=tsp(spct)
    if len(termines) < 20 : affichage()
    else:
        aff_podium()
        myfonta = pygame.font.SysFont("monospace", 30)
        ttts = myfonta.render("press q to exit", 20, (255,0,0))
        fenetre.blit(ttts, (100,100))
        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(fps)

for f in os.listdir("./"):
    if f[0] == "c" or f[1] == "v": os.remove(f)

