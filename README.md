cuckoo-fu
=========

Kung-fu scripts and add-on for Cuckoo Sandbox. Have fun and keep hacking!

Modules
=======

Reporting / dogeon
------------------

Adds reporting in DOGEON format (see http://dogeon.org/).
 
How to install:

Setup requirements with:

```
pip install dogeon
```

Copy this file in reporting modules folder, in /modules/reporting. Enable the module
Adding the following lines to reporting.conf, in /conf/reporting.conf:

```
[dogeon]
enabled = yes
```

Run cuckoo and use doge power with care.

Credits
=======

 * Alessandro Tanasi (@jekil)
 * Machete (pic below)

```
,,,,,,,,............................................................  .         
.,,,,,............................................................  ..          
,,........................................................O888888= ...          
... . ..................  .............................. 8877I7$O8$..           
....................... .    ...........................$8777IIIIO$,            
...................  ..  ...      ......................887$7Z7IIOO:            
.................  ...             ....................$DZ$$ZIZ$I$O$            
...... ..........    ...            ...................O8Z777IIII$8I            
.........    .....     .....          .............. .:ZOZ$ZZZ$7IOO~            
........... ......       .    .       ............. ...,OZI77I777OO=.           
.................. ......      ..   ..............   ...O8O$$77I$Z$?.           
........ ............   .....        ..............$ZO?Z88OOZ$77ZOOOI,..        
.,++.................   .. ..     . .............?ZOO88888O$$$7$ZO88OO=7.       
.++??.......................   ................?I7OO88D8888O$$$ZZD8888OO$?    ..
.:++8?I.......................................IIIOOO888O88O88888OZO8O8OOOZ.    .
.....=OIO....................................I77Z8OO8O888888O888Z8OO888OOO+     
.......+8I$.................................$777ZOOO888888888888888OO8D8Z$+=    
.........+?I?..... ........................7II7$ZOOOO8O888888D88OOOOO8DD$7?=    
..........:O??+.... ........ ............=III77$ZOOOZOOO8888888ZZZOO888OZZI=,   
............+O+?+... .......     ..... .I7IIII$$OOZZZZZO$O8OZZZZO78888O78Z7I?.  
..............+OII=............ ... ?I7I7III777. :Z$ZZZOOOOOOZOOOO8888$88O$7$~  
.................?IZ.............,IIIZIIII77.     IZZZZOOOOOO8888D88ONZ8O8$ZZI. 
..................,?7+.II:... ?I7IIII$II77?       +$OOO888DDND88888OO8$Z.OZ$$ZI 
...................+?8I7O7I.7IIIII7IIIII          IIOO888DDDD888888OZOZ8 IOZOOO$
....................,77III$777III.                7ZO888DDDDD8D8888OZZOO  OO88O$
=.....................?777O7. ...                 +ZO888DDDDDDDD888OZZZ$  .OOOOZ
...............:,,,.....I=8=  .                   ?$OOODD8NNNNND888OZOZO   $88OO
~::............=I~~............  ...             .77O8DNNNNNNNNNNDOOO8DI   ?O8OO
+~::::,....?I?7~?:................  ....          ~DDNNNNNNNNNNNNNNDOOO$    Z88O
+~~,~::?$7?I7??=++~=,,,,,.,,....,,......   ..... .7888DDNNNNNNNNNNNNN8$.    IOO8
+=~~+~~:~=I+77I77~==~==:II=I=+??+=?=~~=+=~:,.::..8DN$DDNNNDODNNN8DNDDO8+     7ZO
:::~:~~=::::=~=~7==?=:=~II$7?+II===+::=++7I=I7=?=DNNIO8NNNDZDDDDDDNNNNNN. .. .7Z
::::~::::?~=~:~~+~:::~:~~~::~:::~~:::~=+7$I++?=?+ZDN$=NNNNNNNNNNNNNNNNNN7?=+=?IZ
~::=:::=::::~~~~~~::~:,::,,::::~,,,,~:,~:::=:::~,DDNNNNNNNNNNNNNNNNNNNNND+?7???O
```