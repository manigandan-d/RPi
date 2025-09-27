from mcp3008 import MCP3008
import time 

adc = MCP3008(vref=3.3)

print("Starting...")

try: 
    while True: 
        light_level = adc.read(0)
        print(f"Light Level: {light_level}")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    adc.close()
