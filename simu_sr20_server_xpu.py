import asyncio
import ipaddress
import logging
from typing import Tuple

from someipy import ServiceBuilder, EventGroup
from someipy.service_discovery import construct_service_discovery
from someipy.serialization import Uint8, Uint64, Float32, SomeIpPayload
from someipy import construct_server_service_instance
from someipy.logging import set_someipy_log_level
from someipy import TransportLayerProtocol
from someipy.service import Method

from sr20_msg import SDServiceMsg
# from vehice_trace_replay import blist
from serializedXP import blist


# SD_MULTICAST_GROUP = "224.0.0.251" # offline mode
SD_MULTICAST_GROUP = "239.127.3.1" # online mode
SD_PORT = 30490
# INTERFACE_IP = ("127.0.0.1") # simulated IP of ADAS ECU / offline mode
INTERFACE_IP = ("172.20.1.22") # simulated IP of ADAS ECU / online mode

SDService_Service_ID = 0x4010 # SD Service ID
SDServiceData_EVENTGROUP_ID = 0x0001 # SD event group
SD_Period_Data_ID = 0x8002
SDService_INSTANCE_ID = 0x0001 # SD Service instance ID for CDCU
# SDService_INSTANCE_ID = 0x0002 # SD Service instance ID for CDCU
    
async def main():
    global service_instance_SDService
    # It's possible to configure the logging level of the someipy library, e.g. logging.INFO, logging.DEBUG, logging.WARN, ..
    set_someipy_log_level(logging.DEBUG)
    
    # Since the construction of the class ServiceDiscoveryProtocol is not trivial and would require an async __init__ function
    # use the construct_service_discovery function
    # The local interface IP address needs to be passed so that the src-address of all SD UDP packets is correctly set
    service_discovery = await construct_service_discovery(
        SD_MULTICAST_GROUP, SD_PORT, INTERFACE_IP
    )

    SDService_eventgroup = EventGroup(
        id=SDServiceData_EVENTGROUP_ID, event_ids=[SD_Period_Data_ID]
    )

    SDService_service = (
        ServiceBuilder()
        .with_service_id(SDService_Service_ID)
        .with_major_version(1)
        .with_eventgroup(SDService_eventgroup)
        .build()
    )

    # For sending events use a ServerServiceInstance
    service_instance_SDService = await construct_server_service_instance(
        SDService_service,
        instance_id=SDService_INSTANCE_ID,
        endpoint=(
            ipaddress.IPv4Address(INTERFACE_IP),
            # 55118,
            55117,
        ),  # src IP and port of the service
        ttl=5,
        sd_sender=service_discovery,
        cyclic_offer_delay_ms=1000,
        protocol=TransportLayerProtocol.TCP,
        client_id=0x1016
        # client_id=0x0000
    )

    # The service instance has to be attached always to the ServiceDiscoveryProtocol object, so that the service instance
    # is notified by the ServiceDiscoveryProtocol about e.g. subscriptions from other ECUs
    service_discovery.attach(service_instance_SDService)

    # ..it's also possible to construct another ServerServiceInstance and attach it to service_discovery as well

    # After constructing and attaching ServerServiceInstances to the ServiceDiscoveryProtocol object the
    # start_offer method has to be called. This will start an internal timer, which will periodically send
    # Offer service entries with a period of "cyclic_offer_delay_ms" which has been passed above
    print("Start offering service..")
    service_instance_SDService.start_offer()

    SD_msg = SDServiceMsg()

    try:
        while True:
            payload = b''
            for payload in blist:
                # Either cyclically send events in an endless loop..
                # await asyncio.Future()
                await asyncio.sleep(0.5)
                # SD_msg.timestamp = Uint64(SD_msg.timestamp.value + 1)
                service_instance_SDService.send_event(
                    SDServiceData_EVENTGROUP_ID, SD_Period_Data_ID, payload
                )

    except asyncio.CancelledError:
        print("Stop offering service..")
        await service_instance_SDService.stop_offer()
    finally:
        print("Service Discovery close..")
        service_discovery.close()

    print("End main task..")

if __name__ == "__main__":
    asyncio.run(main())
