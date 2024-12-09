import json
import os
from google.protobuf import json_format
from sr_service.proto.sr2_0.sd_overall_pb2 import SDOverallMsg
from utils.parse_config import outputDir
from utils.parse_config import SD_PERIOD_DATA_JSON

# 创建 RootMessage 对象
root_message = SDOverallMsg()

# 读取转换后的 JSON 文件
if not os.path.exists(f'{outputDir}/{SD_PERIOD_DATA_JSON}'):
    print(f"File {SD_PERIOD_DATA_JSON} not exists")
elif os.path.getsize(f'{outputDir}/{SD_PERIOD_DATA_JSON}') < 3:
    print(f"File {SD_PERIOD_DATA_JSON} is empty")
else:
    with open(f'{outputDir}/{SD_PERIOD_DATA_JSON}', 'r') as f:
        json_data = json.load(f)

    # 填充 SfbpRwmDdsMsg 消息
    if 'sfbpRwmDdsMsg' in json_data:
        json_format.ParseDict(json_data['sfbpRwmDdsMsg'], root_message.sfbp_rwm_dds_msg)

    # 填充 OnlineLocalMapMsg 消息
    if 'onlineLocalMapMsg' in json_data:
        json_format.ParseDict(json_data['onlineLocalMapMsg'], root_message.online_local_map_msg)

    # 填充 MfLocalposeMsg 消息
    if 'mfLocalposeMsg' in json_data:
        json_format.ParseDict(json_data['mfLocalposeMsg'], root_message.mf_localpose_msg)

    # 填充 MfLocalposeMsg 消息
    if 'localposeMsg' in json_data:
        json_format.ParseDict(json_data['localposeMsg'], root_message.localpose_msg)

    # 填充 MfLocalposeMsg 消息
    if 'bpHmiOutputMsg' in json_data:
        json_format.ParseDict(json_data['bpHmiOutputMsg'], root_message.bp_hmi_output_msg)

    # 填充 MfLocalposeMsg 消息
    if 'mpOutputMsg' in json_data:
        json_format.ParseDict(json_data['mpOutputMsg'], root_message.mp_output_msg)

    # 填充 MfLocalposeMsg 消息
    if 'mapFusionLanesForScuMsg' in json_data:
        json_format.ParseDict(json_data['mapFusionLanesForScuMsg'], root_message.map_fusion_lanes_for_scu_msg)

    # 填充 MfLocalposeMsg 消息
    if 'smMsg' in json_data:
        json_format.ParseDict(json_data['smMsg'], root_message.sm_msg)

    # 填充 MfLocalposeMsg 消息
    if 'aebMsg' in json_data:
        json_format.ParseDict(json_data['aebMsg'], root_message.aeb_msg)

# 序列化 RootMessage 为二进制数据
sd_period_data = root_message.SerializeToString()