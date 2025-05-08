import os
import platform

bit = platform.architecture()[0]

if bit == '64bit':
    binary = 'marina'
elif bit == '32bit':
    binary = 'marina32'
else:
    print('Device not supported')
    sys.exit(1)

if os.path.isfile(binary):
    os.system(f'chmod +x {binary}')
    os.system(f'./{binary}')
else:
    print(f'{binary} not found in the current directory')
    
