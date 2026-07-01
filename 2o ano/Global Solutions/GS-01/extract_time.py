import struct
import datetime

with open('file.0x16b7998.0x818144d8.DataSectionObject.ThinPrint.evt-1.dat', 'rb') as f:
    fd = f.read()

for i in range(0, len(fd)-4, 4):
    try:
        b_stamp = fd[i:i+4]
        unix_time = struct.unpack('<I', b_stamp)[0]
                                           
        if 155000000 <= unix_time <= 1735689600:
            dt = datetime.datetime.fromtimestamp(unix_time)
            print(f'Addr {hex(i)}: {dt.strftime("%d/%m/%Y_%H:%M:%S")}')
    except:
        pass
