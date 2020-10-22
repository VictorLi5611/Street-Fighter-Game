"""
VARIABLE MAP
VARIABLE                  PURPOSE                                                TYPE                       RANGE
screenWidth               Width of screen                                        int                        1300
screenHeight              Height of screen                                       int                        700
arena                     Image of the arena                                     img                        N/A
mode                      State of program                                       string                     play, menu, gameover, help
ryu_stand                 Image of Standing Ryu
ryu_punch                 Image of punching Ryu 
ryu_kick                  Image of Kicking Ryu
ryu_jump                  Image of Ryu Jumping
characterScale            Scaling the charicatar images
ryuHeight                 Height of ryu
ryuStandWidth             Width of Standing Ryu 
ryuPunchWidth             Width of Punching Ryu
ryuKickWidth              Width of Kicking Ryu
ryuX                      X posision of Ryu
ryuY                      Y posision of Ryu
speedX                    Movement of Ryu in the X direction
speedY                    Movement of Ryu in the Y direction
ryuJumpWidth              Width of Ryu Jumping Image
ryuJumpHeight             Height of Ryu Jumping Image
jump                      To indecated when to Jump for Ryu      
counter                   Delay for the ranged attack for Ryu
counter2                  Delay for the ranged attack for Ken         
ryu_ranged                Image of Ryu doing the ranged attacks
ryuRangedWidth            The Width of Ryu's Ranged attack
ryuRangedHeight           The Height of Ryu Ranged attack
bullet                    Loads the Image of the bullet for Ryu
bulletX                   The X posision of Ryu's bullet
bulletY                   The Y posision of Ryu's bullet
bulletWidth               The Width of Ryu's bullet
bulletHeight              The Height of Ryu's bullet
bulletSpeed               The X increments of the Ryu's bullet
showBullet                To deterimin when Ryu can shoot his bullet
rangedTimer               The delay so you can't spam ranged attacks
ryu_crouch                Image of Ryu crouching
ryuCrouchHeight           The height of Ryu crouching
ryuCrouchWidth            The width of Ryu crouching
ryuDeath                  The sound when Ryu Dies
ryuKick                   The sound when Ryu Kicks
ryuPunch                  The sound when Ryu Punches
ryuHaduken                The sound when Ryu uses his ranged attack
kenX                      The X posision of Ken
kenY                      The Y posision of Ken
kenHeight                 The Height of Ken
kenStandWidth             The Width of Ken Standing
ken_stand                 The Image of Ken standing
kenPunchWidth             The Width when Ken is Punching
kenKickWidth              The Width when Ken is Kicking
kenRangedHeight           The Height when Ken is using its ranged attack
kenRangedWidth            The Width when Ken is using its ranged attack
kenJumpWidth              The Width when Ken is jumping
kenJumpHeight             The Height when Ken is jumping
kenCrouchWidth            The Width when Ken is crouching
kenCrouchHeight           The Height when Ken is crouching
ken_punch                 The Image for Ken's Punch
ken_kick                  The Image for Ken's Kick
ken_jump                  The Image for Ken's jump
ken_ranged                The Image for Ken's ranged attack
bullet2                   The Image for Ken's Haduken
ken_crouch                The Image for Ken's Crouching
speedX2                   Used for the movement of Ken X pos
bulletSpeed2              Used for the movement of Kens ranged attack
showBullet2               Used to determine if it should show the rannged attack
bulletX2                  The X pos of Ken's ranged attack missle
rangedTimer2              The delay on ken's ranged attack (can't spam)
speedY2                   Used for the movement of Kens Y pos
bulletY2                  Used for the movement of Kens ranged attack (Y pos)
bar                       The Image of the Brige in the middle                   
kenHealth                 The health of Ken
ryuHealth                 The health of Ryu
timer                     The match timer
f                         The font of the text
keyCheck                  cheak if the key is being pressed
score                     The score between player 1 and player 2
ranged_block
ranged_block2
startMenuX2, startMenuY2, startMenuWidth2, menuBarX2, menuBarY2, menuHeight2, menuWidth2
"""
add_library("minim")
minim = Minim(this)
import random
import pickle

