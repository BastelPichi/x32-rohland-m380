# x32-rohland-m380
One way sync from X32-Emulator to Rohland M380 Midi. Allows using Mixing Station from your phone to control the Rohland Mixer.

## Only Mute and Faders implemented! Only changes from phone to Mixer, changes from Mixer to Phone are not synced.

## Setup Instructions:
1) Download the [X32-Emulator](https://sites.google.com/site/patrickmaillot/x32#h.p_rE4IH0Luimc0). Put the .exe in the same directory as the .py file.
2) On the mixer:
   System -> Remote (F4) -> Usb Midi (F2) -> Select Fader and Mute Change for receive and send, select DEV_ID 17.
3) Double click the .py file.
4) The Program will print all available MIDI devices. If theres an error, copy the correct name from the list and put it in line 43 of main.py.

## Tested with:
- Roland M380, FW Version 1.321
- X32 Emulator from 8.1.2024
- Mixing Station on Android and ios, X32-Edit on PC. X32-Mix on ios does not properly work!

### Disclaimer
This is a very quick and dirty project. Dont use it in production, its not reliable (by design).
