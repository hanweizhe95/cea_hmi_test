import pyshark
import json

from google.protobuf import json_format  # protobuf==4.25.1    

def pcapToJson(pcapFile, serviceID, methoID, jsonFile, message):
    trace_file = pyshark.FileCapture(pcapFile, display_filter=f'someip.serviceid == {serviceID} && someip.methodid == {methoID}')
    with open(jsonFile, "w") as f:  
        for packet in trace_file:
            try:
                # 直接获取 SOME/IP 有效负载的二进制数据
                payload_data = packet.someip.payload.binary_value
                # 使用 pb2 反序列化
                message.ParseFromString(payload_data)
                # 转换为 JSON 并输出
                f.write(json_format.MessageToJson(message, indent=None) + "\n")  
            except AttributeError:
                continue  # 如果没有 payload，跳过
            except Exception as e:
                print(f"Error parsing packet: {e}")

    with open(jsonFile,"r") as json_file:
        content = json_file.read().splitlines()
        json_objects = [json.loads(line) for line in content]

    with open(jsonFile,"w") as json_file:
        json.dump(json_objects, json_file, indent = 4)

    print("已将文件格式化")

def pcapToJsonOneFrame(pcapFile, serviceID, methoID, jsonFile, message, frame = 0):
    trace_file = pyshark.FileCapture(pcapFile, display_filter=f'someip.serviceid == {serviceID} && someip.methodid == {methoID}')
    with open(jsonFile, "w") as f:  
        # 直接获取 SOME/IP 有效负载的二进制数据
        payload_data = trace_file[frame].someip.payload.binary_value
        # 使用 pb2 反序列化
        message.ParseFromString(payload_data)
        # 转换为 JSON 并输出
        f.write(json_format.MessageToJson(message, indent=None) + "\n")  

    with open(jsonFile,"r") as json_file:
        content = json_file.read().splitlines()
        json_objects = [json.loads(line) for line in content]

    with open(jsonFile,"w") as json_file:
        json.dump(json_objects, json_file, indent = 4)

    print("已将第",frame,"帧数据格式化")