def setup():
    #Globalize variables
    global screenWidth, screenHeight, arena, mode, ryu_stand, ryuStandWidth, ryuHeight, ryuX, ryuY, characterScale, speedX, ryu_punch, ryuPunchWidth, ryu_kick, ryuKickWidth, ryu_jump
    global ryuJumpWidth, ryuJumpHeight, speedY, jump, counter, counter2, ryu_ranged, ryuRangedWidth, ryuRangedHeight, bullet, bulletX, bulletY, bulletWidth, bulletHeight, bulletSpeed, showBullet
    global rangedTimer, ryu_crouch, ryuCrouchHeight, ryuCrouchWidth, ryuDeath, ryuKick, ryuPunch, ryuHaduken, kenX, kenY, kenHeight, kenStandWidth, ken_stand
    global kenPunchWidth, kenKickWidth, kenRangedHeight, kenRangedWidth, kenJumpWidth, kenJumpHeight, kenCrouchWidth, kenCrouchHeight, ken_punch, ken_kick, ken_jump, ken_ranged
    global bullet2, ken_crouch, speedX2, bulletSpeed2, showBullet2, bulletX2, rangedTimer2, speedY2, bulletY2, bar, keyList, kenHealth, ryuHealth, timer, f, keyCheck, score
    global ranged_block, ranged_block2, startMenuX2, startMenuY2, startMenuWidth2, menuBarX2, menuBarY2, menuHeight2, menuWidth2
    global allBoundaries, menuBarX, menuBarY, menuHeight, menuWidth, activeMenuItems, whichMenuItem, numMenuItems, menuChosen, removeMenuItem, startMenuX, startMenuY
    global backroundX, backroundY, menu,title, play, help, scores, main, startMenuWidth, playChosen, helpChosen, scoresChosen, score2, numMenu2Items
    global playTextX, playTextY, helpTextX, helpTextY, scoreTextX, scoreTextY, playerName, validkey, shield, shieldOn, shieldOn2, shield2, mainMenuSound
    global numHelpItems, name, string, player2name, name2, string2, ryuCombo, kenCombo, ryuMaxCombo, kenMaxCombo, reset, reset2, kenKick, kenPunch, kenHaduken
    global results, result, scoreBoxX, scoreBoxY, startBoxX, startBoxY, scoreBoxWidth, scoreBoxHeight, nameBoxX, nameBoxY, startNameBoxX, startNameBoxY, numScoresItems, scoreBoxInterval, incrY

    #Initialize variables
    screenWidth = 1536
    screenHeight = 988
    size(1536, 988)
    
    mode = "menu"

    arena = loadImage("map.jpg")
    ryu_stand = loadImage("ryu_stand.png")
    ryu_punch = loadImage("ryu_punch.png")
    ryu_kick = loadImage("ryu_kick.png")
    ryu_jump = loadImage("ryu_jump.png")
    ryu_ranged = loadImage("ryu_ranged.png")
    bullet = loadImage("ryu_bullet.png")
    ryu_crouch = loadImage("ryu_crouch.png")
    
    ken_stand = loadImage("ken_stand.png")
    ken_punch = loadImage("ken_punch.png")
    ken_kick = loadImage("ken_kick.png")
    ken_jump = loadImage("ken_jump.png")
    ken_ranged = loadImage("ken_ranged.png")
    bullet2 = loadImage("ken_bullet.png")
    ken_crouch = loadImage("ken_crouch.png")
    bar = loadImage("bar.png")
    shield = loadImage("shield.png")
    shield2 = loadImage("shield.png")
    
    characterScale = 4
    ryuHeight = 117 * characterScale
    ryuStandWidth = 57 * characterScale
    ryuPunchWidth = 85 * characterScale
    ryuKickWidth = 78 * characterScale
    ryuRangedWidth = 372.5
    ryuRangedHeight = 368
    ryuJumpWidth = 202.5 
    ryuJumpHeight = 323
    ryuCrouchHeight = 317
    ryuCrouchWidth = 208
    ryuX = 100
    ryuY = screenHeight - ryuHeight - 30
    
    kenHeight = 117 * characterScale
    kenStandWidth = 49 * characterScale
    kenX = screenWidth - kenStandWidth - 90
    kenY = screenHeight - kenHeight - 30
    kenPunchWidth = 79 * characterScale
    kenKickWidth = 99 * characterScale
    kenRangedWidth = 372.5
    kenRangedHeight = 368
    kenJumpWidth = 178 
    kenJumpHeight = 374
    kenCrouchHeight = 374
    kenCrouchWidth = 178
    
    bulletX = ryuX + ryuRangedWidth
    bulletX2 = kenX - kenRangedWidth + 50
    bulletY = ryuY + ryuRangedHeight/2 - 30
    bulletY2 = kenY + kenRangedHeight/2 - 30
    bulletWidth = 148.5
    bulletHeight = 110
    bulletSpeed = 0
    bulletSpeed2 = 0
    
    minim = Minim(this)
    ryuDeath = minim.loadFile( "Ryu_Death.mp3" )
    ryuKick = minim.loadFile( "Ryu_Kick.mp3")
    ryuPunch = minim.loadFile( "Ryu_Punch.mp3" )
    ryuHaduken = minim.loadFile( "Ryu_Haduken.mp3" )
    kenKick = minim.loadFile( "Ken_Kick.mp3")
    kenPunch = minim.loadFile( "Ken_Punch.mp3" )
    kenHaduken = minim.loadFile( "Ken_Haduken.mp3" )
    mainMenuSound = minim.loadFile("MainMenuSounds.mp3")
    
    mainMenuSound.loop()

    speedX = 0
    speedX2 = 0
    speedY = 0
    speedY2 = 0
    jump = False
    rangedTimer = True
    rangedTimer2 = True
    counter = 0
    counter2 = 0
    showBullet = False
    showBullet2 = False    
    
    ryuHealth = 100
    kenHealth = 100
    timer = 60
    
    f = loadFont("BitstreamVeraSans-BoldOblique-48.vlw")
    
    keyCheck = [False for i in range(10)]
    
    ranged_block = False
    ranged_block2 = False
    
    score = [0, 0]
    
    allBoundaries = []
    startMenuX = 0
    startMenuY = 400
    startMenuWidth = 300
    menuBarX = startMenuX
    menuBarY = startMenuY
    menuHeight = 200
    menuWidth = 300
    numMenuItems = 3
    numMenu2Items = 3
    numHelpItems = 2
    removeMenuItem = True
    
    startMenuX2 = 100
    startMenuY2 = 658
    startMenuWidth2 = 300
    menuBarX2 = startMenuX
    menuBarY2 = startMenuY
    menuHeight2 = 100
    menuWidth2 = 500
    playTextX = menuBarX + 100
    playTextY = menuBarY + 100
    helpTextX = menuBarX + 200,
    helpTextY = menuBarY + 300 
    scoreTextX = menuBarX + 300
    scoreTextY = menuBarY + 500
    

    whichMenuItem = -1
    
    
    #Initialize variables
    screenWidth = 1536
    screenHeight = 988
    size(1536, 988)
    backroundX = 0
    backroundY = 0
    
    playChosen = 0
    helpChosen = 1
    scoresChosen = 2
    
    main = loadImage("Menu.jpg")
    title = loadImage("Title.PNG")
    play = loadImage ("Play.PNG") 
    help = loadImage ("Help.PNG")
    score2 = loadImage ("Scores.PNG")
    
    name = []
    string = ""
    name2 = []
    string2 = ""
    
    player2name = False
    playerName = False
    
    ryuCombo = 0
    kenCombo = 0
    ryuMaxCombo = 0
    kenMaxCombo = 0
    shieldOn = False
    shieldOn2 = False
    
    scoreBoxX = 750
    scoreBoxY = 250
    startBoxX = scoreBoxX
    startBoxY = scoreBoxY
    scoreBoxWidth = 500
    scoreBoxHeight = 100
    scoreBoxInterval = 100
    nameBoxX = 250
    nameBoxY = 250
    startNameBoxX = nameBoxX
    startNameBoxY = nameBoxY
    numScoresItems = 5
    incrY = 0
    results = []

    validkey = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    reset = False
    reset2 = False
           
