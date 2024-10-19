import traci
import pandas as pd
from ._config import *


def coll_base_info(vehicle_id, time_stamp):
    global base_info_left, base_info_middle, base_info_right, base_info_acc
    vehicle_lane_id = traci.vehicle.getLaneID(vehicle_id)
    vehicle_type = traci.vehicle.getTypeID(vehicle_id)
    vehicle_speed = traci.vehicle.getSpeed(vehicle_id)
    vehicle_acc = traci.vehicle.getAcceleration(vehicle_id)
    vehicle_pos = traci.vehicle.getPosition(vehicle_id)
    if vehicle_lane_id in lane_id_dict['left']:
        base_info_left.append(["left_lane", vehicle_id, vehicle_type, vehicle_speed, vehicle_acc, vehicle_pos[0], time_stamp])
    elif vehicle_lane_id in lane_id_dict['middle']:
        base_info_middle.append(["middle_lane", vehicle_id, vehicle_type, vehicle_speed, vehicle_acc, vehicle_pos[0], time_stamp])
    elif vehicle_lane_id in lane_id_dict['right']:
        base_info_right.append(["right_lane", vehicle_id, vehicle_type, vehicle_speed, vehicle_acc, vehicle_pos[0], time_stamp])
    elif vehicle_lane_id in lane_id_dict['acc']:
        base_info_acc.append(["acc_lane", vehicle_id, vehicle_type, vehicle_speed, vehicle_acc, vehicle_pos[0], time_stamp])

def coll_delay_data(vehicle_ids):
    global delay_data, delay_aggregated_data
    for vehicle_id in vehicle_ids:
        pos = traci.vehicle.getPosition(vehicle_id)
        pos_x = pos[0]
        if pos_x > 3240:
            vehicle_type = traci.vehicle.getTypeID(vehicle_id)
            delay_time = traci.vehicle.getTimeLoss(vehicle_id)
            if vehicle_id not in delay_aggregated_data:
                delay_aggregated_data[vehicle_id] = {
                    'vehicle_id': vehicle_id,
                    'delay_time': delay_time}

def data_coll_vi_ti(vehicle_id, time_stamp):
    coll_base_info(vehicle_id, time_stamp)

def data_coll_ti(vehicle_ids):
    coll_delay_data(vehicle_ids)

def data_coll_t_check(base_setting_para, interrupt_timesatmp, time_stamp):
    F_NAME = base_setting_para
    if base_setting_para[3]:
        tag = 'without_ramp'
    else:
        tag = 'ramp'
    file_name_base = f"mpr_{F_NAME[2]}_flow_{F_NAME[0]}_{F_NAME[1]}_time_{interrupt_timesatmp}_{tag}"

    base_info_left_df = pd.DataFrame(base_info_left, columns=['left_lane', 'vehicle_id_left', 'vehicle_type_left', 'speed_left', 'acc_left', 'pos_left', 'time_stamp_left'])
    base_info_middle_df = pd.DataFrame(base_info_middle, columns=['middle_lane', 'vehicle_id_middle', 'vehicle_type_middle', 'speed_middle', 'acc_middle', 'pos_middle', 'time_stamp_middle'])
    base_info_right_df = pd.DataFrame(base_info_right, columns=['right_lane', 'vehicle_id_right', 'vehicle_type_right', 'speed_right', 'acc_right', 'pos_right', 'time_stamp_right'])
    base_info_acc_df = pd.DataFrame(base_info_acc, columns=['acc_lane', 'vehicle_id_acc', 'vehicle_type_acc', 'speed_acc', 'acc_acc', 'pos_acc', 'time_stamp_acc'])
    base_info_total = pd.concat([base_info_left_df, base_info_middle_df, base_info_right_df, base_info_acc_df], axis=1)
    base_info_total.to_csv(f"../../output/data/base_info_data/base_info_{file_name_base}.csv", index=False)

    delay_data = pd.DataFrame(delay_aggregated_data.values())
    delay_data.to_csv(f"../../output/data/delay_data/delay_{file_name_base}.csv", index=False)
