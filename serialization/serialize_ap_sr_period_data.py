import json
from google.protobuf import json_format
from proto_ap.WM_display_realtime_pb2 import ApDrivingData
from utils.parse_config import outputDir

# 读取转换后的 JSON 文件
with open(f'{outputDir}/ap_sr_period_data.json', 'r') as f:
    json_data = json.load(f)[0]

# 创建 RootMessage 对象
root_message = ApDrivingData()

#     Location location = 1;  // 车身位置坐标
#     repeated Slot slot = 2;  // AP、APA过程的可泊车位（实时探测车位）
#     repeated StripObstacle obj = 3;  // 未使用
#     repeated ApLaneLineInfo lanelines = 4;  // 未使用
#     repeated int32 curFloor = 5;            // [curfloor, next floor]
#     repeated ApTrajectoryDataType Trajectory = 6;  // VPA、APA泊车轨迹蓝色的引导线
#     repeated ApDynaObject dynObj = 7;  // 动态目标
#     ApEssentialMsg essentialMsg = 8;  // 泊车实时状态
#     repeated Slot slotAvm = 9;  // 学习过程中实时探测到的AVM车位
#     repeated TrainingSpdBump spdBump = 10;  // 学习过程中探测到的减速带（IMU探测）
#     repeated SlotIdMapping slotIdMapping = 11;  // 学习过程中自动泊入时可泊车位和当前AVM车位匹配信息 ，只用到size，里面的两个slotId均未使用，待确认
#     repeated Ap_StaticObject ap_StaticObject = 12;  // 静态目标物
#     ApNaviMsg naviMsg = 13;  // 起点导航信息，暂停使用
#     SRprotobuf.OnlineLocalMapMsg online_local_map_msg = 14;  // 包括实时车道线和热力图，是泊车新增的元素，所以结构和名字取为和行车一致
#     repeated Wall wall = 15;  // 墙面

# print(type(json_data))

# 解析 'location' 字段
if 'location' in json_data:
    json_format.ParseDict(json_data['location'], root_message.location)

# 解析 'slot' 字段
if 'slot' in json_data:
    for slot_data in json_data['slot']:
        slot = root_message.slot.add()
        json_format.ParseDict(slot_data, slot)

# 解析 'curFloor' 字段
if 'curFloor' in json_data:
    for curFloor_data in json_data['curFloor']:
        curFloor = root_message.curFloor.add()
        json_format.ParseDict(curFloor_data, curFloor)

# 解析 'Trajectory' 字段
if 'Trajectory' in json_data:
    for trajectory_data in json_data['Trajectory']:
        trajectory = root_message.Trajectory.add()
        json_format.ParseDict(trajectory_data, trajectory)

# 解析 'dynObj' 字段
# ApDynaObject dynObj
if 'dynObj' in json_data:
    for dyn_obj_data in json_data['dynObj']:
        dyn_Obj = root_message.dynObj.add()
        json_format.ParseDict(dyn_obj_data, dyn_Obj)
# if 'dynObj' in json_data:
#     json_format.ParseDict(json_data['dynObj'], root_message.dynObj)

# 解析 'essentialMsg' 字段
if 'essentialMsg' in json_data:
    json_format.ParseDict(json_data['essentialMsg'], root_message.essentialMsg)

# 解析 'slotAvm' 字段
if 'slotAvm' in json_data:
    for slot_avm_data in json_data['slotAvm']:
        slot_avm = root_message.slotAvm.add()
        json_format.ParseDict(slot_avm_data, slot_avm)

# 解析 'spdBump' 字段
if 'spdBump' in json_data:
    for spd_bump_data in json_data['spdBump']:
        spd_bump = root_message.spdBump.add()
        json_format.ParseDict(spd_bump_data, spd_bump)

# 解析 'slotIdMapping' 字段
if 'slotIdMapping' in json_data:
    for slot_id_mapping_data in json_data['slotIdMapping']:
        slot_id_mapping = root_message.slotIdMapping.add()
        json_format.ParseDict(slot_id_mapping_data, slot_id_mapping)

# 解析 'ap_StaticObject' 字段
if 'apStaticObject' in json_data:
    for static_obj_data in json_data['apStaticObject']:
        static_obj = root_message.ap_StaticObject.add()
        json_format.ParseDict(static_obj_data, static_obj)

# 解析 'online_local_map_msg' 字段
if 'onlineLocalMapMsg' in json_data:
    json_format.ParseDict(json_data['onlineLocalMapMsg'], root_message.online_local_map_msg)

# 解析 'wall' 字段
if 'wall' in json_data:
    for wall_data in json_data['wall']:
        wall = root_message.wall.add()
        json_format.ParseDict(wall_data, wall)

# 序列化 RootMessage 为二进制数据
ap_sr_period_data = root_message.SerializeToString()