def sortingScores(results):
    count = 0
    for i in range(len(results)-1):
        if results[i][1] < results[i + 1][1]:
            results[i], results[i + 1] = results[i + 1], results[i]
            count += 1
    if count == 0:
        return results
    else:
        return sortingScores(results)
    
def inputScores(result):
    with open("scores.txt","w") as f:
        pickle.dump(result, f)

        
def outputScores():
    with open("scores.txt","r") as f:
        results =[]  
        results = pickle.load(f)   

    return results


def draw():
    global speedX, ryuX, ryuY, speedY, jump, ryuHeight, screenHeight, counter, counter2, bulletX, showBullet, bulletSpeed, bulletSpeed2, rangedTimer, speedX2, kenX
    global showBullet2, bulletX2, rangedTimer2, speedY2, kenY, ryuHealth, kenHealth, timer, mode
    global allBoundaries, menuBarX, menuBarY, menuHeight, menuWidth, activeMenuItems, whichMenuItem, numMenuItems, menuChosen, removeMenuItem, startMenuX, startMenuY
    global backroundX, backroundY
    global menu,title, play, help, scores, main, score
    global startMenuX2, startMenuY2, startMenuWidth2, menuBarX2, menuBarY2, menuHeight2, menuWidth2
    global playTextX, playTextY, helpTextX, helpTextY, scoreTextX, scoreTextY
    global numHelpItems, ryuCombo, kenCombo, mainMenuSound
    global name, string, incrY, reset, reset2, ryuMaxCombo, kenMaxCombo
    global result, scoreScreen, scoreBoxX, scoreBoxY, startBoxX, startBoxY, scoreBoxWidth, scoreBoxHeight, nameBoxX, nameBoxY, startNameBoxX, startNameBoxY, numScoresItems, scoreBoxInterval, results
    

    if mode == "scores":
        allBoundaries = []
        background(main)
        textFont(f)
        textSize(40)
        text( "Scores" , screenWidth/2 - 100, 200)
        noFill()
        
        for i in range(numScoresItems):
            rect( nameBoxX, nameBoxY + incrY, scoreBoxWidth, scoreBoxHeight)
            rect( scoreBoxX, scoreBoxY + incrY, scoreBoxWidth, scoreBoxHeight)
            incrY += 110
        incrY = 0
        
        textSize(30)
        text ( "Return to the Main Menu" , 550 , 925) 
        rect( 400, 850, 722, 100)
        results = outputScores()
        results = sortingScores(results)
        for i in range(numScoresItems):
            rect( nameBoxX, nameBoxY + incrY, scoreBoxWidth, scoreBoxHeight)
            rect( scoreBoxX, scoreBoxY + incrY, scoreBoxWidth, scoreBoxHeight)
            text( results[i][0], nameBoxX, nameBoxY + incrY + 75)
            text (results[i][1], scoreBoxX, scoreBoxY + incrY + 75)
            incrY += 110
        incrY = 0 
        
        upperLeft =  [ 400, 850 ]
        lowerRight = [ 1122 , 950]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        
        activeMenuItems = [ True for i in range( 1 ) ]
        
        for i in range(numScoresItems):
            rect( nameBoxX, nameBoxY + incrY, scoreBoxWidth, scoreBoxHeight)
            rect( scoreBoxX, scoreBoxY + incrY, scoreBoxWidth, scoreBoxHeight)
            text( results[i][0], nameBoxX, nameBoxY + incrY + 75)
            text (results[i][1], scoreBoxX, scoreBoxY + incrY + 75)
            incrY += 110
        incrY = 0
        ryuCombo = 0
        kenCombo = 0
        ryuMaxCombo = 0
        kenMaxCombo = 0
        
        textSize(30)
        text ( "Return to the Main Menu" , 550 , 925) 
        rect( 400, 850, 722, 100) 
    
        
        upperLeft =  [ 400, 850 ]
        lowerRight = [ 1122 , 950]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        
        activeMenuItems = [ True for i in range( 1 ) ]
        
        if 400 <= mouseX <= 1122 and 850 <= mouseY <= 950:
            allBoundaries = []
            background(main)
            textSize(40)
            text( "Scores" , screenWidth/2 - 100, 200)
            noFill()
            textSize(30)
        
            for i in range(numScoresItems):
                rect( nameBoxX, nameBoxY + incrY, scoreBoxWidth, scoreBoxHeight)
                rect( scoreBoxX, scoreBoxY + incrY, scoreBoxWidth, scoreBoxHeight)
                text( results[i][0], nameBoxX, nameBoxY + incrY + 75)
                text (results[i][1], scoreBoxX, scoreBoxY + incrY + 75)
                incrY += 110
            incrY = 0
        
        
            textSize(35)
            text ( "Return to the Main Menu" , 550 , 925) 
            rect( 400, 850, 722, 100) 
    
        
            upperLeft =  [ 400, 850 ]
            lowerRight = [ 1122 , 950]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
    
    if mode == "enter_name":
        allBoundaries = []
        background(main)
        textFont(f)
        textSize(75)
        text("Enter Names", screenWidth/2 - 250, 200)
        textSize(30)
        text("Click box to type name", screenWidth/2 - 185, 500)
        text("Press enter to confirm", screenWidth/2 - 185, 550)
    
        upperLeft =  [ 100, 658 ]
        lowerRight = [ 600 , 758]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        
        upperLeft =  [ 900, 658 ]
        lowerRight = [ 1400 , 758]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        
        upperLeft =  [ 500, 850 ]
        lowerRight = [ 1000 , 950]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
    

        activeMenuItems = [ True for i in range( numMenu2Items ) ]
       
        noFill()
        rect( 100, 658, 500, 100)
        rect ( 900 , 658, 500, 100)
        rect ( 500, 850, 500, 100)
        
        textSize(60)
        text(string, 150, 720)
        text(string2, 950, 720)
        text("Begin", 670, 920)
        if 500 <= mouseX <= 1000 and 850 <= mouseY <= 950:
            allBoundaries = []
            background(main)
            textFont(f)
            textSize(75)
            text("Enter Names", screenWidth/2 - 250, 200)
            textSize(30)
            text("Click box to type name", screenWidth/2 - 185, 500)
            text("Press enter to confirm", screenWidth/2 - 185, 550)
    
            upperLeft =  [ 100, 658 ]
            lowerRight = [ 600 , 758]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
            
            upperLeft =  [ 900, 658 ]
            lowerRight = [ 1400 , 758]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
        
            upperLeft =  [ 500, 850 ]
            lowerRight = [ 1000 , 950]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
    

            activeMenuItems = [ True for i in range( numMenu2Items ) ]
        
            noFill()
            rect( 100, 658, 500, 100)
            rect ( 900 , 658, 500, 100)
            rect ( 500, 850, 500, 100)
        
            textSize(60)
            text(string, 150, 720)
            text(string2, 950, 720)
            textSize(70)
            text("Begin", 670, 920)
    
        
    if mode == "help":
        allBoundaries = []
        textFont(f)
        background(main)
        textSize(60)
        text ( "Player 1", 200, 250)
        text ("Player 2 " , 1000, 250)
        #Instructions for Player 1
        textSize (25)
        text ("Moving Back reflects all attacks except ranged attacks", 400,700)
        text ("Crouching only reduces the damage from ranged attacks", 400, 750)
        text ("WASD movement" , 200, 350)
        text ("F -> Punch" , 200 , 450)
        text ("G -> Kick" , 200, 550)
        text ("H -> Ranged" , 200, 650)
        
        #Instruction for Player 2
        text (" IJKL movement" , 1000, 350)
        text ("1 -> Punch" , 1000 , 450)
        text ("2 -> Kick" , 1000, 550)
        text ("3 -> Ranged" , 1000, 650)
        
        noFill()
        #return to the main menu button
        rect( 600, 800, 722, 150) 
        text ( "Return to the Main Menu" , 768 , 900) 
        #play Button
        rect (150 , 800 , 200, 150)
        text ("Play" , 200, 900)
        
        
        upperLeft =  [ 600, 800 ]
        lowerRight = [ 1322, 950 ]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        
        upperLeft = [150, 800]
        lowerRight = [350, 950]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        activeMenuItems = [ True for i in range( numHelpItems ) ]
        
        if 600 <= mouseX <= 1322 and 800 <= mouseY <= 950:
            allBoundaries = []
            background(main)
            textSize(60)
            text ( "Player 1", 200, 250)
            text ("Player 2 " , 1000, 250)
            #Instructions for Player 1
            textSize (25)
            text ("Moving Back reflects all attacks except ranged attacks", 400,700)
            text ("Crouching only reduces the damage from ranged attacks", 400, 750)
            text ("WASD movement" , 200, 350)
            text ("F -> Punch" , 200 , 450)
            text ("G -> Kick" , 200, 550)
            text ("H -> Ranged" , 200, 650)
            
            #Instruction for Player 2
            text (" IJKL movement" , 1000, 350)
            text ("1 -> Punch" , 1000 , 450)
            text ("2 -> Kick" , 1000, 550)
            text ("3 -> Ranged" , 1000, 650)
            
            noFill()
            #return to the main menu button
            #play Button
            rect (150 , 800 , 200, 150)
            text ("Play" , 200, 900)
            rect( 600, 800, 722, 150) 
            textSize(35)
            text ( "Return to the Main Menu" , 768 , 900) 
            
            upperLeft =  [ 600, 800 ]
            lowerRight = [ 1322, 950 ]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
        
            upperLeft = [150, 800]
            lowerRight = [350, 950]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
            activeMenuItems = [ True for i in range( numHelpItems ) ]
            
        if 150 <= mouseX <= 350 and 800 <= mouseY <= 950:
            allBoundaries = []
            background(main)
            textSize(60)
            text ( "Player 1", 200, 250)
            text ("Player 2 " , 1000, 250)
            #Instructions for Player 1
            textSize (25)
            text ("Moving Back reflects all attacks except ranged attacks", 400,700)
            text ("Crouching only reduces the damage from ranged attacks", 400, 750)
            text ("WASD movement" , 200, 350)
            text ("F -> Punch" , 200 , 450)
            text ("G -> Kick" , 200, 550)
            text ("H -> Ranged" , 200, 650)
            
            #Instruction for Player 2
            text (" IJKL movement" , 1000, 350)
            text ("1 -> Punch" , 1000 , 450)
            text ("2 -> Kick" , 1000, 550)
            text ("3 -> Ranged" , 1000, 650)
        
            noFill()
            #return to the main menu button
            rect( 600, 800, 722, 150) 
            text ( "Return to the Main Menu" , 768 , 900) 
            #play Button
            textSize(40)
            rect (150 , 800 , 200, 150)
            text ("Play" , 200, 900)
            
        
            upperLeft =  [ 600, 800 ]
            lowerRight = [ 1322, 950 ]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
        
            upperLeft = [150, 800]
            lowerRight = [350, 950]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
            activeMenuItems = [ True for i in range( numHelpItems ) ]
            
    
    if mode == "menu":
        allBoundaries = []
        textFont(f)
        background(main)
        mainMenuSound.play()
        for i in range( numMenuItems ):
            upperLeft =  [ menuBarX, menuBarY ]
            lowerRight = [ menuBarX + menuWidth , menuBarY + menuHeight]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
            menuBarY += menuHeight
            menuBarX += 100

        activeMenuItems = [ True for i in range( numMenuItems ) ]
        menuBarX = startMenuX
        menuBarY = startMenuY
        
        for i in range( numMenuItems ):
            noFill()
            rect( menuBarX, menuBarY, menuWidth, menuHeight )
            menuWidth += 100
            menuBarY = menuBarY + menuHeight
        menuBarX = startMenuX
        menuBarY = startMenuY
        menuWidth = startMenuWidth
        
   
        textSize(60)
        text("Play", playTextX, playTextY)
        text("Help", menuBarX + 200, menuBarY + 300 )
        text ("Score", menuBarX + 300, menuBarY + 500 )
        text("Street Fighter", 1000, 200)
        if menuBarX <= mouseX <=  menuBarX + menuWidth and menuBarY <= mouseY <=  menuBarY + menuHeight:
            background(main)
            
            for i in range( numMenuItems ):
                noFill()
                rect( menuBarX, menuBarY, menuWidth, menuHeight )
                menuWidth += 100
                menuBarY = menuBarY + menuHeight
            menuBarX = startMenuX
            menuBarY = startMenuY
            menuWidth = startMenuWidth
            
            textSize(75)
            text("Play", playTextX, playTextY)
            textSize(60)
            text("Help", menuBarX + 200, menuBarY + 300 )
            text ("Score", menuBarX + 300, menuBarY + 500 )
            text("Street Fighter", 1000, 200)
            
        if  menuBarX <= mouseX <=  menuBarX + menuWidth + 100 and menuBarY + menuHeight <= mouseY <=  menuBarY +  menuHeight * 2:
            background(main)
            
            for i in range( numMenuItems ):
                noFill()
                rect( menuBarX, menuBarY, menuWidth, menuHeight )
                menuWidth += 100
                menuBarY = menuBarY + menuHeight
            menuBarX = startMenuX
            menuBarY = startMenuY
            menuWidth = startMenuWidth
            
            textSize (75)
            text("Help", menuBarX + 200, menuBarY + 300 )
            textSize (60)
            text("Play", playTextX, playTextY)
            text ("Score", menuBarX + 300, menuBarY + 500 )
            text("Street Fighter", 1000, 200)
            
        if menuBarX <= mouseX <= menuBarX + menuWidth + 200 and menuBarY + menuHeight * 2 <= mouseY <= menuBarY + menuHeight * 3 + 100:
            background(main)
            for i in range( numMenuItems ):
                noFill()
                rect( menuBarX, menuBarY, menuWidth, menuHeight )
                menuWidth += 100
                menuBarY = menuBarY + menuHeight
            menuBarX = startMenuX
            menuBarY = startMenuY
            menuWidth = startMenuWidth
            
            textSize (75)
            text ("Score", menuBarX + 250, menuBarY + 500 )
            textSize (60) 
            text("Help", menuBarX + 200, menuBarY + 300 )
            text("Play", playTextX, playTextY)
            text("Street Fighter", 1000, 200)
           
        
    if mode == "round_over":
        text(win_text, screenWidth/2 - 340, screenHeight/2)
        text("SCORE: " + str(score[0]) + " - " + str(score[1]), screenWidth/2 - 290, screenHeight/2 + 75)
        gameReset()
                    
    if mode == "gameover":
        text(win_text, screenWidth/2 - 400, screenHeight/2)
        text("SCORE: " + str(score[0]) + " - " + str(score[1]), screenWidth/2 - 290, screenHeight/2 + 75)
        gameReset()
        
    if mode == "play":
                
        #Load map as background
        background(arena)
        
        mainMenuSound.pause()
        
        textSize(40)
        text(string, 60, 50)
        text(string2, 950, 50)
        
        #Sudden Death
        suddenDeath()
            
        #Health bar
        checkWinner()  
        
        ryuColor = healthColor("ryu")
        fill(ryuColor[0], ryuColor[1], ryuColor[2])
        rect(50, 75, ryuHealth * 5.5, 25)
        
        kenColor = healthColor("ken")
        fill(kenColor[0], kenColor[1], kenColor[2])
        rect(screenWidth - 600, 75, kenHealth * 5.5, 25)
        
        fill(255, 255, 255)
        textFont(f)
        textSize(75)
        text(str(timer), screenWidth/2 - 60, 115)
        
        #Standing image of Ryu and Ken
        characterPosition("ryu")
        characterPosition("ken")
        imageMode(CENTER)
        image(bar, screenWidth/2 + 25, screenHeight - 94/2, 552, 94)
        imageMode(CORNER)
        
        #Bullet stuff
        bulletStuff()
        
        #Move character
        ryuX = screenBoundaryCheck(ryuX, ryuStandWidth)
        ryuX += speedX
        kenX = screenBoundaryCheck(kenX, kenStandWidth)
        kenX += speedX2
        
        #Make Ryu jump
        characterJump()
                    
        #Move Bullet
        moveBullet()
        
        #Hit detection
        hitDetection()    
        
        text (ryuCombo , 60, 200)
        text (kenCombo , 1400, 200)    
                    
        if shieldOn == True:
            image(shield, ryuX, ryuY, ryuStandWidth, ryuHeight)
            
        if shieldOn2 == True:
            image(shield2, kenX, kenY, kenStandWidth, kenHeight) 
            
        if reset == True:
            if frameCount % 60 == 0:
                reset = False
        
        if reset2 == True:
            if frameCount % 60 == 0:
                reset2 = False
        
