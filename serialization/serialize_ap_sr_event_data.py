import json
from google.protobuf import json_format
from proto_ap.WM_display_map_pb2 import map_trajectory_data

# 读取转换后的 JSON 文件
with open('ap_sr_event_data.json', 'r') as f:
    json_data = json.load(f)[0]

# 创建 RootMessage 对象
root_message = map_trajectory_data()

    # venue_map venueMap = 1;  // 地图信息
    # SRprotobuf.ApTrajectoryDataType apTrajectoryData = 2;  // VPA激活后显示的地面道路
    # uint32 timestamp = 3;  // 发送地图时刻点的时间戳，XPU调试用
    # int32 isAcrossFloors = 4;  //0:不跨楼层， 1:跨楼层


# 解析 'venueMap' 字段
if 'venueMap' in json_data:
    json_format.ParseDict(json_data['venueMap'], root_message.venueMap)

# 解析 'apTrajectoryData' 字段
if 'apTrajectoryData' in json_data:
    json_format.ParseDict(json_data['apTrajectoryData'], root_message.apTrajectoryData)

# 解析 'timestamp' 字段
if 'timestamp' in json_data:
    root_message.timestamp = json_data['timestamp']

# 解析 'isAcrossFloors' 字段
if 'isAcrossFloors' in json_data:
    root_message.isAcrossFloors = json_data['isAcrossFloors']

# 序列化 RootMessage 为二进制数据
ap_sr_event_data = root_message.SerializeToString()