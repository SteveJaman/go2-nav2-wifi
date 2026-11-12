#!/usr/bin/env python3
import time
import sys
from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.sport.sport_client import SportClient

def main():
    print("[TEST] Initializing DDS Network...")
    # The container uses eth0 to talk to the robot's internal network
    ChannelFactoryInitialize(0, "wlx1cbfce22ca47") 

    print("[TEST] Connecting to SportClient...")
    client = SportClient()
    client.SetTimeout(10.0)
    client.Init()

    print("[TEST] Sending StandUp command...")
    client.StandUp()
    time.sleep(2.0) # Wait for the dog to balance

    print("[TEST] Sending FootRaiseHeight(+0.03) -> You should see the feet lift higher!")
    client.FootRaiseHeight(0.03)
    time.sleep(4.0) # Hold it for 4 seconds so you can see it

    print("[TEST] Resetting FootRaiseHeight to 0.0 (Normal)...")
    client.FootRaiseHeight(0.0)

    print("[TEST] Done.")

if __name__ == "__main__":
    main()
