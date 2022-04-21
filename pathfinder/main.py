import HUD
import OBD
import display

def main():
    screen = display.Display()
    obd = OBD.Obd(screen)
    obd.start()
    hud = HUD.Hud(screen)
    hud.start()

if __name__ == "__main__":
    main()
