import time
import mido
import subprocess
from threading import Thread


def map_(value, minin, maxin, minout, maxout):
    return minout + (value - minin) * (maxout - minout) / (maxin - minin)

def send_changes():
    while True:
        for i in range(len(l)):
            if l[i] != last[i]:
                v = l[i]
                last[i] = v

                v = int(map_(v, 0, 1, 0, 127))
                print("Write", i, v)
                out.send(mido.Message('control_change', channel=0, control=i, value=v))

        for i in range(len(m)):
            if m[i] != mlast[i]:
                v = m[i]
                mlast[i] = v

                v = 0 if v else 1
                print("Mute", i, v)
                
                out.send(mido.Message('control_change', channel=0, control=0x40-1+i, value=v))
        time.sleep(0.01)


if __name__ == "__main__":
    l=[0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # fader values
    last = l.copy()
    m=[False, False, False, False, False, False, False, False, False, False, False, False] # I only need 12 mute buttons. Expand this list to support more.
    mlast = m.copy()
    command = ['x32.exe']

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(mido.get_output_names())

    out = mido.open_output('2- RSS M-400 1') # This might be slightly different for you.

    thread = Thread(target = send_changes)
    thread.start()

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            a = output.strip()

            if a.startswith("->X"):
                if ("/ch/" in a) and ("/mix/fader" in a):
                    try:
                        b = a.split("/ch/")[1].split("/")[0]
                        channel = int(b)
                        value = float(a.split("[")[1].split("]")[0])
                        l[channel] = value
                    except:
                        print("Error")
                if ("/ch/" in a) and ("/mix/on" in a):
                    try:
                        b = a.split("/ch/")[1].split("/")[0]
                        channel = int(b)
                        value = int(a.split("[")[1].split("]")[0])
                        if value: value = True
                        else: value = False
                    
                        m[channel] = value
                    except:
                        print("Error")
                    

    stderr_output = process.stderr.read()
    if stderr_output:
        print(f"Error: {stderr_output}")
