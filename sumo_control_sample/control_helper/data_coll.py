import traci
from ._config import *


def data_coll_vi_ti(vehicle_id, time_stamp):
    data = traci.vehicle.getAccel(vehicle_id)