import subprocess
import os

def gui_start():
    os.chdir("../gui")
    subprocess.run(["python", "gui_main.py"])


def main():
    gui_start()
    
    return 0

if __name__ == "__main__":
    main()