          6 <<=~                     #
                ############## $ V1.3 $################

##############& Imported Modules

from os import system, path #####R
from time import sleep ######ed
import base64   ########
from webbrowser import open_new as tab

##########################
#Tool Style
##########################
gr, r, g, y, b, p, c, w=[
'\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m' ]
    
def color(text):
    col = [gr, r, g, y, b, p ,c, w]
    text= text.replace('GR@',col[0])
    text= text.replace('R@',col[1])
    text= text.replace('G@',col[2])
    text= text.replace('Y@',col[3])
    text= text.replace('B@',col[4])
    text= text.replace('P@',col[5])
    text= text.replace('C@',col[6])
    text= text.replace('W@',col[7])
    return text
       
######################
   
def cptl(text):
    
    for n in range(0,3):
        c = len(text)
        for z in range(0, c):
            f = ("R@" + text[:z].lower() + "G@" + text[z].upper())
            print(color(f),end="\r")
            sleep(.2)
        


######################
# Joker Banner
######################
system("clear")
def joker_banner():
	print(color("W@mNNNNNNNNNNNMMMNNmo/:B@---W@/dNNNNNmdddmhs+-G@``````        ```"))
	sleep(.2)                   
	print(color("W@NNNNNNNMNNNNNNNNhs+:B@-----W@/yNNNNNNmddmds/G@.``.```        `````"))
	sleep(.2)               
	print(color("W@mNNNNNNNNNNNNNNNs--B@..----:W@+dMMMMNNmdmmh+.G@``..```     ` ````"))
	sleep(.2)         
	print(color("W@mmmmmmmmmNNNNNmNy-B@.....--:/W@hNNNMMMNmmmds-G@``..```"))       
	sleep(.2)           
	print(color("W@dddddhhddddmdddh-B@........./sW@hNNNNMMNNmdy/.G@```.````````  ")) 
	sleep(.2)              
	print(color("W@yhhhhooyysyyhyo/B@-...```...-./+W@ydNNMNNmdh+.G@````...`````"))  
	sleep(.2)             
	print(color("W@yyysy++osssso//B@:-....`...-..::/W@sshhdmNmdo.G@``````-::-.-:.`"))  
	sleep(.2)               
	print(color("W@sssso/:::////---::-.-.::/:::/:///++ohdmmy:.G@``  `.-:/:///-```")) 
	sleep(.2)         
	print(color("W@ooos+/-.--::---:://///:///:---:---:/ohmNd+.G@.`   ```.:/:-::-`")) 
	sleep(.2)      
	print(color("W@ooo+/::----:::::::---..-----..-::::/ohNNmy:.G@``````   `......``"))  
	sleep(.2)  
	print(color("W@osso+/:----:-..`....``..--::::--://+ohmNNm+-...-`` `  G@``-.")) 
	sleep(.2) 
	print(color("W@yyys+/-.``..```....` `.-.---...::/+oyhmNNNh-...--```  G@``.-.```.`")) 
	sleep(.2)       
	print(color("W@hdddyo-...``````.........----::+ooyydmNNNMm/```.-``     G@`..-```"))  
	sleep(.2)      
	print(color("W@mmNmmh/--:-``````...-----:::+syhdhhdmNNNNNNo.``.-.      G@`....``")) 
	sleep(.2)     
	print(color("W@NNNNNmy//:-B@-````````......../W@syyhhhdmmNNNNmo.``-:.`    G@ `.``-")) 
	sleep(.2)          
	print(color("W@NNNNMMmso+/:.B@````````````.-/W@oshyhhddmmNNNNm+.``./.    G@ ````..```"))
	sleep(.2)    
	print(color("W@NNNNMMNdyoo++:.B@.````````.-:W@+osyhdmmmmmmmmmd:..`.-.     G@``````"))  
	sleep(.2)         
	print(color("W@MMMMMMMmdyosooo/B@--.````.-/W@osyyhdddmNmmddddh-.``.-`     G@`.```")) 
	sleep(.2)           
	print(color("W@MMMMMMMNmdyyyssys/B@---.-+W@/syhddddmmmmdddhhhs--.-/:`      G@` `"))  
	sleep(.2)             
	print(color("W@MMMMMMMMNmddddddhso-B@..-W@oyhddhhhhddddhhhyhho.:/+s:``` G@  ` `"))  
	sleep(.2)              
	print(color("W@NdddmMMMNmdhhdmmmmy/-B@..W@hddddddhyyhhhhhyyhh+-::+o-`.`  G@  ``"))  
	sleep(.2)              
	print(color("W@R@o///+shR@W@NMNmdyosyhmmy:-/hmmdhhhhyyyyyyyyyhd+G@/--.-/.  `'")) 
	sleep(.2)               
	print(color("W@R@oo+////+hR@W@NMMMdo+osyy/-smmdmdhyysyssyyyyyhh:G@-.``.-````    `"))  
	sleep(.2)              
	print(color("W@R@/+++//:::sR@W@NNNNy/://o//ymNmmddyysyysssyyhho`G@``````.-..    ``")) 
	sleep(.2)              
	print(color("W@R@-::-:::::/oR@W@/:+hs+:-:/ohmmNNmmdyyyssssyyyh+G@``  `-/-`-` `--.`"))  
	sleep(.2)         
	print(color("W@R@-.-.-----:--R@W@odmdhs+:/+sydmNNmdddhssssoyyh:G@` ``-//...-.:/.`")) 
	sleep(.2)           
	print(color("W@R@`.``..`..-:sR@W@dmmmmmhs++oyyhdmmdhhhso/R@:-W@shh-G@  `-+/.``-`..````  ``"))   
	sleep(.2)          
	print(color("W@R@.```````-+hR@W@dmmNNNmdhy++syyhddyss+/-R@../W@yhh`G@ ``..`   `` ``"))  
	sleep(.2)            
	print(color("W@R@--..--.-/sR@W@ddmmmmmmdyoss+syhhhs-R@--..-W@+sydyG@` ``` "))   
	sleep(.2)                 
	print(color("W@//::+o::ohhdhdmdddhhs+o+:oo+/R@:.`.-W@/ssyyd+  G@``   ```..`  `")) 
	sleep(.2)             
	print(color("W@:::+so/+osyyyyhyyyso/-R@..``.---.-W@:osssysh- G@ ```.``.-.`.```   ``"))
	sleep(.2)            
	print(color("R@........---:::--.-.......`..--:+W@syyyysss` G@`  ````.``....``")) 
	sleep(.2)               
	print(color("R@`.................```....`..-+W@ossssssss- G@`     `   `````````")) 
	sleep(.2)             
	print(color("R@``````````````....````......+W@soo+oooss:  G@`             `....``")) 
	sleep(.2)             
	print(color("W@...--::://///R@:--.--..```...:W@yoo+ooooo/` G@ `     `   `   `.````"))  
	sleep(.2)            
	print(color("R@...--::::----------...``.-/W@yso++o++o:`` G@ `       ``.`  `..`"))   
	sleep(.2)             
	print(color("R@``````.......------.....:W@+syssoo+o+-`G@           `````  `.``"))  
	sleep(.2)              
	print(color("R@`````````....----....-W@/+oyhsoooo+/.` G@          .``     ````"))  
	sleep(.2)              
	print(color("R@```````.....------::W@+sssyhhysys+/G@``` `        ``"))    
	sleep(.2)             
	print(color("R@```````.......-::/W@/sdhhyhdhyyo+/-G@``         ```")) 
	sleep(.2)                
	print(color("R@.....---::-::::/W@+ohdmmddddhso+/:.G@``          `  ```"))  
	sleep(.2)                
	print(color("R@.--:://++////+W@osshmmmmmdyos+//:G@:```          ````"))  
	sleep(.2)                  
	print(color("R@-.----:::://W@oyhmNmmmmdhy+/////:G@-`````         ``"))  
	sleep(.2)                  
	print(color("R@------::/W@+oosmmNNNmdhyo/:////:-G@.``````        `````")) 
	sleep(.2)
	print(color("R@++/:://W@+oyhddNmNNNmho/:::////:-G@` ```````       ```` `")) 
	sleep(.2)  
	print(color("W@ssssssyyhdhyhhdddhs+:::///:/::G@.`  ```````     `...`.```"))   
	sleep(.2)  
	print(color("W@sssssysooo+ossyso//::////::/:-G@``   `````````````...``.`..")) 
	sleep(.2)   
	print(color("W@/++++///////////:////:/::///:G@-``     ``..`````````` `")) 
	sleep(.2)
	print(color("W@::://://::::::://+///:::////:R@.``  ``  ``...``````"))
	sleep(.2)
	print(color("W@---..------:://+///:::://///-R@`````````  ````````"))
	sleep(.2)
	print(color("W@.......----:::/+//:::::/+//-`R@.` ````````` ```````"))
	sleep(.2)
	print(color("W@.........---::/::-:::::///-`.`R@````..````````` ````."))
	sleep(.2)
	print(color("W@..........-----:----::::-.`..R@` ```...``````````````..----.."))
	sleep(.2)
	print(color("R@W@.........----..----R@-.``..``````....`````..-......-.--:::::--")) 
	sleep(.2)     
	print(color("R@``W@`.....`............R@..``.-.` ```........------...-.-..-:-:::"))    
	sleep(.2)
	print(color("R@```````````..........```.-.` ````............---.```````..------::"))
	sleep(.2)
	print(color("R@````````````````````````..`` ````..............---.```````...----::"))
	sleep(.2)
	print(color("R@``````````````````````...``  ```...............----.````````....---:"))
	sleep(.2)
	print(color("R@`````````````````````.-..`  `````..............------.````````...----:"))
	sleep(.2)
	print(color("R@````````````````````...``   ````................--::---.```````...----:"))
	print("\n\n")
	
	
