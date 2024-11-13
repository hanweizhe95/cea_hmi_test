import pyshark
import socket
import time
import sys
import json

from google.protobuf import json_format  # protobuf==4.25.1  
sys.path.append('./proto_ap')  
  
import WM_display_realtime_pb2

recording_trace_path = r"./Logging018.pcapng"
trace_file = pyshark.FileCapture(recording_trace_path, display_filter="someip.serviceid == 0x4010")
print(trace_file)

# trace_file = list(trace_file)

blist = []
with open("output.json", "w") as f:  
    for packet in trace_file:
        try:
            # 直接获取 SOME/IP 有效负载的二进制数据
            payload_data = packet.someip.payload.binary_value
            blist.append(payload_data)
            # 使用 pb2 反序列化
            msg = WM_display_realtime_pb2.ApDrivingData()
            msg.ParseFromString(payload_data)

            # 转换为 JSON 并输出
            f.write(json_format.MessageToJson(msg, indent=None) + "\n")  

        except AttributeError:
            continue  # 如果没有 payload，跳过
        except Exception as e:
            print(f"Error parsing packet: {e}")

with open("output.json","r") as json_file:
    content = json_file.read().splitlines()
    json_objects = [json.loads(line) for line in content]

with open("output.json","w") as json_file:
    json.dump(json_objects, json_file, indent = 4)

print("已将文件格式化")