txt = open("../../main.py", "r").read()
print(txt)
x = open("../../main.py", "w")
x.write(txt.replace("""if isMidi:
    i = 0
    done = False
    midiPorts = []
    try:
        x = rtmidi.MidiIn(0)
    except:
        pass
    x = rtmidi.MidiIn(0)
    while not done:
        try:
            midiPorts.append(x.get_port_name(i))
            i += 1
        except:
            done = True
    done = False
    if len(midiPorts) > 1:
        while not done:
            midiPort = int(input(f"Choose a midi port from this list. Give the index:\n{midiPorts}"))
            if 0 <= midiPort < len(midiPorts):
                done = True
            else:
                print("Invalid port")
    elif len(midiPorts) == 1:
        midiPort = 0
    else:
        print("MIDI is unavailable, please plug a controller in or create a virtual input.")
        isMidi = False
    if isMidi:
        midiIn = mido.open_input(midiPorts[midiPort])""", """if isMidi:
    import requests
    midiAddress = input("Input local ip of server in server.py")
    class midiIn:
        class message:
            def __init__(self, type):
                self.type=type
        def poll():
            x = requests.get(midiAddress + "/midi/")
            return midiIn(x.text)
            """))
x.close()
print("NuclearGraphics has been fixed. Run main.py in this directory and visit the right IP address to gain access. I'm not sure what that'll be but it's probably 127.0.0.1:5000. It can be very inconsistent, unfortunately.")
