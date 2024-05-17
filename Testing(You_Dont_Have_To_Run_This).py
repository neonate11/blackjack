import random
import os
import platform
import time
screen_width = os.get_terminal_size()[0] 
screen_height = os.get_terminal_size()[1]

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

heart = '\u2665'
print('Original Card Design:')
print('┌─────────┐')
print('│ ▓▓▓▓▓▓▓ │')
print('│ ▓▓▓▓▓▓▓ │')
print('│ ▓▓▓▓▓▓▓ │')
print('│ ▓▓▓▓▓▓▓ │')
print('│ ▓▓▓▓▓▓▓ │')
print('└─────────┘')
print('┌─────────┐')
print('│8♥       │')
print('│         │')
print('│    ♥    │')
print('│         │')
print('│       8♥│')
print('└─────────┘')
print('New Deck Design:')
'backside'
print('╭─────────╮')
print('│⚜ ⚜ ⚜ ⚜  │')
print('│ ⚜ ⚜ ⚜ ⚜ │')
print('│⚜ ⚜ ⚜ ⚜  │')
print('│ ⚜ ⚜ ⚜ ⚜ │')
print('│⚜ ⚜ ⚜ ⚜  │')
print('╰─────────╯')
'shoe'
print('▗▄▄▄▄▄▄▄▄▄')
print('▐█████████')
print('▐█████████')
print('▐█████████')
print('▐█████████')
print('▐█████████')
print('▝▀▀▀▀▀▀▀▀▀')
'3'
print('╭─────────╮')
print('│3   ♥    │')
print('│         │')
print('│    ♥    │')
print('│         │')
print('│    ♥   3│')
print('╰─────────╯')
'4'
print('╭─────────╮')
print('│4 ♥   ♥  │')
print('│         │')
print('│         │')
print('│         │')
print('│  ♥   ♥ 4│')
print('╰─────────╯')
'5'
print('╭─────────╮')
print('│5 ♥   ♥  │')
print('│         │')
print('│    ♥    │')
print('│         │')
print('│  ♥   ♥ 5│')
print('╰─────────╯')
'6'
print('╭─────────╮')
print('│6 ♥   ♥  │')
print('│         │')
print('│  ♥   ♥  │')
print('│         │')
print('│  ♥   ♥ 6│')
print('╰─────────╯')
'7'
print('╭─────────╮')
print('│7 ♥   ♥  │')
print('│    ♥    │')
print('│  ♥   ♥  │')
print('│         │')
print('│  ♥   ♥ 7│')
print('╰─────────╯')
'8'
print('╭─────────╮')
print('│8 ♥   ♥  │')
print('│    ♥    │')
print('│  ♥   ♥  │')
print('│    ♥    │')
print('│  ♥   ♥ 8│')
print('╰─────────╯')
'9'
print('╭─────────╮')
print('│9 ♥   ♥  │')
print('│  ♥   ♥  │')
print('│    ♥    │')
print('│  ♥   ♥  │')
print('│  ♥   ♥ 9│')
print('╰─────────╯')
'10'
print('╭─────────╮')
print('│10 ♥ ♥   │')
print('│  ♥ ♥ ♥  │')
print('│         │')
print('│  ♥ ♥ ♥  │')
print('│   ♥ ♥ 10│')
print('╰─────────╯')
'Jack'
print('╭─────────╮')
print('│J┌─────┐ │')
print('│♥│▓▓▒▒▓│ │')
print('│ │░░░░░│ │')
print('│ │▓▒▒▓▓│♥│')
print('│ └─────┘J│')
print('╰─────────╯')
'Queen'
print('╭─────────╮')
print('│Q┌─────┐ │')
print('│♥│▓▓▒▒▓│ │')
print('│ │░░░░░│ │')
print('│ │▓▒▒▓▓│♥│')
print('│ └─────┘Q│')
print('╰─────────╯')
'King'
print('╭─────────╮')
print('│K┌─────┐ │')
print('│♥│▓▓▒▒▓│ │')
print('│ │░░░░░│ │')
print('│ │▓▒▒▓▓│♥│')
print('│ └─────┘K│')
print('╰─────────╯')

#ACES
'Ace of hearts'
print('╭─────────╮')
print('│A  _ _   │')
print('│♥ ( V )  │')
print('│   \ /   │')
print('│    V   ♥│')
print('│        A│')
print('╰─────────╯')
'Ace of Spades'
print('╭─────────╮')
print('│A   .    │')
print('│♠  / \   │')
print('│  (_._)  │')
print('│    |   ♠│')
print('│        A│')
print('╰─────────╯')
'Ace of Diamonds'
print('╭─────────╮')
print('│A   ^    │')
print('│♦ /   \  │')
print('│  \   /  │')
print('│    v   ♦│')
print('│        A│')
print('╰─────────╯')
'Ace of Clubs'
print('╭─────────╮')
print('│A   _    │')
print('│♣  ( )   │')
print('│  (_\'_)  │')
print('│    |   ♣│')
print('│        A│')
print('╰─────────╯')


