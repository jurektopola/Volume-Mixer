from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
from read import getValue

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#current = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(0, None)

while True:
    sessions = AudioUtilities.GetAllSessions()
    for sessions in sessions:
        TIDALvolume = sessions._ctl.QueryInterface(ISimpleAudioVolume)
        if sessions.Process and sessions.Process.name() == "TIDALPlayer.exe":
            TIDALvolume.źSetMasterVolume(getValue(), None)