#Programma, kas ļauj ievadīt un saglabāt priekšmetu atzīmes

#1. Jāļauj ievadīt priekšmetus (input)
#2. Jāizvada ievadītie priekšmeti (print, for)
#3. Jāļauj ievadīt priekšmetu atzīmes (input) -- 1 - 10, nv
#4. Jāļauj lietotājam izvēlēties priekšmetu un izvadīt atzīmes saistītas ar šo priekšmetu (...)
#5. Jānodrošina priekšmetu un atzīmju saglabāšana failā (json.dumps)
#6. Jānodrošina priekšmetu un atzīmju ielāde no faila (json.load)
#7. Jānodrošina priekšmetu un atzīmju dzēšana
# Atzīmes var glabāt klasē
class prieksmets:
    nosaukums = ""
    atzimes = []
# vai (labāk) vārdnīcā
atzimes = { "prieksmets1" : [] }
atzimes["citsprieksmets"] = []
for key, value in atzimes.items():
    print (key, value)