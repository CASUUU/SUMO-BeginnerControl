import traci
from ._config import *


def control_func(vehicle_id):
    # TODO: your control function
    # This is just an example.
    vehicle_lane_id = traci.vehicle.getLaneID(vehicle_id)
    if vehicle_lane_id in lane_id_dict['left']:
        traci.vehicle.setAccel(vehicle_id, 1.2)
