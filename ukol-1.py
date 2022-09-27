baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
for z in baliky.values():
    if z == True:
        print("Balík byl předán kurýrovi")
    else:
        print("Balík zatím nebyl předán kurýrovi")
    z + 1