def keyPressed():
    global speedX, speedX2, speedY, ryuY, counter, counter2, bulletSpeed, bulletSpeed2, rangedTimer, rangedTimer2, speedY2, keyCheck
    global name, string, player2name, name2, playerName, string2, shieldOn, shieldOn2, reset, reset2
    
   
    if mode == "enter_name":
        if playerName == True:
            if key in validkey:
                name.append(key)
                
            string = "".join(name)
            if key == "\n" or len(string) == 10:
                playerName = False

                
        if player2name == True:
            if key in validkey:
                name2.append(key)
            string2 = "".join(name2)
            if key == "\n" or len(string2) == 10:
                player2name = False
    
    
    #Move character when key is pressed
    if key == "d":
        speedX = 5
        shieldOn = False
          
    if key == "l":
        speedX2 = 5
        shieldOn2 = True
        
    if key == "a":
        speedX = -5
        shieldOn = True
            
    if key == "s":
        keyCheck[8] = True
        shieldOn = False
        
    if key == "j":
        speedX2 = -5
        shieldOn2 = False
        
    if key == "k":
        keyCheck[9] = True
        shieldOn2 = False

    

    #Ryu fighting
    if key == "f":
        keyCheck[0] = True
        shieldOn = False
                
    elif key == "g":
        keyCheck[1] = True
        shieldOn = False
                
    elif rangedTimer == True:
        if key == "h":
            bulletSpeed = 15
            rangedTimer = False
            if mode == "play":
                ryuHaduken.play(0)
            keyCheck[3] = True
            shieldOn = False
            
    if key == "w":
        if reset == False:
            speedY = -10
            keyCheck[2] = True
            shieldOn = False
            reset = True
        
    
    #Ken fighting
    if key == "1":
        keyCheck[4] = True
        shieldOn2 = False
                
    elif key == "2":
        keyCheck[5] = True
        shieldOn2 = False
                            
    elif rangedTimer2 == True:
        if key == "3":
            bulletSpeed2 = -15
            rangedTimer2 = False
            if mode == "play":
                kenHaduken.play(0)
            keyCheck[7] = True
            shieldOn2 = False
            
    if key == "i":
        if reset2 == False:
            speedY2 = -10
            keyCheck[6] = True
            shieldOn2 = False
            reset2 = True
    
