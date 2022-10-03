from classes.Unichar import Unichar
from colorama import Fore, init; init()

try:

    #### Try the class Unichar here! #### █
    u = Unichar("a")
    print(u.get_size2())
    #####################################

except Exception as e:
    print(f"{Fore.RED}Error: {e}{Fore.RESET}")