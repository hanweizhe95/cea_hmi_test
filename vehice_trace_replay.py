import pyshark
import socket
import time

recording_trace_path = r"./output_data.pcap"
trace_file = pyshark.FileCapture(recording_trace_path)

blist = []
trace_file = list(trace_file)
for i in range(len(trace_file)):
    a = trace_file[i]
    b = a.TCP.payload.binary_value
    blist.append(b)
    # print(b)
    # print(len(b))
    #
    # print(b[len(b)-60])

print(len(blist))
print(type(blist))
print(blist)

# payload_str = []
# payload_byte = list()
# trace_file = list(trace_file)
# for i in range(len(trace_file)):
#     payload_str = trace_file[i].TCP.payload.raw_value
#     print(payload_str[0:100])
#     print("-----------------------------------------------------------------------")
#     for j in range(0, len(payload_str), 2):
#         payload_byte.append(int(payload_str[j:j + 2], 16))
#     print(len(payload_byte))
#
# payload_byte = bytearray(payload_byte)
#
# blist = list()
#
# blist.append(payload_byte)

# print(blist)