def keyReleased():
    global speedX, counter, counter2, speedX2, ranged_block, ranged_block2
    
    counter = 0
    counter2 = 0
    
    #Stop moving character once key is released
    if key == "d":
        speedX = 0
    elif key == "a":
        speedX = 0
        shieldOn = False
    
    elif key == "j":
        speedX2 = 0
    elif key == "l":
        speedX2 = 0
        shieldOn2 = False
        
    elif key == "f":
        keyCheck[0] = False
        
    elif key == "g":
        keyCheck[1] = False
        
    elif key == "w":
        keyCheck[2] = False
    
    elif key == "h":
        keyCheck[3] = False
        
    elif key == "1":
        keyCheck[4] = False
        
    elif key == "2":
        keyCheck[5] = False
    
    elif key == "i":
        keyCheck[6] = False
        
    elif key == "3":
        keyCheck[7] = False
    
    elif key == "s":
        keyCheck[8] = False
    
    elif key == "k":
        keyCheck[9] = False
        
    ranged_block, ranged_block2 = False, False
    
        
# This takes a character's X coordinate and width. If the character goes off screen it puts them back in.
def screenBoundaryCheck(X, Width):
    if X < 0:
        X = 0
    if X > screenWidth - Width:
        X = screenWidth - Width
        
    if X == ryuX:
        if X + ryuStandWidth >= kenX:
            X = kenX - 1 - ryuStandWidth
    
    if X == kenX:
        if X <= ryuX + ryuStandWidth:
            X = ryuX + ryuStandWidth + 1
    return(X)

    
