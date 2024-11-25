## File description
1. **data_transfer.py**: transfer trace file to json
2. **simu_service_server_xpu.py**: replay pcap on CDCU
3. **parser/pcapToJson.py**: pcan to json
4. **out/xxx.json**: output of pcapToJson--> modify this file for signal value check.
5. **serialization/serialize_xxx.py**: serialize json log
6. **xconfig.ini**: configuration file
7. **utils/parse_config.py**: parse configuration file

### Description of xconfig.ini
+ [Directory] : input and out directory
    + traceFileDir : trace file directory
    + outputDir : output directory

+ [TraceFile]
    + traceFile : trace file name

+ [JsonOutput]
    + apSrPeriodData : json file name of AP_SR_Period_Data
    + apSrEventData : json file name of AP_SR_Event_Data
    + sdPeriodData : json file name of SD_Period_Data

+ [Setting]
    + pcapReadMode : 
        + 0 : whole file read mode
        + 1 : one frame read mode
    + onlineMode
        + 0 : offline mode
        + 1 : online mode
    + sendApSrPeriodData
        + 0 : mute data sending
        + 1 : unmute data sending
    + sendApSrEventData
        + 0 : mute data sending
        + 1 : unmute data sending
    + sendSdPeriodData
        + 0 : mute data sending
        + 1 : unmute data sending

+ [FrameNumber] : parse which frame of pcap
    + apSrPeriodDataFrameNumber : parse which frame of AP_SR_Period_Data
    + apSrEventDataFrameNumber : parse which frame of AP_SR_Event_Date
    + sdPeriodDataFrameNumber : parse which frame of SD_Period_Date

+ [XPU] : XPU related IP and Port
    + XPU_SOC_M_IP_ADDR = 172.20.1.22
    + XPU_SOC_M_SR_SERVICE_SERVER_PORT = 55117
    + XPU_SOC_M_SD_SERVICE_SERVER_PORT = 55118

+ [SOMEIP] : SOME/IP related IP and Port
    + SOMEIP_SD_IP_ADDRESS = 239.127.3.1
    + SOMEIP_SD_PORT = 30490

+ [ID] : refer to kMatrix
    + SR_SERVICE_INSTANCE_ID = 0x0001
    + SR_SERVICE_SERVICE_ID = 0x4010
    + SR_SERVICE_EVENT_GROUP_ID = 0x0001
    + AP_SR_PERIOD_DATA_ELEMENT_ID = 0x8002
    + AP_SR_EVENT_DATA_ELEMENT_ID = 0x8003
    + SD_SERVICE_INSTANCE_ID = 0x0001
    + SD_SERVICE_SERVICE_ID = 0x4011
    + SD_SERVICE_EVENT_GROUP_ID = 0x0001
    + SD_PERIOD_DATA_ELEMENT_ID = 0x8002

## Preinstalled lib
1. pyshark
2. someipy

## Run
0. cofigure [xconfig.ini](#description-of-xconfigini) for personal setting
1. python .\data_transfer.py
2. python .\simu_service_server_xpy.py