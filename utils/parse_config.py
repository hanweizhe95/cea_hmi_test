import configparser

# Create a configparser object
config = configparser.ConfigParser()

# Read the .ini file
config.read('config.ini')

# Access values from the .ini file
traceFileDir = config['Directory']['traceFileDir']
outputDir = config['Directory']['outputDir']

traceFile = config['TraceFile']['traceFile']

apSrPeriodData = config['JsonOutput']['apSrPeriodData']
apSrEventData = config['JsonOutput']['apSrEventData']
apSrPeriodData = config['JsonOutput']['apSrPeriodData']

pcapReadMode = config['Setting'].getint('pcapReadMode', fallback=0)
onlineMode = config['Setting'].getint('onlineMode', fallback=0)
sendApSrPeriodData = config['Setting'].getint('sendApSrPeriodData', fallback=0)
sendApSrEventData = config['Setting'].getint('sendApSrEventData', fallback=0)
sendSdPeriodData = config['Setting'].getint('sendSdPeriodData', fallback=0)

apSrPeriodDataFrameNumber = config['FrameNumber'].getint('apSrPeriodDataFrameNumber', fallback=0)
apSrEventDataFrameNumber = config['FrameNumber'].getint('apSrEventDataFrameNumber', fallback=0)
sdPeriodDataFrameNumber = config['FrameNumber'].getint('sdPeriodDataFrameNumber', fallback=0)

XPU_SOC_M_IP_ADDR = config['XPU']['XPU_SOC_M_IP_ADDR']
XPU_SOC_M_SR_SERVICE_SERVER_PORT = config['XPU'].getint('XPU_SOC_M_SR_SERVICE_SERVER_PORT')
XPU_SOC_M_SD_SERVICE_SERVER_PORT = config['XPU'].getint('XPU_SOC_M_SD_SERVICE_SERVER_PORT')

SOMEIP_SD_IP_ADDRESS = config['SOMEIP']['SOMEIP_SD_IP_ADDRESS']
SOMEIP_SD_PORT = config['SOMEIP'].getint('SOMEIP_SD_PORT')

SR_SERVICE_INSTANCE_ID = int(config['ID']['SR_SERVICE_INSTANCE_ID'], 16)
SR_SERVICE_SERVICE_ID = int(config['ID']['SR_SERVICE_SERVICE_ID'], 16)
SR_SERVICE_EVENT_GROUP_ID = int(config['ID']['SR_SERVICE_EVENT_GROUP_ID'], 16)
AP_SR_PERIOD_DATA_ELEMENT_ID = int(config['ID']['AP_SR_PERIOD_DATA_ELEMENT_ID'], 16)
AP_SR_EVENT_DATA_ELEMENT_ID = int(config['ID']['AP_SR_EVENT_DATA_ELEMENT_ID'], 16)
SD_SERVICE_INSTANCE_ID = int(config['ID']['SD_SERVICE_INSTANCE_ID'], 16)
SD_SERVICE_SERVICE_ID = int(config['ID']['SD_SERVICE_SERVICE_ID'], 16)
SD_SERVICE_EVENT_GROUP_ID = int(config['ID']['SD_SERVICE_EVENT_GROUP_ID'], 16)
SD_PERIOD_DATA_ELEMENT_ID = int(config['ID']['SD_PERIOD_DATA_ELEMENT_ID'], 16)