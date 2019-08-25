import os
import subprocess
import emoji
cmd = 'git --version'
ret = subprocess.call(cmd, shell=True)
print(type(ret))

print(emoji.emojize(':grinning_face_with_big_eyes:'))