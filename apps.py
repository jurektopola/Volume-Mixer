from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
'''
In this file you select applications for corresponding potentiometers
Run file to see sessions from active sound applications, then manually type session name to array for selected potentiometer
'''
sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    if session.Process:
        print(session.Process.name())

'''
POTENTIOMETER 0 CONTROLS MASTER VOLUME

Below are lists of applications controlled by potentiometers, type different process names to change applications
If there is more than one session name in list, the potentiometer will control all of them
Each list is controlled by one potentiometer, for example 'apps1' is controlled by potentiometer 1
'''

apps1 = ['Discord.exe']
apps2 = ['TIDALPlayer.exe']
apps3 = ['chrome.exe']
apps4 = ['Cities.exe', 'FactoryGameSteam-Win64-Shipping.exe', 'ScrapMechanic.exe', 'valheim.exe', 'DyingLightGame.exe', 'TheForest.exe', 'witcher3.exe', 'eurotrucks2.exe', 'cs2.exe', 'javaw.exe']