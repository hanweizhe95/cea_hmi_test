from parser.pcapToJson import pcapToJson
from proto_ap.WM_display_realtime_pb2 import ApDrivingData
from proto_ap.WM_display_map_pb2 import map_trajectory_data
from sr_service.proto.sr2_0.sd_overall_pb2 import SDOverallMsg
from utils.parse_config import traceFileDir
from utils.parse_config import traceFile
from utils.parse_config import SR_SERVICE_SERVICE_ID
from utils.parse_config import AP_SR_PERIOD_DATA_ELEMENT_ID
from utils.parse_config import AP_SR_PERIOD_DATA_JSON
from utils.parse_config import AP_SR_EVENT_DATA_ELEMENT_ID
from utils.parse_config import AP_SR_EVENT_DATA_JSON
from utils.parse_config import SD_SERVICE_SERVICE_ID
from utils.parse_config import SD_PERIOD_DATA_ELEMENT_ID
from utils.parse_config import SD_PERIOD_DATA_JSON
from utils.parse_config import outputDir
from utils.parse_config import pcapReadMode
from utils.parse_config import parseApSrPeriodData
from utils.parse_config import parseApSrEventData
from utils.parse_config import parseSdPeriodData
from utils.parse_config import apSrPeriodDataFrameNumber
from utils.parse_config import apSrEventDataFrameNumber
from utils.parse_config import sdPeriodDataFrameNumber
import os

if not os.path.exists(f'{outputDir}'):
        os.mkdir(f'{outputDir}')

original_trace_file = f"{traceFileDir}/{traceFile}"

if parseApSrPeriodData:
    pcapToJson(
        original_trace_file, 
        SR_SERVICE_SERVICE_ID,
        AP_SR_PERIOD_DATA_ELEMENT_ID, 
        f"{outputDir}/{AP_SR_PERIOD_DATA_JSON}", 
        ApDrivingData(),
        pcapReadMode,
        apSrPeriodDataFrameNumber
        )
else:
    print("AP_SR_Period_Data is not parsed, switch on setting in config file if necessary.\n")

if parseApSrEventData:
    pcapToJson(
        original_trace_file, 
        SR_SERVICE_SERVICE_ID,
        AP_SR_EVENT_DATA_ELEMENT_ID, 
        f"{outputDir}/{AP_SR_EVENT_DATA_JSON}", 
        map_trajectory_data(),
        pcapReadMode,
        apSrEventDataFrameNumber
        )
else:
    print("AP_SR_Event_Data is not parsed, switch on setting in config file if necessary.\n")

if parseSdPeriodData:
    pcapToJson(
        original_trace_file,
        SD_SERVICE_SERVICE_ID,
        SD_PERIOD_DATA_ELEMENT_ID,
        f"{outputDir}/{SD_PERIOD_DATA_JSON}",
        SDOverallMsg(),
        pcapReadMode,
        sdPeriodDataFrameNumber
        )
else:
    print("SD_Period_Data is not parsed, switch on setting in config file if necessary.\n")