# This takes the controls of the player and the character responds accordingly
def characterPosition(character):
    global showBullet, showBullet2, ranged_block, ranged_block2
    
    if character == "ryu":
        if keyCheck[0] == True:
            image(ryu_punch, ryuX, ryuY, ryuPunchWidth, ryuHeight)
        elif keyCheck[1] == True:
            image(ryu_kick, ryuX, ryuY, ryuKickWidth, ryuHeight)
        elif speedY !=0:
            image(ryu_jump, ryuX, ryuY + 10, ryuJumpWidth, ryuJumpHeight)
        elif keyCheck[3] == True:
            image(ryu_ranged, ryuX, ryuY + 100, ryuRangedWidth, ryuRangedHeight)
            showBullet = True
        elif keyCheck[8] == True:
            image(ryu_crouch, ryuX, ryuY + 140, ryuCrouchWidth, ryuCrouchHeight)
            ranged_block = True
        else:
            image(ryu_stand, ryuX, ryuY, ryuStandWidth, ryuHeight) 
     
    if character == "ken":
        if keyCheck[4] == True:
            image(ken_punch, kenX - 100, kenY, kenPunchWidth, kenHeight)
        elif keyCheck[5] == True:
            image(ken_kick, kenX - 100, kenY, kenKickWidth, kenHeight)
        elif speedY2 !=0:
            image(ken_jump, kenX, kenY + 10, kenJumpWidth, kenJumpHeight)
        elif keyCheck[7] == True:
            image(ken_ranged, kenX - 150, kenY + 100, kenRangedWidth, kenRangedHeight)
            showBullet2 = True
        elif keyCheck[9] == True:
            image(ken_crouch, kenX, kenY + 100, kenCrouchWidth, kenCrouchHeight)
            ranged_block2 = True
        else:
            image(ken_stand, kenX, kenY, kenStandWidth, kenHeight)
            
