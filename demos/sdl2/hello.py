import sys
import sdl2.ext

def run():
    sdl2.ext.init()
    win = sdl2.ext.Window("Hello", size=(400, 300))
    win.show()

    processor = sdl2.ext.TestEventProcessor()
    processor.run(win)
    sdl2.ext.quit()
    return 0

if __name__ == "__main__":
    run()
