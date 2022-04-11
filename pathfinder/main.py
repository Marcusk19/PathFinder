import HUD
import OBD

def main():
    obd = OBD.Obd()
    obd.start()
    hud = HUD.Hud()
    hud.start()

if __name__ == "__main__":
    main()