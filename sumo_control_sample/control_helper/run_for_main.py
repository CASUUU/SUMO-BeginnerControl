import traci
import sys
from .control import *
from .data_coll import *


interrupt_timestamp = 300

def run(base_setting_para):  # Function to execute the defined operations
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
        if time_stamp % 1 == 0:
            data_coll_ti(vehicle_ids)
        # Periodic summary of data
        ### - Accompanied by data output and saving -
        if time_stamp == interrupt_timestamp:
            data_coll_t_check(base_setting_para, interrupt_timestamp, time_stamp)
        
        
        step += 0.1
    traci.close()
    sys.stdout.flush()