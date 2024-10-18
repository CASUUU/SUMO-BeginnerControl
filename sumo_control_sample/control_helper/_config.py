lane_id_dict = {
    'left': ["1_2", "3_3", "4_2", "0_1_2", "1_0_3"],
    'middle': ["1_1", "3_2", "4_1", "0_1_1", "1_0_2"],
    'right': ["1_0", "3_1", "4_0", "0_1_0", "1_0_1"],
    'acc': ["3_0"]
}

base_info_left, base_info_middle, base_info_right, base_info_acc = ([] for _ in range(4))
delay_aggregated_data = {} 
delay_data = []