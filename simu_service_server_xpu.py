import asyncio
import ipaddress
import logging

from someipy import ServiceBuilder, EventGroup
from someipy.service_discovery import construct_service_discovery
from someipy.serialization import Uint8, Uint64, Float32, SomeIpPayload
from someipy import construct_server_service_instance
from someipy.logging import set_someipy_log_level
from someipy import TransportLayerProtocol
from someipy.service import Method

from serialize_ap_sr_period_data import ap_sr_period_data
from serialize_sd_period_data import sd_period_data


# SOMEIP_SD_IP_ADDRESS = "224.0.0.251" # offline mode
SOMEIP_SD_IP_ADDRESS = "239.127.3.1" # online mode
SOMEIP_SD_PORT = 30490
# XPU_SOC_M_IP_ADDR = ("127.0.0.1") # simulated IP of ADAS ECU / offline mode
XPU_SOC_M_IP_ADDR = ("172.20.1.22")
XPU_SOC_M_SERVER_PORT = 55117

# SR Service
SR_SERVICE_INSTANCE_ID = 0x0001
SR_SERVICE_SERVICE_ID = 0x4010
SR_SERVICE_EVENT_GROUP_ID = 0x0001
AP_SR_PERIOD_DATA_ELEMENT_ID = 0x8002

# SD Service
SD_SERVICE_INSTANCE_ID = 0x0001
SD_SERVICE_SERVICE_ID = 0x4011
SD_SERVICE_EVENT_GROUP_ID = 0x0001
SD_PERIOD_DATA_ELEMENT_ID = 0x8002
    
async def main():
    global service_instance_SRService
    # It's possible to configure the logging level of the someipy library, e.g. logging.INFO, logging.DEBUG, logging.WARN, ..
    set_someipy_log_level(logging.DEBUG)
    
    # Since the construction of the class ServiceDiscoveryProtocol is not trivial and would require an async __init__ function
    # use the construct_service_discovery function
    # The local interface IP address needs to be passed so that the src-address of all SD UDP packets is correctly set
    service_discovery = await construct_service_discovery(
        SOMEIP_SD_IP_ADDRESS, SOMEIP_SD_PORT, XPU_SOC_M_IP_ADDR
    )

    ##########################################
    # Construct SR service
    ##########################################
    SRService_eventgroup = EventGroup(
        id = SR_SERVICE_EVENT_GROUP_ID,
        event_ids = [AP_SR_PERIOD_DATA_ELEMENT_ID]
    )

    SRService_service = (
        ServiceBuilder()
        .with_service_id(SR_SERVICE_SERVICE_ID)
        .with_major_version(1)
        .with_eventgroup(SRService_eventgroup)
        .build()
    )

    # For sending events use a ServerServiceInstance
    service_instance_SRService = await construct_server_service_instance(
        SRService_service,
        instance_id = SR_SERVICE_INSTANCE_ID,
        endpoint = (
            ipaddress.IPv4Address(XPU_SOC_M_IP_ADDR),
            XPU_SOC_M_SERVER_PORT,
        ),  # src IP and port of the service
        ttl = 5,
        sd_sender = service_discovery,
        cyclic_offer_delay_ms = 1000,
        protocol = TransportLayerProtocol.TCP,
    )

    ##########################################
    # Construct SD service
    ##########################################
    SDService_eventgroup = EventGroup(
        id = SD_SERVICE_EVENT_GROUP_ID,
        event_ids = [SD_PERIOD_DATA_ELEMENT_ID]
    )

    SDService_service = (
        ServiceBuilder()
        .with_service_id(SD_SERVICE_SERVICE_ID)
        .with_major_version(1)
        .with_eventgroup(SDService_eventgroup)
        .build()
    )

    # For sending events use a ServerServiceInstance
    service_instance_SDService = await construct_server_service_instance(
        SDService_service,
        instance_id = SD_SERVICE_INSTANCE_ID,
        endpoint = (
            ipaddress.IPv4Address(XPU_SOC_M_IP_ADDR),
            XPU_SOC_M_SERVER_PORT,
        ),  # src IP and port of the service
        ttl = 5,
        sd_sender = service_discovery,
        cyclic_offer_delay_ms = 1000,
        protocol = TransportLayerProtocol.TCP,
    )

    # The service instance has to be attached always to the ServiceDiscoveryProtocol object, so that the service instance
    # is notified by the ServiceDiscoveryProtocol about e.g. subscriptions from other ECUs
    service_discovery.attach(service_instance_SRService)
    service_discovery.attach(service_instance_SDService)

    # ..it's also possible to construct another ServerServiceInstance and attach it to service_discovery as well

    # After constructing and attaching ServerServiceInstances to the ServiceDiscoveryProtocol object the
    # start_offer method has to be called. This will start an internal timer, which will periodically send
    # Offer service entries with a period of "cyclic_offer_delay_ms" which has been passed above
    print("Start offering service..")
    service_instance_SRService.start_offer()
    service_instance_SDService.start_offer()

    try:
        while True:
            await asyncio.sleep(0.5)
            service_instance_SRService.send_event(
                SR_SERVICE_EVENT_GROUP_ID, AP_SR_PERIOD_DATA_ELEMENT_ID, ap_sr_period_data.payload
            )
            service_instance_SRService.send_event(
                SD_SERVICE_EVENT_GROUP_ID, SD_PERIOD_DATA_ELEMENT_ID, sd_period_data.payload
            )           
            # payload = b''
            # for payload in ap_sr_period_data:
            #     # Either cyclically send events in an endless loop..
            #     # await asyncio.Future()
            #     await asyncio.sleep(0.5)
            #     service_instance_SRService.send_event(
            #         SR_SERVICE_EVENT_GROUP_ID, AP_SR_PERIOD_DATA_ELEMENT_ID, payload
            #     )

    except asyncio.CancelledError:
        print("Stop offering service..")
        await service_instance_SRService.stop_offer()
        await service_instance_SDService.stop_offer()
    finally:
        print("Service Discovery close..")
        service_discovery.close()

    print("End main task..")

if __name__ == "__main__":
    asyncio.run(main())
