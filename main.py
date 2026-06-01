Last login: Mon Jun  1 15:36:19 on ttys001
(base) kinglickass@Kings-MacBook-Air-6 ~ % python main.py
python: can't open file '/Users/kinglickass/main.py': [Errno 2] No such file or directory
(base) kinglickass@Kings-MacBook-Air-6 ~ % cd CoolAF/gamestory
(base) kinglickass@Kings-MacBook-Air-6 gamestory % python main.py
(base) kinglickass@Kings-MacBook-Air-6 gamestory % git clone https://github.com/Eightdevvis/king.git
Cloning into 'king'...
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 0), reused 7 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (7/7), done.
(base) kinglickass@Kings-MacBook-Air-6 gamestory % hx .









    1  import pygame                                                            
    2  pygame.init()                              W292 no newline at end of file
    3  screen = pygame.display.set_mode((800, 600))                       (W292)
    4  pygame.display.set_caption("idlezone")                                   
    5  running = True                                                           
    6  while running:                                                           
    7      for event in pygame.event.get():                                     
    8          if event.type == pygame.QUIT:                                    
    9              running = False                                              
   10      pygame.display.flip()                                                
●  11  pygame.quit()                                                            
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
 INS   main.py [+]                                            ● 1  1 sel  11:14 
                                                                                
