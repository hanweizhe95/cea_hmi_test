import pyshark
import json

from google.protobuf import json_format  # protobuf==4.25.1    

def pcapToJsonWholeFile(pcapFile, serviceID, methodID, jsonFile, message):
    print(f"Converting {pcapFile}... \nService id: {hex(serviceID)} \nMethod id: {hex(methodID)} ")
    trace_file = pyshark.FileCapture(pcapFile, display_filter=f'someip.serviceid == {serviceID} && someip.methodid == {methodID}')
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
        trace_file.close()

    with open(jsonFile,"r") as json_file:
        content = json_file.read().splitlines()
        json_objects = [json.loads(line) for line in content]

    with open(jsonFile,"w") as json_file:
        json.dump(json_objects, json_file, indent = 4)

    print("已将文件格式化\n")

def pcapToJsonOneFrame(pcapFile, serviceID, methodID, jsonFile, message, frame = 0):
    print(f"Converting {pcapFile}... \nService id: {hex(serviceID)} \nMethod id: {hex(methodID)} ")
    trace_file = pyshark.FileCapture(pcapFile, display_filter=f'someip.serviceid == {serviceID} && someip.methodid == {methodID}')
    
    # 直接获取 SOME/IP 有效负载的二进制数据
    frame_count = sum(1 for _ in trace_file)
    print("Length of trace file:",frame_count)
    if frame_count == 0:
        print("No valid frame in the trace file.\n")

    elif frame < 0:
        print("Invalid frame number input!\n")

    elif frame >= frame_count:
        print("Please choose a frame number within trace file frame size.\n")

    else:
        payload_data = trace_file[frame].someip.payload.binary_value
        # 使用 pb2 反序列化
        message.ParseFromString(payload_data)
        # 转换为 JSON 并输出
        with open(jsonFile, "w") as f:
            f.write(json_format.MessageToJson(message, indent=4))
        
        print(f"已将第{frame}帧数据格式化\n")
    
    trace_file.close()

def pcapToJson(pcapFile, serviceID, methodID, jsonFile, message, pcapReadMode, frame=0):
    if pcapReadMode == 1:
        pcapToJsonOneFrame(pcapFile, serviceID, methodID, jsonFile, message, frame)
    elif pcapReadMode == 0:
        pcapToJsonWholeFile(pcapFile, serviceID, methodID, jsonFile, message)
    else:
        print("Invalid pcap read mode! Please check config setting.\n")