'''

          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
ejm98    |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|

                              
//        ⎹          ╱               ⟋            ⎽⎼⎻⎺                                       
//        |         ╱              ⟋           ⎽⎼⎻⎺                                          
//        ⎸        ╱             ⟋          ⎽⎼⎻⎺                                             
//       ⎹        ╱            ⟋         ⎽⎼⎻⎺       _-‾                                      
//       |       ╱           ⟋        ⎽⎼⎻⎺       _-‾               __---‾‾         _⎽⎽⎼⎼⎻⎻⎺⎺ 
//       ⎸      ╱          ⟋       ⎽⎼⎻⎺       _-‾           __---‾‾         _⎽⎽⎼⎼⎻⎻⎺⎺‾       
//      ⎹      ╱         ⟋      ⎽⎼⎻⎺       _-‾       __---‾‾       _⎽⎽⎼⎼⎻⎻⎺⎺‾                
//      |     ╱        ⟋     ⎽⎼⎻⎺       _-‾   __---‾‾       _⎽⎽⎼⎼⎻⎻⎺⎺‾                       
//      ⎸    ╱       ⟋    ⎽⎼⎻⎺                                                               
//          ╳      ⤫                                                                         
//      ⎸    ╲       ⟍    ⎺⎻⎼⎽          ‾-_   ‾‾---__       ‾⎺⎺⎻⎻⎼⎼⎽⎽_                       
//      |     ╲        ⟍     ⎺⎻⎼⎽          ‾-_       ‾‾---__        ‾⎺⎺⎻⎻⎼⎼⎽⎽_               
//      ⎹      ╲         ⟍      ⎺⎻⎼⎽          ‾-_           ‾‾---__        ‾⎺⎺⎻⎻⎼⎼⎽⎽_        
//       ⎸      ╲          ⟍       ⎺⎻⎼⎽          ‾-_                ‾‾---__       ‾⎺⎺⎻⎻⎼⎼⎽⎽_ 
//       |       ╲           ⟍        ⎺⎻⎼⎽          ‾-_                                      
//       ⎹        ╲            ⟍         ⎺⎻⎼⎽                                                
//        ⎸        ╲             ⟍          ⎺⎻⎼⎽                                             
//        |         ╲              ⟍           ⎺⎻⎼⎽ 
//        ⎹          ╲               ⟍         

           .....
        _d^^^^^^^^^b_
     .d''           ``b.
   .p'     Objects     `q.
  .d'   in mirror may   `b.
 .d'   be less virtual   `b.
 ::   than they appear.   ::
 ::  ...................  ::
 ::                       ::
 `p.  johnca@netcom.com  .q'
  `p.   John Abbe aka   .q'
   `b.     Rademir     .d'
     `q..          ..p'
        ^q........p^

            

        _.,,,,,,,,,._
     .d''           ``b.
   .p'     Objects     `q.
 .d'   in mirror may    `b.
 .d'   be less virtual   `b.
 ::   than they appear.   ::
 `p.  johnca@netcom.com  .q'
  `p.   John Abbe aka   .q'
   `b.     Rademir     .d'
     `q..            ..,'
        '',,,,,,,,,,''


        . -- ~~~ -- .
    .-~               ~-.
   /                     \
  /                       \
 |                         |
 |                         |
 |                         |
  \                       /
   \                     /
    `-.               .-'
        ~- . ___ . -~


         , - ~~ - ,
     , '            ' ,
   ,                    ,
  ,                      ,
 ,                        ,
 ,                        ,
 ,                        ,
  ,                      ,
   ,                    ,
     ,                , 
       ' - , __ , - '

        *  *              *  *
     *        *        *        *
    *          *      *          *
    *          *      *          *
     *        *        *        *
        *  *              *  *


        /  /              /  /
     /        /        /        /
    /          /      /          /
    /          /      /          /
     /        /        /        /
        /  /              /  /


        o  o              o  o
     o        o        o        o
    o          o      o          o
    o          o      o          o
     o        o        o        o
        o  o              o  o


        =  =              =  =
     =        =        =        =
    =          =      =          =
    =          =      =          =
     =        =        =        =
        =  =              =  =



        x  x              x  x
     x        x        x        x
    x          x      x          x
    x          x      x          x
     x        x        x        x
        x  x              x  x



                                              _  _
             =  =                          =        =
          =        =                     =            =
         =          =                   =              =
         =          =                   =              =
          =        =                     =            =
             =  =                          =        =
                                              ~  ~


           %%%    %%%
      %%%              %%%

  %%%                      %%%

 %%%                         %%%

 %%%                         %%%

 %%%                        %%%

    %%%                  %%%

          %%%     %%%

                                                                                                                                                            
                                                                                                                                                  
                                                                          ▓▓▓▓▓▓                                                                  
                                                                  ▒▒░░            ░░▒▒                                                            
                                                              ▒▒                        ▒▒                                                        
                                                            ▒▒                            ▒▒                                                      
                                                          ▒▒                                ▓▓                                                    
                                                        ░░                                    ▒▒                                                  
                                                        ▒▒                                    ░░                                                  
                                                                                                ▒▒                                                
                                                      ▒▒                                        ░░                                                
                                                      ▒▒                                                                                          
                                                      ░░                                                                          
                                                      ░░                                                                               
                                                      ▒▒                                        ░░░                                    
                                                      ██                                        ▓▓                                        
                                                                                                ▒▒                                          
                                                        ▓▓                                    ▓▓                                                  
                                                          ▓▓                                ░░                                             
                                                          ▓▓▒▒                              ▓▓                                                    
                                                             ▒▒                        ░░░░░        
                                                                ▒▒░░                  ▒▒      
                                                                      ▒▒▒▒░░  ▒▒▒▒▒▒           
                                                                                                                 
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  


'''