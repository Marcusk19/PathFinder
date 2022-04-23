import HUD
import OBD
import display

def main():
    screen = display.Display()
    obd = OBD.Obd(screen)
    hud = HUD.Hud(screen)
    hud.start()
    obd.start()


if __name__ == "__main__":
    main()
