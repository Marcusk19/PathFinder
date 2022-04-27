pathfinder
==========
These are the underlying modules for the PathFinder. Each one has a specific role to perform and most are tied together under
our two large "main" modules: OBD.py and HUD.py. A python file main.py is used as an entrypoint for the program and each main
module takes their own respective thread to run concurrently.

.. code-block:: python

   # an instance of OBD and HUD declared and ran
   def main():
      screen = display.Display()
      obd = OBD.Obd(screen)
      hud = HUD.Hud(screen)
      hud.start()
      obd.start()

.. toctree::
   :maxdepth: 4

   pathfinder
