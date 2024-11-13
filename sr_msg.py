from dataclasses import dataclass
from someipy.serialization import (
    SomeIpPayload,
    SomeIpFixedSizeArray,
    Uint8,
    Uint64,
    Float32,
)

# With someipy it's possible to either send and receive payloads unserialized simply as bytes-objects. This is useful
# when you don't care about the content, e.g. reading binary data and simply sending it.
# However, you can also define the SOME/IP payload structure directly as Python classes and serialize your Python object
# to a bytes-payload which can be sent. You can also deserialize a received bytes-object into your defined
# Python object structure.

# In this example we define a "temperature message" that consists of another SOME/IP struct and of a fixed size
# SOME/IP array

@dataclass
class SRServiceMsg(SomeIpPayload):
    # Always define payloads with the @dataclass decorator. This leads to the __eq__ being
    # generated which makes it easy to compare the content of two messages.
    # For defining a payload struct simply derive from the SomeIpPayload class. This will ensure
    # the Python object can be serialized and deserialized and supports e.g. len() calls which
    # will return the length of the payload in bytes

    HeartBeatTickArray: SomeIpFixedSizeArray

    def __init__(self):
        self.HeartBeatTickArray = SomeIpFixedSizeArray(Uint8, 5)
        # Arrays can be modelled using the SomeIpFixedSizeArray class which gets the type that
        # the array shall hold (e.g. Float32) and the number of elements
        # The len(self.measurements) call will return the number of bytes (4*len(Float32)).
        # If you need to now the number of elements use len(self.measurements.data).


# Simple example how to instantiate a payload, change values, serialize and deserialize
if __name__ == "__main__":
    tmp_msg = SRServiceMsg()

    tmp_msg.HeartBeatTickArray.data[0] = Uint8(22)
    tmp_msg.HeartBeatTickArray.data[1] = Uint8(23)
    tmp_msg.HeartBeatTickArray.data[2] = Uint8(24)
    tmp_msg.HeartBeatTickArray.data[3] = Uint8(25)

    # The @dataclass decorator will also generate a __repr__ function
    print(tmp_msg)

    # serialize() will return a bytes object
    output = tmp_msg.serialize()
    print(output.hex())

    # Create a new TemperatureMsg from the serialized bytes
    tmp_msg_again = SRServiceMsg().deserialize(output)
    print(tmp_msg_again)

    assert tmp_msg_again == tmp_msg
