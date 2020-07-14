from Code.AVIMMEL.Architect.InterfacesAndStructs.Structs import Data
from Analisys.Devices.MFD.MFD382.Calculation.AnlzSpeedLimits import AnlzSpeedLimits

ASL = AnlzSpeedLimits(m_hel=Data(value=13200))
ASL.buildplot(hight_max=6300, temprMove=0)
