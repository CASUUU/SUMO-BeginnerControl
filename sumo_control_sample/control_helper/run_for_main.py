import traci
import sys
from .control import *
from .data_coll import *

interrupt_timestamp = 500

def run():  # Function to execute the defined operations
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        # Basic information in this simulation step
        vehicle_ids = traci.vehicle.getIDList()
        time_stamp = int(step * 10) / 10
        # Control each vehicle in sequence
        for vehicle_id in vehicle_ids:
            control_func(vehicle_id)
            if time_stamp % 1 == 0:
                data_coll_vi_ti(vehicle_id, time_stamp)
        
        step += 0.1
    traci.close()
    sys.stdout.flush()