					THIS HAS A LOT OF IMPORTANT INFO PLEASE READ


################################################### HOW TO USE ###################################################

Click on Pokemon Brick Bronze Auto Player.exe. A CMD command prompt will open up. It has text with more information,
that I suggest you read, but if you don't want to do that, just press Enter a bunch and it will just start. 

You close the program by closing the CMD command prompt. There are large gaps to do it in, but having a kill switch
seems to trigger something aobut Windows Defender, so you just have to move your mouse to close it. Your mouse might
move on its own (due to the program doing something), but it only does that once every 10 seconds at most.

Please put only 1 .gif or .webp in the image_folder (I put a Pikachu .webp in there just so the program actually 
has something to do, please replace this with a .gif or .webp of your choice).

I ask for a .gif or a .webp from the sites below, as opposed to .pngs or .jpgs because if my program takes a 
screenshot at the wrong time, it may miss the Pokemon completely. 

############################################# WHERE TO GET SPRITES #################################################

The Sprites tested and optimized for I got from:

	Here: https://play.pokemonshowdown.com/sprites/xyani/

	Here (for the Shiny Sprites): https://play.pokemonshowdown.com/sprites/xyani-shiny/

	Here: https://brickbronze.fandom.com/wiki/Route_1

	And here: https://brickbronze.fandom.com/wiki/Gale_Forest

(I did not get far in the game to test more than route 1 and Gale Forest, but I tested a lot of the Pokemon there 
to make sure that the program worked as expected.)

I downloaded these sprites in the brickbronze website by literally going to the website I wanted, and right 
clicking on the sprite, and clicking "save as" to save it. You don't need to do anything else to these files
but put them in the image_folder folder, my program automatically scales them up.

For the play.showdown website, I just pressed CNTRL + F, typed in the Pokemon I was looking for, and when it took
me to the pokemon I was looking for, I clicked the link. It opened a new page that had a .gif of the Pokemon I was
looking for, and I right clicked it to save, same as last time. 

The Pokemon Brick Bronze website seems to have more accurate models and I suggest using those whenever possible,
but the Sprites from the pokemon showdown website are also good enough, and I made the program work for both. 

################################################# HOW IT WORKS #####################################################

This program presses 'W' for 2 Seconds, 'S' for 2 seconds, then checks if it is in battle.

It does this by checking if there is the word "Lv." in a specific part of the screen.

If that is there, it then takes a screenshot (not saved in your computer, just saves it temporarily),
and checks every frame of a .gif or a .webp image given to it. 
This usually takes 5-20 seconds depending on how many frames there are and wether
 its a .gif or a .webp (.gifs take a little longer). 

The reason we do this is because when we take the "screenshot" the Pokemon on screen is moving, and some move so
dramatically we might get unlucky and confuse the computer. 

So we check every frame to make sure we do not miss anything.

If it does not find anything, it moves the mouse to the "flee" location in the program. It double clicks it, and 
loops again to the pressing of 'W' and 'S'

If the program does find something, it enters an 'idle' session where it just clicks on 2 seperate places on the
screen. It does this forever, until you turn it off. This is to prevent the game (if you leave it on and leave 
to go do something) from disconnecting due to inactivity (something that happened to me a lot while testing). 


There are occasional false positives, however thse happen very rarely, and I quite honestly have no clue why they
happen only seemingly once every 50 tries. I biased for false positives as opposed to false negatives, because
I did not want the user to miss anything, as opposed to potentially missing the Pokemon they are looking for. 

In the src folder are the Python files I used to create this. If you want, you are more than welcome to look
through them, in case you don't feel comfortable clicking on random .exes people send you, as the exe is just
those Python file's logic. They aren't needed for anything though, you can delete those if you want, but the
image_folder is very important, and must always be in the same folder the .exe file is in.

IF there is anything that does not work as expected, you want a tweak, or anything else, please do not hesitate to
reach out. I tested it all I could, but there could always be something unexpected happening, and I am more than
happy to make adjustments where needed. 