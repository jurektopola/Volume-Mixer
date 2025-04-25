from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
from decode import masterVolume, pot1, pot2, pot3, pot4
from apps import apps1, apps2, apps3, apps4
'''
This file is controlling different applications volume with potentiometers.
DO NOT CHANGE APPLICATIONS CONTROL IN THIS FILE!!! instead go to 'apps.py'
'''

if __name__ == "__main__":
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

while True:
    volume.SetMasterVolumeLevel(masterVolume(), None)

    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process:
            app_name = session.Process.name()
            app_volume = session._ctl.QueryInterface(ISimpleAudioVolume)

            if app_name in apps1:
                app_volume.SetMasterVolume(pot1(), None)
            elif app_name in apps2:
                app_volume.SetMasterVolume(pot2(), None)
            elif app_name in apps3:
                app_volume.SetMasterVolume(pot3(), None)
            elif app_name in apps4:
                app_volume.SetMasterVolume(pot4(), None)