#####Tool Banner@######
#####           @######
def tool_bnr():
    print(color(" W@+++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    sleep(.1)
    print(color(" +G@      _       _       W@V1.3G@    _____           _      W@+"))
    sleep(.1)
    print(color(" +Y@     | | ___ | | _____ _ __  |_   _|__   ___ | |___  W@+"))
    sleep(.1)
    print(color(" +C@  _  | |/ _ \| |/ / _ \ '__|   | |/ _ \ / _ \| / __| W@+"))
    sleep(.1)
    print(color(" +B@ | |_| | (_) |   <  __/ |      | | (_) | (_) | \__ \ W@+"))
    sleep(.1)
    print(color(" +R@  \___/ \___/|_|\_\___|_|      |_|\___/ \___/|_|___/ W@+"))
    sleep(.1)
    print(color(" +++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    print(" ")


##############
#About me
def About():
	#from ToolStyle import color
    print(color("R@+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    sleep(.1)
    print(color("+Y@      _    _                 _   C@V1.3    R@+"))
    sleep(.1)
    print(color("+G@     / \  | |__   ___  _   _| |  R@+"))
    sleep(.1)
    print(color("+C@    / _ \ | '_ \ / _ \| | | | __| R@+"))
    sleep(.1)
    print(color("+B@   / ___ \| |_) | (_) | |_| | |_ R@+"))
    sleep(.1)
    print(color("+R@  /_/   \_\_.__/ \___/ \__,_|\__| R@+"))
    sleep(.1)
    print(color("+C@                                 Coded By : Abdo Storm                   R@+  "))
    sleep(.1)
    print(color("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    print(" ")




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

######################
#part2


################



joker_banner()
print(color("R@{P@!R@} Y@What Are You Using??"))
ip = print(color("\n#> [C@1Y@] C@Get_ip"))
youtube = print(color("\nY@##> [W@2Y@] W@Download_from_youtube"))
tool = print(color("\n###> [B@3Y@] B@Abdo_Tool"))

OS = (input(color("\nB@###> G@")))

if OS =='1':
    print(color("\n\n =$\\ Done ..\n\n"))
    cptl(" starting Abdo tools ")
    system("clear")
    de=("""ZnJvbSB0aW1lIGltcG9ydCBzbGVlcAppbXBvcnQgc29ja2V0CnNsZWVwKDIpCnByaW50ICgiIiIg
XDAzM1sxOzkwbXdlbGxjb20gaW4gZGFyayBzY3JpcHQKXDAzM1sxOzkxbQogX19fXyAgICBfICAg
IF9fX18gIF8gIF9fICBfX19fIF9fX19fIF9fXyAgX19fXyAgX18gIF9fCnwgIF8gXCAgLyBcICB8
ICBfIFx8IHwvIC8gLyBfX198XyAgIF8vIF8gXHwgIF8gXHwgIFwvICB8CnwgfCB8IHwvIF8gXCB8
IHxfKSB8ICcgLyAgXF9fXyBcIHwgfHwgfCB8IHwgfF8pIHwgfFwvfCB8CnwgfF98IC8gX19fIFx8
ICBfIDx8IC4gXCAgIF9fXykgfHwgfHwgfF98IHwgIF8gPHwgfCAgfCB8CnxfX19fL18vICAgXF9c
X3wgXF9cX3xcX1wgfF9fX18vIHxffCBcX19fL3xffCBcX1xffCAgfF98CgpcMDMzWzE7OTZtICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgIFZvZGFmb25lIFNtcyBTcGFtbWVyCiAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgIENvZGVkIEJ5IDogQWJkbyBTdG9ybQogICAgICAgICAgICAg
IOKYoyB3ZWxsY29tIGJybyBpbiBkYXJrIHNjcmlwdCDimKMgIApUZWxlZ3JhbSBMaW5rClwwMzNb
MTs5M21odHRwczovL3QubWUvRGFya1N0b3JtMTIzNDU2IAoiIiIpCnNsZWVwKC4zNSkKcHJpbnQg
KCJcMDMzWzE7OTFtKlwwMzNbMTs5M21fX19fX19fX19cMDMzWzE7OTJtR2V0X0lQXDAzM1sxOzk1
bV9fX19fX19fX19cMDMzWzE7OTFtKiIpCnByaW50ICgiXDAzM1sxOzkwbTwgLSAtIC0gLSAtIC0g
LSAtIC0gLSAtIC0gLSAtIC0gPiIpCnNsZWVwKC41MCkKdHJ5OgogICAgaG9zdF9uYW1lID0gaW5w
dXQgKCJcMDMzWzE7OTZtWytdTmFtZSBTaXRlOlwwMzNbMTs5N20gIikKICAgIGlwID0gc29ja2V0
LmdldGhvc3RieW5hbWUoInd3dy4iK2hvc3RfbmFtZSsiLmNvbSIpCiAgICBwcmludCAoCiAgICAi
XDAzM1sxOzkwbVRhcmdldCBJUyA6IFwwMzNbMTs5M20iLGhvc3RfbmFtZSwiXG4iICAgICAgICAi
XDAzM1sxOzkwbUlQIElzICAgICA6IFwwMzNbMTs5M20iLGlwLCJcMDMzWzE7OTdtIikKZXhjZXB0
IEV4Y2VwdGlvbiBhcyBlOgogICAgcHJpbnQgKCJcMDMzWzE7OTFtRXJyb3I6IixlLCJcMDMzWzE7
OTdtIik=""")

    x=base64.b64decode(de)
    d=x.decode("utf-8")

    g=compile(d,"","exec")

    exec(g)
##############
elif OS =='2':
    print(color("\n\n =$\\ Done ..\n\n"))
    cptl(" starting Abdo tools ")
    system("clear")
    de=("""ZnJvbSB0aW1lIGltcG9ydCBzbGVlcApzbGVlcCgyKQpwcmludCAoIiIiIFwwMzNbMTs5MG13ZWxs
Y29tIGluIGRhcmsgc2NyaXB0ClwwMzNbMTs5NG0KIF9fX18gICAgICAgICAgICAgICAgICAgICAg
XyAgICAgICAgICAgICAgICAgXwp8ICBfIFwgIF9fX19fICAgICAgX19fIF9fIHwgfCBfX18gICBf
XyBfICBfX3wgfAp8IHwgfCB8LyBfIFwgXCAvXCAvIC8gJ18gXHwgfC8gXyBcIC8gX2AgfC8gX2Ag
fAp8IHxffCB8IChfKSBcIFYgIFYgL3wgfCB8IHwgfCAoXykgfCAoX3wgfCAoX3wgfAp8X19fXy8g
XF9fXy8gXF8vXF8vIHxffCB8X3xffFxfX18vIFxfXyxffFxfXyxffAoKXDAzM1sxOzkwbS0gLSAt
IC0gLSAtIC0gLSAtIC0gLSAtIC0gLSAtIC0gLSAtIC0gLSAtIC0gLSAtIApcMDMzWzE7OTZtICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgIFZvZGFmb25lIFNtcyBTcGFtbWVyCiAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgIENvZGVkIEJ5IDogQWJkbyBTdG9ybQogICAgICAgICAgICAg
IOKYoyB3ZWxsY29tIGJybyBpbiBkYXJrIHNjcmlwdCDimKMgIApUZWxlZ3JhbSBMaW5rClwwMzNb
MTs5M21odHRwczovL3QubWUvRGFya1N0b3JtMTIzNDU2IAoiIiIpCnNsZWVwKC4zNSkKcHJpbnQg
KCJcMDMzWzE7OTFtKlwwMzNbMTs5M21fX19fX19fX19cMDMzWzE7OTRtZG93bmxvYWRfZnJvbV95
b3V0dWJlXDAzM1sxOzk1bV9fX19fX19fX19cMDMzWzE7OTFtKiIpCnByaW50ICgiXDAzM1sxOzkw
bTwgLSAtIC0gLSAtIC0gLSAtIC0gLSAtIC0gLSAtIC0gLSAtIC0gLSA+IikKc2xlZXAoLjM1KQp0
cnk6Cglmcm9tIHBhZnkgaW1wb3J0IG5ldwoJdXJsID0gaW5wdXQgKCJcMDMzWzE7OTJtVFlQRSBV
Ukw6IFwwMzNbMTs5N20gIikKCXZlZGlvID0gbmV3KHVybCkKCWRsID0gdmVkaW8uc3RyZWFtcwoJ
c3QgPSB2ZWRpby5hdWRpb3N0cmVhbXMKCXByaW50ICgiXDAzM1sxOzkwbWF1ZGlvIG9yIHZlZGlv
PyIpCglJTiA9IGlucHV0ICgiXDAzM1sxOzkybUlOUFVUOlwwMzNbMTs5N20gIikKCWlmIElOID09
ICJ2ZWRpbyI6CgkJZm9yIGkgaW4gZGwgOgoJCQlwcmludCAoaSkKCQlGID0gaW5wdXQgKCJcMDMz
WzE7OTJtc3RyZWFtczpcMDMzWzE7OTZtICIpCgkJaWYgRiA9PSAiMCI6CgkJCWRsWzBdLmRvd25s
b2FkKCIvc2RjYXJkL2Rvd25sb2FkLnB5IikKCQllbGlmIEYgPT0gIjEiOgoJCQlkbFsxXS5kb3du
bG9hZCgiL3NkY2FyZC9kb3dubG9hZC5weSIpCgkJZWxpZiBGID09ICIyIjoKCQkJZGxbMl0uZG93
bmxvYWQoIi9zZGNhcmQvZG93bmxvYWQucHkiKQoJCWVsaWYgRiA9PSAiMyI6CgkJCWRsWzNdLmRv
d25sb2FkKCIvc2RjYXJkL2Rvd25sb2FkLnB5IikKCQllbGlmIEYgPT0gIjQiOgoJCQlkbFs0XS5k
b3dubG9hZCgiL3NkY2FyZC9kb3dubG9hZC5weSIpCgkJZWxpZiBGID09ICI1IjoKCQkJZGxbNV0u
ZG93bmxvYWQoIi9zZGNhcmQvZG93bmxvYWQucHkiKQoJCQoJZWxpZiBJTiA9PSAiYXVkaW8iOgoJ
CWZvciBlIGluIHN0OgoJCQlwcmludChlKQoJCUIgPSBpbnB1dCAoIlwwMzNbMTs5Mm1zdHJlYW1z
OiAiKydcMDMzWzE7OTZtJykKCQlpZiBCID09ICIwIjoKCQkJc3RbMF0uZG93bmxvYWQoIi9zZGNh
cmQvZG93bmxvYWQucHkiKQoJCWVsaWYgQiA9PSAiMSI6CgkJCXN0WzFdLmRvd25sb2FkKCIvc2Rj
YXJkL2Rvd25sb2FkLnB5IikKCQllbGlmIEIgPT0gIjIiOgoJCQlzdFsyXS5kb3dubG9hZCgiL3Nk
Y2FyZC9kb3dubG9hZC5weSIpCgkJZWxpZiBCID09ICIzIjoKCQkJc3RbM10uZG93bmxvYWQoIi9z
ZGNhcmQvZG93bmxvYWQucHkiKQoJCWVsaWYgQiA9PSAiNCI6CgkJCXN0WzRdLmRvd25sb2FkKCIv
c2RjYXJkL2Rvd25sb2FkLnB5IikKCQllbGlmIEIgPT0gIjUiOgoJCQlzdFs1XS5kb3dubG9hZCgi
L3NkY2FyZC9kb3dubG9hZC5weSIpCmV4Y2VwdCBFeGNlcHRpb24gYXMgcDoKCXByaW50ICgiRVJS
T1I6IixwKQ==
""")
    x=base64.b64decode(de)
    d=x.decode("utf-8")

    g=compile(d,"","exec")

    exec(g)
########@

elif OS == "3":
  print(color("\n\n =$\\ Done ..\n\n"))
  cptl(" starting Abdo tools ")
  system("clear")
  def linux():
    system("clear")
    tool_bnr()
    print("     \033[1;33mWelcome Back >_* ..")
    print (color("        C@════════════════════════╗"))
    sleep(.1)
    print (color("        ╠[W@1C@] G@Install Termux-Kali          C@║"))
    print ("        ╠═════════════════════════════════╣")
    sleep(.1)
    print (color("        ╠[W@2C@] G@Install Termux-fedoraC@        ║"))
    sleep(.1)
    print ("        ╠═════════════════════════════════╣")
    sleep(.1)
    print (color("        ╠[W@3C@] G@Install MetasploitC@            ║"))
    sleep (.1)
    print("        ╠═════════════════════════════════╣")
    sleep(.1)
    print(color("        ╠[W@4C@] G@Install Termux-NmapC@              ║"))
    sleep(.1)
    print("        ╠═════════════════════════════════╣")
    sleep(.1)
    print(color("        ╠[W@5C@] G@Install Send_Email               C@║"))
    sleep(.1)
    print("        ╠═════════════════════════════════╣")
    sleep(.1)
    print(color("        ╠[W@6C@] G@Install Base64              C@║"))
    sleep(.1)
    print ("        ╠═════════════════════════════════╣")
    sleep(.1)
    print(color("        ╠[W@7C@] G@About Me           C@║"))
    sleep(.1)
    print("        ╚══════╦═══════════════════╦══════╝")
    sleep(.1)
    print(color("               ║  [Y@99C@] Y@Main Menu  C@ ║"))
    sleep(.1)
    print("               ╠═══════════════════╣")
    sleep(.1)
    print(color("               ║     [R@00C@] R@Exit     C@║"))
    sleep(.1)
    print("               ╚═════════╦═════════╝")
    sleep(.1)
    print("              ╔══════════╝")
    sleep(.1)

    linux = int(input(color('              ╚═══>\033[1;33m$\ W@')))
###22222########
    if linux == 1:
    		kali =input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')
    		if kali.lower() == "y":
        		system("sudo apt-get update -y")
        		system("sudo apt-get upgrade -y")
        		system("sudo apt-get install wget proot -y && wget -y")
        		system("sudo apt-get install git -y")
        		
#########2##########          
         
    elif linux == 2:
        system("pkg update -y")
        system("pkg upgrade -y")
        system("pkg install wget proot -y && wget -y")
        system ("pkg install git -y")
        system('git clone https://github.com/MasterDevX/Termux-Kali.git')
        system('mv Termux-Kali ../')
        print('  ')
        print('\033[1;31m[*] \033[1;33mTermux-Kali Installed Successfully √')
        sleep(2)
        system("clear")
        
#############2#2##        
        
    elif linux == 3:
        meta = input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')
        if meta.lower() == "y":
            system("pkg update")
            system("pkg upgrade")
            system("pkg install unstable")
            system("pkg install metasploit")
            print('\033[1;31m[*] \033[1;33mTermux-Kali Installed Successfully √')
            sleep(2)
            system("clear")
        else:
            print (color("R@ Try Again ^ - ^"))
            
##################            
            
    elif linux == 4:
        system("pkg update")
        system("pkg upgrade")
        system("pkg install nmap")

#####№###@#@#@#####

    elif linux == 5:
        system("pkg update && pkg upgrade")
        system("clear")
        decode = ("""ZnJvbSB0aW1lIGltcG9ydCBzbGVlcApmcm9tIG1haWxlciBpbXBvcnQgTWFpbGVyCnNsZWVwKDIp
CnByaW50ICgiIiJcMDMzWzE7OTBtIHdlbGxjb20gaW4gZGFyayBzY3JpcHQgICAgICAgClwwMzNb
MTs5MW0gICAKOjo6Ojo6OjogICAgICAgOjo6Ojo6ICAgICA6Ojo6OjogICAgIDo6ICAgIDo6ICAg
ICAgICAgICAgICAgIAo6OiAgICAgIDo6ICAgIDo6ICAgIDo6ICAgIDo6ICAgOjogICAgOjogICA6
Ogo6OiAgICAgIDo6ICAgIDo6ICAgIDo6ICAgIDo6IDo6OjogICAgOjogIDo6Cjo6ICAgICAgOjog
ICAgOjo6Ojo6OjogICAgOjogICAgOjogICA6Ojo6Cjo6ICAgICAgOjogICAgOjogICAgOjogICAg
OjogICAgOjogICA6OiA6Ogo6OiAgICAgIDo6ICAgIDo6ICAgIDo6ICAgIDo6ICAgIDo6ICAgOjog
IDo6Cjo6Ojo6Ojo6OiAgICAgOjogICAgOjogICAgOjogICAgOjogICA6OiAgIDo6ClwwMzNbMTs5
Nm0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgVm9kYWZvbmUgU21zIFNwYW1tZXIKICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgQ29kZWQgQnkgOiBBYmRvIFN0b3JtCiAgICAgICAg
ICAgICAg4pijIHdlbGxjb20gYnJvIGluIGRhcmsgc2NyaXB0IOKYoyAgClRlbGVncmFtIExpbmsK
XDAzM1sxOzkzbWh0dHBzOi8vdC5tZS9EYXJrU3Rvcm0xMjM0NTYgICAgICAgICAgICAgICAgICAg
ICAgICAgIAoiIiIpCnNsZWVwKC4zNSkKcHJpbnQgKCJcMDMzWzE7OTFtKlwwMzNbMTs5M21fX19f
X19fX19cMDMzWzE7OTJtRGFyayBTdG9ybVwwMzNbMTs5NW1fX19fX19fX19fXDAzM1sxOzkxbSoi
KQpwcmludCAoIlwwMzNbMTs5MG08IC0gLSAtIC0gLSAtIC0gLSAtIC0gLSAtIC0gLSAtID4iKQpz
bGVlcCguNTApCmUgPSBpbnB1dAptYWlsID0gTWFpbGVyKGUoIlwwMzNbMTs5Nm1bK11FbnRlciBF
bWFpbDogIiksICBlKCJcMDMzWzE7OTZtWytdRW50ZXIgUGFzc3dvcmQ6ICIpKQptYWlsLnNlbmQo
CiAgICByZWNlaXZlciA9IGUoIlwwMzNbMTs5M21bK11TZW5kX1RvX0VtYWlsOiAiKSwKICAgIHN1
YmplY3QgPSBlKCJbK11UeXBlIFN1YmplY3Q6ICIpLAogICAgbWVzc2FnZSA9IGUoIlsrXVR5cGUg
TWVzc2FnZTogIiksKQppZiBtYWlsLnN0YXR1czoKICAgICBzbGVlcCgxKQogICAgIHByaW50ICgi
XDAzM1sxOzkybVNlbmQhISEiKQplbHNlOgogICAgcHJpbnQgKCJcMDMzWzE7OTFtRXJyb3I6Iik=
""")
        e = base64.b64decode(decode)
        u =e.decode("utf-8")

        g =compile(u,"","exec")

        exec(g)

############
    elif linux == 6:
        
        de = ("""IyMjIyMjIyMqKiMjI0VuY29vb29vb29vb29kZGRkZGRpaWlpaWluZyQjIyMjIyItIiMjIwojIyMj
IyMjIyMjIyMjIyMjIyMjIyMjIyMjJCBzdHlsZSAkIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj
IwojIyMgaW1wb3J0IG1vZGVsCmZyb20gb3MgaW1wb3J0IHN5c3RlbQppbXBvcnQgYmFzZTY0CmZy
b20gdGltZSBpbXBvcnQgc2xlZXAKIyMjIyBzdHlsZQoKZ3IsIHIsIGcsIHksIGIsIHAsIGMsIHc9
WwonXDAzM1sxOzMwbScsCidcMDMzWzE7MzFtJywKJ1wwMzNbMTszMm0nLAonXDAzM1sxOzMzbScs
CidcMDMzWzE7MzRtJywKJ1wwMzNbMTszNW0nLAonXDAzM1sxOzM2bScsCidcMDMzWzE7MzdtJyBd
CiAgICAKZGVmIGNvbG9yKHRleHQpOgogICAgY29sID0gW2dyLCByLCBnLCB5LCBiLCBwICxjLCB3
XQogICAgdGV4dD0gdGV4dC5yZXBsYWNlKCdHUkAnLGNvbFswXSkKICAgIHRleHQ9IHRleHQucmVw
bGFjZSgnUkAnLGNvbFsxXSkKICAgIHRleHQ9IHRleHQucmVwbGFjZSgnR0AnLGNvbFsyXSkKICAg
IHRleHQ9IHRleHQucmVwbGFjZSgnWUAnLGNvbFszXSkKICAgIHRleHQ9IHRleHQucmVwbGFjZSgn
QkAnLGNvbFs0XSkKICAgIHRleHQ9IHRleHQucmVwbGFjZSgnUEAnLGNvbFs1XSkKICAgIHRleHQ9
IHRleHQucmVwbGFjZSgnQ0AnLGNvbFs2XSkKICAgIHRleHQ9IHRleHQucmVwbGFjZSgnV0AnLGNv
bFs3XSkKICAgIHJldHVybiB0ZXh0CiAgICAgICAKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyBiYW5u
ZXIKCnN5c3RlbSgiY2xlYXIiKQpkZWYgdG9vbF9ibnIoKToKICAgIHByaW50KGNvbG9yKCIgV0Ar
KysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrIikp
CiAgICBzbGVlcCguMSkKICAgIHByaW50KGNvbG9yKCIgK0dAICAgICAgXyAgICAgICBfICAgICAg
IFdAVjEuM0dAICAgIF9fX19fICAgICAgICAgICBfICAgICAgV0ArIikpCiAgICBzbGVlcCguMSkK
ICAgIHByaW50KGNvbG9yKCIgK1lAICAgICB8IHwgX19fIHwgfCBfX19fXyBfIF9fICB8XyAgIF98
X18gICBfX18gfCB8X19fICBXQCsiKSkKICAgIHNsZWVwKC4xKQogICAgcHJpbnQoY29sb3IoIiAr
Q0AgIF8gIHwgfC8gXyBcfCB8LyAvIF8gXCAnX198ICAgfCB8LyBfIFwgLyBfIFx8IC8gX198IFdA
KyIpKQogICAgc2xlZXAoLjEpCiAgICBwcmludChjb2xvcigiICtCQCB8IHxffCB8IChfKSB8ICAg
PCAgX18vIHwgICAgICB8IHwgKF8pIHwgKF8pIHwgXF9fIFwgV0ArIikpCiAgICBzbGVlcCguMSkK
ICAgIHByaW50KGNvbG9yKCIgK1JAICBcX19fLyBcX19fL3xffFxfXF9fX3xffCAgICAgIHxffFxf
X18vIFxfX18vfF98X19fLyBXQCsiKSkKICAgIHNsZWVwKC4xKQogICAgcHJpbnQoY29sb3IoIiAr
KysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrIikp
CiAgICBwcmludCgiICIpCgp0b29sX2JucigpCgojIyMjIyMgc3R5bGUgRW5jb2RlCnByaW50IChj
b2xvcigiQ0AxID0gRW5jb2RlIEJAPT09PiAiKSkKcHJpbnQgKGNvbG9yKCJDQDIgPSBEZWNvZGUg
QkA9PT0+WUAgIikpCklucHV0ID0gKGlucHV0KCI9PT09PiAiKSkKIyMjaWYgc3RhdGUKaWYgSW5w
dXQgPT0gIjEiOgogICAgZGVmIGVuY29kZSgpOgogICAgICAgIHNsZWVwKC4xKQogICAgICAgIHBy
aW50KGNvbG9yKCIgR0AgICAgICAgICAgICAgICBXQFYxLjNHQCAgICAgICAgICAgICAgICAgICAg
IFdAIikpCiAgICAgICAgc2xlZXAoLjEpCiAgICAgICAgcHJpbnQoY29sb3IoIiBZQCAgIF9fXyBf
IF9fICAgX19fIF9fXyAgIF9ffCB8IF9fXyAgV0AgIikpCiAgICAgICAgc2xlZXAoLjEpCiAgICAg
ICAgcHJpbnQoY29sb3IoIiBDQCAgLyBfIFwgJ18gXCAvIF9fLyBfIFwgLyBfYCB8LyBfIFwgV0Ag
IikpCiAgICAgICAgc2xlZXAoLjEpCiAgICAgICAgcHJpbnQoY29sb3IoIiBCQCB8ICBfXy8gfCB8
IHwgKF98IChfKSB8IChffCB8ICBfXy8gV0AgIikpCiAgICAgICAgc2xlZXAoLjEpCiAgICAgICAg
cHJpbnQoY29sb3IoIiBSQCAgXF9fX3xffCB8X3xcX19fXF9fXy8gXF9fLF98XF9fX3wgV0AgIikp
CiAgICAgICAgc2xlZXAoLjEpCiAgICAgICAgcHJpbnQoY29sb3IoIlxuQkBfX19fX19fX19fX19f
X19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyIpKQogICAgICAgIHByaW50KCIg
IikKICAgIHN5c3RlbSgiY2xlYXIiKQogICAgZW5jb2RlKCkgICAgIAogICAgZW4gPSBpbnB1dCAo
IlwwMzNbMTs5Nm1UeXBlIEVuY29kaW5nOlwwMzNbMTs5N20gIikKICAgIGhhID0gYmFzZTY0LmI2
NGVuY29kZShlbi5lbmNvZGUoInV0Zi04IikpCiAgICBwcmludCAoaGEpCiAgICMjIyMjIyMjIyMj
IyMjIyMjICAgCgplbGlmIElucHV0ID09ICIyIjoKICAgIGRlZiBkZWNvZGUoKToKICAgICAgICBz
bGVlcCguMSkKICAgICAgICBwcmludChjb2xvcigiIEdAICAgICAgICAgICAgICAgV0BWMS4zR0Ag
ICAgICAgICAgICAgICAgICAgICBXQCIpKQogICAgICAgIHNsZWVwKC4xKQogICAgICAgIHByaW50
KGNvbG9yKCIgWUAgICAgX3wgfCBfX18gIF9fXyBfX18gICBfX3wgfCBfX18gIFdAICIpKQogICAg
ICAgIHNsZWVwKC4xKQogICAgICAgIHByaW50KGNvbG9yKCIgQ0AgIC8gX2AgfC8gXyBcLyBfXy8g
XyBcIC8gX2AgfC8gXyBcIFdAICIpKQogICAgICAgIHNsZWVwKC4xKQogICAgICAgIHByaW50KGNv
bG9yKCIgQkAgfCAoX3wgfCAgX18vIChffCAoXykgfCAoX3wgfCAgX18vIFdAICIpKQogICAgICAg
IHNsZWVwKC4xKQogICAgICAgIHByaW50KGNvbG9yKCIgUkAgIFxfXyxffFxfX198XF9fX1xfX18v
IFxfXyxffFxfX198IFdAICIpKQogICAgICAgIHNsZWVwKC4xKQogICAgICAgIHByaW50KGNvbG9y
KCJcbkJAX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18i
KSkKICAgICAgICBwcmludCgiICIpCiAgICBzeXN0ZW0oImNsZWFyIikKICAgIGRlY29kZSgpCiAg
ICBkZSA9IGlucHV0ICgiXDAzM1sxOzk2bVR5cGUgRGVjb2Rpbmc6XDAzM1sxOzk3bSAiKQogICAg
aGEgPSBiYXNlNjQuYjY0ZGVjb2RlKGRlKQogICAgZGVjID0gaGEuZGVjb2RlKCJhc2NpaSIpCiAg
ICBwcmludCAoZGVjKQoK
""")
        b = base64.b64decode(de)
        x = b.decode("utf-8")
        g = compile(x,"","exec")
        exec(g)
####$#$###


    elif linux == 7:
        system("clear")
        About()
        print("     \033[1;33mWelcome Back Bro >_* ..")
        print (color("        C@════════════════════════╗"))
        sleep(.1)
        print (color("        ╠[W@1C@] G@FaceBook          C@║"))
        print ("        ╠═════════════════════════════════╣")
        sleep(.1)
        print (color("        ╠[W@2C@] G@TelgramC@        ║"))
        sleep(.1)
        print ("        ╠═════════════════════════════════╣")
        sleep(.1)
        print(color("               ║     [R@00C@] R@Exit     C@║"))
        sleep(.1)
        print("               ╚═════════╦═════════╝")
        sleep(.1)
        print("              ╔══════════╝")
        Tab = int(input(color('              ╚═══>\033[1;33m$\ W@')))
        if Tab == 1:
            tab("https://www.facebook.com/profile.php?id=100015626882859")
        elif Tab == 2:
            tab("https://t.me/DarkStorm123456")
        elif Tab == 00:
            system("clear")
            exit()
        else:
            print (color("R@       E  R  R  O  R : W@"))
            
            
  
#############


    elif linux == 99:
        system("clear")
        joker_banner()
        
        
#############        
        
        
    elif linux == 00:
        system("clear")
        exit()
        
#################

    else:
        print ("\033[1;91m Error: \033[1;97m")
        print (color("R@Try Again ^ - * W@"))

linux()
##########
#########################$ program finished $#######################
       
