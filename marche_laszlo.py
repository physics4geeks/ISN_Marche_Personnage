from tkinter import *

fenetre=Tk()
fenetre.title("Laszlo")

def enfoncee(evt) :
    ''' Une touche enfoncée modifie le vecteur vitesse '''
    global VX, VY, pos
    t = evt.keysym
    if t == 'Up' :
        VX, VY = 0, -5
    elif t == 'Down' :
        VX, VY = 0, 5
    elif t == 'Left' :
        VX, VY = -5, 0
    elif t == 'Right' :
        VX, VY = 5, 0

def relachee(evt) :
    ''' Une touche relachée modifie le vecteur vitesse '''
    global VX, VY
    VX, VY = 0, 0

def animation():
    ''' Calcul des nouvelles coordonnees du personnage '''
    ''' Si le personnage se deplace on incremente le n° de l'image '''
    ''' sans dépasser la fin du cycle '''
    global X,Y, pos
    X, Y = X + VX, Y+ VY
    if VX != 0 or VY != 0 :
        pos = pos + 1
    if pos not in range(0,12) and VY > 0 :
        pos = 0
    elif pos not in range(12,24) and VX < 0 :
        pos = 12
    elif pos not in range(24,36) and VX > 0 :
        pos = 24
    elif pos not in range(36,48) and VY < 0 :
        pos = 36
    Fond.itemconfig(Las,image = fichier[pos])
    Fond.coords(Las,X,Y)
    fenetre.after(50,animation)

Fond=Canvas(fenetre,width=600,height=600,bg="white")
Fond.grid()

fichier = []
for i in range(48) :
    fichier.append(PhotoImage(file='image-'+str(i)+'.gif'))

X, Y, VX, VY, pos = 260, 260, 0, 0, 0

Las = Fond.create_image(X,Y,image=fichier[0])

fenetre.bind_all("<KeyPress>", enfoncee)
fenetre.bind_all("<KeyRelease>", relachee)
animation()

fenetre.mainloop()


