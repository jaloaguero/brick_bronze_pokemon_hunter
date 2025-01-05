from config_handler import get_info_from_config, get_file_name_w_directory, change_resolution

#TODO: create a "try" "catch" so in case user fucks up config file it still has some basic stuff there

class ConfigManager:
    def __init__(self):
        self.img_scale_percent = 400
        tmp = change_resolution()
        self.target_coordinates = tmp[0]
        self.text_coords = tmp[1]
        self.hold_time = int(get_info_from_config('config.txt', "hold_time"))
        self.key_1 = get_info_from_config('config.txt', "key_1")
        self.key_2 = get_info_from_config('config.txt', "key_2")
        self.countdown_time = int(get_info_from_config('config.txt', "countdown_time"))
        self.debug = get_info_from_config('config.txt', "debug")
        self.threshold = float(get_info_from_config('config.txt', "threshold"))
        self.folder_path = get_info_from_config('config.txt', "folder_path")
        self.img_dir = get_file_name_w_directory(self.folder_path)

# Function to create and return the ConfigManager instance
def init_config():
    print("Creating configManager...")
    return ConfigManager()