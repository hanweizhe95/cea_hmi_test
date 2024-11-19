import pyshark
import socket
import time
import sys
import json

from google.protobuf import json_format  # protobuf==4.25.1  
sys.path.append('./proto_ap')    
import WM_display_realtime_pb2
sys.path.append('./sr2_0')
import sd_overall_pb2

original_trace_file = r"./Logging018.pcapng"


SR_SERVICE_SERVICE_ID = 0x4010
AP_SR_PERIOD_DATA_ELEMENT_ID = 0x8002
AP_SR_PERIOD_DATA_JSON = "ap_sr_period_data.json"

SD_SERVICE_SERVICE_ID = 0x4011
SD_PERIOD_DATA_ELEMENT_ID = 0x8002
SD_PERIOD_DATA_JSON = "sd_period_data.json"

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

pcapToJson(
    original_trace_file, 
    SR_SERVICE_SERVICE_ID,
    AP_SR_PERIOD_DATA_ELEMENT_ID, 
    AP_SR_PERIOD_DATA_JSON, 
    WM_display_realtime_pb2.ApDrivingData()
    )

pcapToJson(
    original_trace_file,
    SD_SERVICE_SERVICE_ID,
    SD_PERIOD_DATA_ELEMENT_ID,
    SD_PERIOD_DATA_JSON,
    sd_overall_pb2.SDOverallMsg()
    )