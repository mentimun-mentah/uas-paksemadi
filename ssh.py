from subprocess import PIPE, Popen

cmd = 'uname -a'
stream = Popen(['ssh', 'nyoman@192.168.18.48', cmd],stdin=PIPE, stdout=PIPE)

rsp = stream.stdout.read().decode('utf-8')
print(rsp)
