from Code.AVIMMEL.Architect.InterfacesAndStructs.Structs import Borders
from Code.Devices.Common.Bright import Bright

ExmBright = Bright(angle=Borders(min=0, max=100),
                   bright=Borders(min=0.5, max=540),
                   dotsInDayTime={"Day": 4, "Night": 5},
                   switchBright=6)
ExmBright.showTable()
