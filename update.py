import sys
import os
def restart():
    os.system('pip install -U discord.py[voice] pynacl youtube-dl --upgrade')
    os.execv(sys.executable, ['python'] + sys.argv)
restart()
