from frog import Frog
from PIL import Image
from time import time

X, Y = 10, 10
frogsize = 500
frogs = Image.new("RGBA", (frogsize*X,frogsize*Y), "#0000")
lfrogs = []

t1 = time()
for y in range(Y):
    for x in range(X):
        frog = Frog(goodeyes=True)

        frogim = frog.get(frogsize)
        lfrogs.append(frogim)
        frogs.paste( frogim, (x*frogsize, y*frogsize))

        percent = round(100*k/(X*Y), 2)
        naffi = int(percent/(100/n))
        print("[", "#"*naffi, " "*(n-naffi),"]", str(percent)+"%      ", end="\r")
print("[", "#"*n,"]", "100%   ")

t2 = time()
print(round(t2-t1,3), "s pour", X*Y, "grenouilles de tailles",frogsize)
print(round((t2-t1)/(X*Y),3), "s/grenouille de taille",frogsize)

frogs.save("frog.png")
lfrogs[0].save('frog.gif', save_all=True, append_images=lfrogs[1:], optimize=False, duration=120, loop=0)


