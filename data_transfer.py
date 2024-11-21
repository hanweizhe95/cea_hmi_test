from parser.pcapToJson import pcapToJsonOneFrame
from proto_ap.WM_display_realtime_pb2 import ApDrivingData
from proto_ap.WM_display_map_pb2 import map_trajectory_data
import sys
sys.path.append('./sr2_0')
import sd_overall_pb2

original_trace_file = r"trace/Logging_G6_2024-10-18_10-24-57_TPA.pcapng"

# SR Service
SR_SERVICE_SERVICE_ID = 0x4010
AP_SR_PERIOD_DATA_ELEMENT_ID = 0x8002
AP_SR_PERIOD_DATA_JSON = "ap_sr_period_data.json"
AP_SR_EVENT_DATA_ELEMENT_ID = 0x8003
AP_SR_EVENT_DATA_JSON = "ap_sr_event_data.json"

# SD Service
SD_SERVICE_SERVICE_ID = 0x4011
SD_PERIOD_DATA_ELEMENT_ID = 0x8002
SD_PERIOD_DATA_JSON = "sd_period_data.json"

pcapToJsonOneFrame(
    original_trace_file, 
    SR_SERVICE_SERVICE_ID,
    AP_SR_PERIOD_DATA_ELEMENT_ID, 
    AP_SR_PERIOD_DATA_JSON, 
    ApDrivingData(),
    1000
    )

pcapToJsonOneFrame(
    original_trace_file, 
    SR_SERVICE_SERVICE_ID,
    AP_SR_EVENT_DATA_ELEMENT_ID, 
    AP_SR_EVENT_DATA_JSON, 
    map_trajectory_data()
    )

pcapToJsonOneFrame(
    original_trace_file,
    SD_SERVICE_SERVICE_ID,
    SD_PERIOD_DATA_ELEMENT_ID,
    SD_PERIOD_DATA_JSON,
    sd_overall_pb2.SDOverallMsg()
    )