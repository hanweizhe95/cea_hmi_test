from parser.pcapToJson import pcapToJsonOneFrame
from parser.pcapToJson import pcapToJson
from proto_ap.WM_display_realtime_pb2 import ApDrivingData
from proto_ap.WM_display_map_pb2 import map_trajectory_data
import sys
sys.path.append('./sr2_0')
import sd_overall_pb2
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
from utils.parse_config import apSrPeriodDataFrameNumber
from utils.parse_config import apSrEventDataFrameNumber
from utils.parse_config import sdPeriodDataFrameNumber
import os

if not os.path.exists(f'{outputDir}'):
        os.mkdir(f'{outputDir}')

original_trace_file = f"{traceFileDir}/{traceFile}"

if pcapReadMode == 1:
    pcapToJsonOneFrame(
        original_trace_file, 
        SR_SERVICE_SERVICE_ID,
        AP_SR_PERIOD_DATA_ELEMENT_ID, 
        f"{outputDir}/{AP_SR_PERIOD_DATA_JSON}", 
        ApDrivingData(),
        apSrPeriodDataFrameNumber
        )
    pcapToJsonOneFrame(
        original_trace_file, 
        SR_SERVICE_SERVICE_ID,
        AP_SR_EVENT_DATA_ELEMENT_ID, 
        f"{outputDir}/{AP_SR_EVENT_DATA_JSON}", 
        map_trajectory_data(),
        apSrEventDataFrameNumber
        )
    pcapToJsonOneFrame(
        original_trace_file,
        SD_SERVICE_SERVICE_ID,
        SD_PERIOD_DATA_ELEMENT_ID,
        f"{outputDir}/{SD_PERIOD_DATA_JSON}",
        sd_overall_pb2.SDOverallMsg(),
        sdPeriodDataFrameNumber
        )
elif pcapReadMode == 0:
    pcapToJson(
        original_trace_file, 
        SR_SERVICE_SERVICE_ID,
        AP_SR_PERIOD_DATA_ELEMENT_ID, 
        f"{outputDir}/{AP_SR_PERIOD_DATA_JSON}", 
        ApDrivingData(),
        )
    pcapToJson(
        original_trace_file, 
        SR_SERVICE_SERVICE_ID,
        AP_SR_EVENT_DATA_ELEMENT_ID, 
        f"{outputDir}/{AP_SR_EVENT_DATA_JSON}", 
        map_trajectory_data()
        )
    pcapToJson(
        original_trace_file,
        SD_SERVICE_SERVICE_ID,
        SD_PERIOD_DATA_ELEMENT_ID,
        f"{outputDir}/{SD_PERIOD_DATA_JSON}",
        sd_overall_pb2.SDOverallMsg()
        )