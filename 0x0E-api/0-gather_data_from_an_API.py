#!/usr/bin/env python3

import requests
import sys

if __name__ == "__main__":

    packet_URL = (
        "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    )
    data_packet = requests.get(packet_URL)

    print(data_packet.text)