def hitDetection():
    global kenHealth, ryuHealth, showBullet2, showBullet ,  kenCombo, ryuCombo,  ryuMaxCombo, kenMaxCombo 
    
    if shieldOn2 == False:
        if keyCheck[0] == True:
            ryuPunch.play(0)
            
            if ryuX + ryuPunchWidth >= kenX:
                kenCombo = 0
                kenHealth -= 1
                ryuCombo += 1
                if ryuCombo > ryuMaxCombo:
                    ryuMaxCombo = ryuCombo
        elif keyCheck[1] == True:
             ryuKick.play(0)
        if keyCheck[1] == True:     
            if ryuX + ryuKickWidth >= kenX:
                kenCombo = 0
                kenHealth -= 1
                ryuCombo += 1
                if ryuCombo > ryuMaxCombo:
                    ryuMaxCombo = ryuCombo
        elif (bulletX + bulletWidth >= kenX) and (showBullet == True) and (ranged_block2 == False):
            kenCombo = 0
            showBullet = False
            kenHealth -= 10
            ryuCombo += 1
            if ryuCombo > ryuMaxCombo:
                    ryuMaxCombo = ryuCombo
        elif (bulletX + bulletWidth >= kenX) and (showBullet == True) and (ranged_block2 == True):
            kenCombo = 0
            showBullet = False
            kenHealth -= 3
            ryuCombo += 1
            if ryuCombo > ryuMaxCombo:
                    ryuMaxCombo = ryuCombo
    else:
        if keyCheck[0] == True:
            if ryuX + ryuPunchWidth >= kenX:
                ryuCombo = 0
                ryuHealth -= 1
                kenCombo += 1
                kenMaxCombo = kenCombo
        elif keyCheck[1] == True:
            if ryuX + ryuKickWidth >= kenX:
                ryuCombo = 0
                ryuHealth -= 1
                kenCombo += 1
                if kenCombo > kenMaxCombo:
                    kenMaxCombo = kenCombo
        elif (bulletX + bulletWidth >= kenX) and (showBullet == True) and (ranged_block2 == False):
            kenCombo = 0
            showBullet = False
            kenHealth -= 10
            ryuCombo += 1
            if ryuCombo > ryuMaxCombo:
                    ryuMaxCombo = ryuCombo
        elif (bulletX + bulletWidth >= kenX) and (showBullet == True) and (ranged_block2 == True):
            kenCombo = 0
            showBullet = False
            kenHealth -= 3
            ryuCombo += 1
            if ryuCombo > ryuMaxCombo:
                    ryuMaxCombo = ryuCombo
            
    if shieldOn == False:
        if keyCheck[4] == True:
            kenPunch.play(0)
            if kenX - 100 <= ryuX + ryuStandWidth:
                ryuCombo = 0
                ryuHealth -= 1
                kenCombo += 1
                kenMaxCombo = kenCombo
                
        elif keyCheck[5] == True:
            kenKick.play(0)
            if kenX - 100 <= ryuX + ryuStandWidth:
                ryuCombo = 0
                ryuHealth -= 1
                kenCombo += 1
                if kenCombo > kenMaxCombo:
                    kenMaxCombo = kenCombo
        
        elif (bulletX2 <= ryuX + ryuStandWidth) and (showBullet2 == True) and (ranged_block == False):
            showBullet2 = False
            ryuCombo = 0
            ryuHealth -= 10
            kenCombo += 1
            if kenCombo > kenMaxCombo:
                kenMaxCombo = kenCombo
        elif (bulletX2 <= ryuX + ryuStandWidth) and (showBullet2 == True) and (ranged_block == True):
            showBullet2 = False
            ryuCombo = 0
            ryuHealth -= 3
            kenCombo += 1
            if kenCombo > kenMaxCombo:
                kenMaxCombo = kenCombo
    else:
        if keyCheck[4] == True:
            if kenX - 100 <= ryuX + ryuStandWidth:
                kenCombo = 0
                kenHealth -= 1
                ryuCombo += 1
                if ryuCombo > ryuMaxCombo:
                    ryuMaxCombo = ryuCombo
                
        elif keyCheck[5] == True:
            if kenX - 100 <= ryuX + ryuStandWidth:
                kenCombo = 0
                kenHealth -= 1
                ryuCombo += 1
                if ryuCombo > ryuMaxCombo:
                    ryuMaxCombo = ryuCombo
        
        elif (bulletX2 <= ryuX + ryuStandWidth) and (showBullet2 == True) and (ranged_block == False):
            showBullet2 = False
            ryuCombo = 0
            ryuHealth -= 10
            kenCombo += 1
            if kenCombo > kenMaxCombo:
                kenMaxCombo = kenCombo
            
        elif (bulletX2 <= ryuX + ryuStandWidth) and (showBullet2 == True) and (ranged_block == True):
            showBullet2 = False
            ryuCombo = 0
            ryuHealth -= 3
            kenCombo += 1
            if kenCombo > kenMaxCombo:
                kenMaxCombo = kenCombo
        
def healthColor(character):
    if character == "ryu":
        if 25 < ryuHealth < 50:
            return([244, 229, 66])
        elif 0 <= ryuHealth <= 25:
            return([255, 0, 0])
        else:
            return([0, 255, 0])
        
    if character == "ken":
        if 25 < kenHealth < 50:
            return([244, 229, 66])
        elif 0 <= kenHealth <= 25:
            return([255, 0, 0])
        else:
            return([0, 255, 0])
        
def checkWinner():
    global kenHealth, ryuHealth, mode, win_text, score, timer
    
    if kenHealth <= 0:
        mode = "round_over"
        win_text = string + " Wins Round"
        score[0] += 1
        timer = 60
        kenHealth = 100
        ryuHealth = 100
        
    if ryuHealth <= 0:
        mode = "round_over"
        win_text = string2 + " Wins Round"
        ryuHealth = 100
        kenHealth = 100
        score[1] += 1
        timer = 60
        
    if score[0] == 2:
        win_text = string + " WINS THE GAME"
        mode = "gameover"
    
    elif score[1] == 2:
        win_text = string2 + "  WINS THE GAME"
        mode = "gameover"
                
    
