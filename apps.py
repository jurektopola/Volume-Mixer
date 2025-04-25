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
list of applications controlled by potentiometers, change it by typing different session name to list
If there is more than one session name in list, the potentiometer will control all of them
'''

apps1 = ['Discord.exe']
apps2 = ['TIDALPlayer.exe']
apps3 = ['chrome.exe']
apps4 = ['Cities.exe', 'FactoryGameSteam-Win64-Shipping.exe', 'ScrapMechanic.exe', 'valheim.exe', 'DyingLightGame.exe', 'TheForest.exe', 'witcher3.exe', 'eurotrucks2.exe', 'cs2.exe', 'javaw.exe']