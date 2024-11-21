## File description
1. **data_transfer.py**: transfer trace file to json
2. **simu_service_server_xpu.py**: replay pcap on CDCU
3. **pcapToJson.py**: pcan to json
4. **xxx.json**: output of pcapToJson--> modify this file for signal value check.
5. **serialization/serialize_xxx.py**: serialize json log


## Preinstalled lib
1. pyshark
2. someipy

## Run
1. python .\data_transfer.py
2. python .\simu_service_server_xpy.py