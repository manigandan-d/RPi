from mcp3008 import MCP3008
import time 

adc = MCP3008(vref=3.3)

print("Starting...")

try: 
    while True: 
        raw_val = adc.read(0)
        volts = adc.read_voltage(0)

        print(f"ADC Value: {raw_val:4d}  Voltage: {volts:.2f} V")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    adc.close()
