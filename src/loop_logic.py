

from image_recognition import compare_images, get_text_from_screenshot
from auto_move import move_mouse, press_keys, idle_game

def start(config):
        print(config.debug)
        print("Pressing key: ",config.key_1)
        press_keys(config.key_1,config.hold_time)
        print("Pressing key: ", config.key_2)
        press_keys(config.key_2,config.hold_time)

        print("Chekcing if we are in battle...")
        in_battle = get_text_from_screenshot(config.text_coords, config.debug)

        if in_battle == True:

            print("We are in battle. Looking for pokemon match on screen.")
            pokemon_found = compare_images(config.img_dir,config.threshold, config.img_scale_percent, config.debug)
            if pokemon_found == False:
                print("Pokemon match not found, moving mouse to flee...")
                move_mouse(config.target_coordinates)
            else:
                print("Pokemon match found! Idling game...")
                idle_game()
        else:
            print("Either not in battle, or currently entering battle...")