def bulletStuff():
    global showBullet, bulletX, bulletSpeed, rangedTimer, showBullet2, bulletX2, bulletSpeed2, rangedTimer2
    
    if showBullet == True:
        image(bullet, bulletX, bulletY, bulletWidth, bulletHeight)
    if bulletX >= kenX - bulletWidth:
        showBullet = False
        bulletX = ryuX + ryuRangedWidth
        bulletSpeed = 0
        rangedTimer = True
    if bulletSpeed == 0:
        showBullet = False
    if showBullet == False:
        bulletX = ryuX + ryuRangedWidth
        bulletSpeed = 0
        rangedTimer = True        
    if showBullet2 == True:
        image(bullet2, bulletX2, bulletY2, bulletWidth, bulletHeight)
    if bulletX2 <= ryuX + ryuStandWidth:
        showBullet2 = False
        bulletX2 = kenX - kenRangedWidth + 50
        bulletSpeed2 = 0
        rangedTimer2 = True
    if bulletSpeed2 == 0:
        showBullet2 = False
    if showBullet2 == False:
        bulletX2 = kenX - kenRangedWidth + 50
        bulletSpeed2 = 0
        rangedTimer2 = True
        
def characterJump():
    global kenY, ryuY, speedY, speedY2
    
    ryuY += speedY
    kenY += speedY2
        
    if ryuY <= 350:
        speedY = 10    
    elif ryuY > screenHeight - ryuHeight - 30:
        ryuY = screenHeight - ryuHeight - 30
        speedY = 0
    if kenY <= 350:
        speedY2 = 10
    elif kenY > screenHeight - kenHeight - 30:
        kenY = screenHeight - kenHeight - 30
        speedY2 = 0
        
def moveBullet():
    global bulletX, bulletX2
    
    bulletX += bulletSpeed
    bulletX2 += bulletSpeed2

def mouseReleased():
    global allBoundaries, whichMenuItem, removeMenuItem, activeMenuItems, numMenuItems, mode, numHelpItems, playerName, player2name, name, name2
    
#  all Boundaries is a list of tuples,  each tuple is the upper left and lower right of each box
#  if removeMenuItem is True, you will not be able to click again in that square again as that place in activeMenuItems will be turned to False
    
    
    if mode == "menu":
        whichMenuItem = - 1
        validLocation = False
        for i in range( numMenuItems ):        
            if activeMenuItems[ i ]:
                validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
                validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
                validLocation = validXRange and validYRange
                if validLocation:
                    whichMenuItem = i
                    break
        if validLocation and removeMenuItem:
            activeMenuItems[ whichMenuItem ] = False
            
        if whichMenuItem == 0:
            mode = "enter_name"
            
        elif whichMenuItem == 1:
            mode = "help"
        
        elif whichMenuItem == 2:
            mode = "scores"
            
    if mode == "enter_name":
        whichMenuItem = - 1
        validLocation = False
        for i in range( numMenu2Items ):        
            if activeMenuItems[ i ]:
                validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
                validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
                validLocation = validXRange and validYRange
                if validLocation:
                    whichMenuItem = i
                    break
        if validLocation and removeMenuItem:
            activeMenuItems[ whichMenuItem ] = False
            
        if whichMenuItem == 0:
            playerName = True
            player2name = False
            name = []
        elif whichMenuItem == 1:
            player2name = True
            playerName = False
            name2 = []
        elif (whichMenuItem == 2) and (string != "") and (string2 != ""):
            mode = "play"
            
    if mode == "scores":
        whichMenuItem = - 1
        validLocation = False
        validXRange = allBoundaries[0][0][0] <= mouseX <= allBoundaries[0][1][0] 
        validYRange = allBoundaries[0][0][1]  <= mouseY <= allBoundaries[0][1][1]
        validLocation = validXRange and validYRange
        if validLocation:
            whichMenuItem = 0
        
        if validLocation and removeMenuItem:
            activeMenuItems[ whichMenuItem ] = False
            
        if whichMenuItem == 0:
            mode = "menu"
    
        
    if mode == "help":    
        whichMenuItem = - 1
        validLocation = False
        for i in range( numHelpItems):        
            if activeMenuItems[ i ]:
                validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
                validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
                validLocation = validXRange and validYRange
                if validLocation:
                    whichMenuItem = i
                    break
        if validLocation and removeMenuItem:
            activeMenuItems[ whichMenuItem ] = False
            
        if whichMenuItem == 0:
            mode = "menu"
            
        elif whichMenuItem == 1:
            mode = "enter_name"
  
            
def gameReset():
    global mode, ryuX, kenX, ryuCombo, kenCombo, score, ryuMaxCombo, kenMaxCombo
    if mode == "round_over":
        if frameCount % 360 == 0:
            mode = "play"
            ryuX = 100
            kenX = screenWidth - kenStandWidth - 90
            ryuCombo = 0
            kenCombo = 0
    elif mode == "gameover":
        if frameCount % 360 == 0:
            mode = "menu"
            ryuX = 100
            kenX = screenWidth - kenStandWidth - 90
            score = [0, 0]
            results = outputScores()
            gameResults = [string, ryuMaxCombo]
            results.append(gameResults)
            gameResults = [string2, kenMaxCombo]
            results.append(gameResults)
            results = sortingScores(results)
            inputScores(results)
            ryuCombo = 0
            kenCombo = 0
            ryuMaxCombo = 0
            kenMaxCombo = 0
            
def suddenDeath():
    global timer, ryuHealth, kenHealth
    if frameCount % 60 == 0:
        timer -= 1
        
    if timer == 0:
        ryuHealth = 1
        kenHealth = 1
        
    if timer <= 0:
        textSize(80)
        text("SUDDEN DEATH", screenWidth/2 - 340, screenHeight/2 - 150)
        
