from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
from decode import masterVolume, pot1, pot2, pot3, pot4

if __name__ == "__main__":
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    while True:
        volume.SetMasterVolumeLevel(masterVolume(), None)
        sessions = AudioUtilities.GetAllSessions()
        for sessions in sessions:
            TIDALvolume = sessions._ctl.QueryInterface(ISimpleAudioVolume)
            if sessions.Process and sessions.Process.name() == "TIDAL.exe":
                TIDALvolume.SetMasterVolume(pot1(), None)