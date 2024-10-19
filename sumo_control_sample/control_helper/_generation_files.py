def generate_roadnet_file_func(speed_setting):
    with open("../../deployment/environment/road.net.xml", "w") as road_net_file:
        print(f"""<?xml version="1.0" encoding="UTF-8"?>

<net version="1.16" junctionCornerDetail="5" limitTurnSpeed="5.50" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/net_file.xsd">

    <location netOffset="85.03,26.17" convBoundary="0.00,-65.00,3250.00,0.00" origBoundary="-85.03,-26.17,270.54,-0.17" projParameter="!"/>

    <edge id=":0_0" function="internal">
        <lane id=":0_0_0" index="0" speed="{speed_setting[0]}" length="8.96" width="3.50" shape="1993.60,-7.94 1996.21,-7.43 1998.01,-7.15 1999.83,-7.03 2002.48,-7.00"/>
    </edge>
    <edge id=":0_1" function="internal">
        <lane id=":0_1_0" index="0" speed="{speed_setting[0]}" length="5.71" width="3.50" shape="1996.77,-3.50 2002.48,-3.50"/>
        <lane id=":0_1_1" index="1" speed="{speed_setting[0]}" length="5.71" width="3.50" shape="1996.77,0.00 2002.48,0.00"/>
        <lane id=":0_1_2" index="2" speed="{speed_setting[0]}" length="5.71" width="3.50" shape="1996.77,3.50 2002.48,3.50"/>
    </edge>
    <edge id=":1_0" function="internal">
        <lane id=":1_0_0" index="0" speed="{speed_setting[0]}" length="8.24" width="3.50" shape="2250.11,-7.00 2252.59,-6.45 2254.11,-5.25 2255.63,-4.05 2258.11,-3.50"/>
        <lane id=":1_0_1" index="1" speed="{speed_setting[0]}" length="8.24" width="3.50" shape="2250.11,-3.50 2258.11,-3.50"/>
        <lane id=":1_0_2" index="2" speed="{speed_setting[0]}" length="8.24" width="3.50" shape="2250.11,0.00 2258.11,0.00"/>
        <lane id=":1_0_3" index="3" speed="{speed_setting[0]}" length="8.24" width="3.50" shape="2250.11,3.50 2258.11,3.50"/>
    </edge>

    <edge id="1" from="1-begin" to="0" priority="-1" type="1" spreadType="center" shape="0.00,0.00 2001.48,0.00">
        <lane id="1_0" index="0" speed="{speed_setting[0]}" length="1996.77" width="3.50" shape="-0.00,-3.50 1996.77,-3.50"/>
        <lane id="1_1" index="1" speed="{speed_setting[0]}" length="1996.77" width="3.50" shape="-0.00,0.00 1996.77,0.00"/>
        <lane id="1_2" index="2" speed="{speed_setting[0]}" length="1996.77" width="3.50" shape="-0.00,3.50 1996.77,3.50"/>
    </edge>
    <edge id="2" from="2-begin" to="0" priority="-1" type="1" spreadType="center" shape="1700.00,-65.00 1993.60,-7.94">
        <lane id="2_0" index="0" speed="{speed_setting[1]}" length="299.09" width="3.50" shape="1700.00,-65.00 1993.60,-7.94"/>
    </edge>
    <edge id="3" from="0" to="1" priority="-1" type="1" spreadType="center" length="247.97" shape="2002.48,-1.75 2250.45,-1.75">
        <lane id="3_0" index="0" speed="{speed_setting[0]}" length="247.97" width="3.50" acceleration="1" shape="2002.48,-7.00 2250.11,-7.00"/>
        <lane id="3_1" index="1" speed="{speed_setting[0]}" length="247.97" width="3.50" shape="2002.48,-3.50 2250.11,-3.50"/>
        <lane id="3_2" index="2" speed="{speed_setting[0]}" length="247.97" width="3.50" shape="2002.48,0.00 2250.11,0.00"/>
        <lane id="3_3" index="3" speed="{speed_setting[0]}" length="247.97" width="3.50" shape="2002.48,3.50 2250.11,3.50"/>
    </edge>
    <edge id="4" from="1" to="4-end" priority="-1" type="1" spreadType="center" length="1200.00" shape="2257.77,0.00 3250.00,0.00">
        <lane id="4_0" index="0" speed="{speed_setting[0]}" length="1200.00" width="3.50" shape="2258.11,-3.50 3250.00,-3.50"/>
        <lane id="4_1" index="1" speed="{speed_setting[0]}" length="1200.00" width="3.50" shape="2258.11,0.00 3250.00,0.00"/>
        <lane id="4_2" index="2" speed="{speed_setting[0]}" length="1200.00" width="3.50" shape="2258.11,3.50 3250.00,3.50"/>
    </edge>

    <junction id="0" type="priority" x="2000.00" y="-2.50" incLanes="2_0 1_0 1_1 1_2" intLanes=":0_0_0 :0_1_0 :0_1_1 :0_1_2" shape="2002.48,5.25 2002.48,-8.75 1999.29,-8.80 1998.18,-8.90 1997.07,-9.06 1995.73,-9.31 1993.93,-9.66 1993.27,-6.22 1995.88,-5.68 1996.64,-5.49 1997.05,-5.36 1997.09,-5.28 1996.77,-5.25 1996.77,5.25">
        <request index="0" response="0000" foes="0000" cont="0"/>
        <request index="1" response="0000" foes="0000" cont="0"/>
        <request index="2" response="0000" foes="0000" cont="0"/>
        <request index="3" response="0000" foes="0000" cont="0"/>
    </junction>
    <junction id="1" type="zipper" x="2250.00" y="-1.75" incLanes="3_0 3_1 3_2 3_3" intLanes=":1_0_0 :1_0_1 :1_0_2 :1_0_3" shape="2258.11,5.25 2258.11,-5.25 2255.07,-6.16 2253.15,-7.84 2251.92,-8.49 2250.11,-8.75 2250.11,5.25">
        <request index="0" response="0010" foes="0010" cont="0"/>
        <request index="1" response="0001" foes="0001" cont="0"/>
        <request index="2" response="0000" foes="0000" cont="0"/>
        <request index="3" response="0000" foes="0000" cont="0"/>
    </junction>
    <junction id="1-begin" type="dead_end" x="0.00" y="0.00" incLanes="" intLanes="" shape="-0.00,5.25 -0.00,-5.25"/>
    <junction id="2-begin" type="dead_end" x="1700.00" y="-65.00" incLanes="" intLanes="" shape="1699.67,-63.28 1700.33,-66.72"/>
    <junction id="4-end" type="dead_end" x="3250.00" y="0.00" incLanes="4_0 4_1 4_2" intLanes="" shape="3250.00,-5.25 3250.00,5.25"/>

    <connection from="1" to="3" fromLane="0" toLane="1" via=":0_1_0" dir="s" state="M"/>
    <connection from="1" to="3" fromLane="1" toLane="2" via=":0_1_1" dir="s" state="M"/>
    <connection from="1" to="3" fromLane="2" toLane="3" via=":0_1_2" dir="s" state="M"/>
    <connection from="2" to="3" fromLane="0" toLane="0" via=":0_0_0" dir="s" state="M"/>
    <connection from="3" to="4" fromLane="0" toLane="0" via=":1_0_0" dir="s" state="Z"/>
    <connection from="3" to="4" fromLane="1" toLane="0" keepClear="0" via=":1_0_1" dir="s" state="Z"/>
    <connection from="3" to="4" fromLane="2" toLane="1" keepClear="0" via=":1_0_2" dir="s" state="M"/>
    <connection from="3" to="4" fromLane="3" toLane="2" keepClear="0" via=":1_0_3" dir="s" state="M"/>

    <connection from=":0_0" to="3" fromLane="0" toLane="0" dir="s" state="M"/>
    <connection from=":0_1" to="3" fromLane="0" toLane="1" dir="s" state="M"/>
    <connection from=":0_1" to="3" fromLane="1" toLane="2" dir="s" state="M"/>
    <connection from=":0_1" to="3" fromLane="2" toLane="3" dir="s" state="M"/>
    <connection from=":1_0" to="4" fromLane="0" toLane="0" dir="s" state="M"/>
    <connection from=":1_0" to="4" fromLane="1" toLane="0" dir="s" state="M"/>
    <connection from=":1_0" to="4" fromLane="2" toLane="1" dir="s" state="M"/>
    <connection from=":1_0" to="4" fromLane="3" toLane="2" dir="s" state="M"/>

</net>
""", file=road_net_file)
        
def generate_roadnet_without_ramp_file_func(speed_setting):
    with open("../../deployment/environment/road_without_ramp.net.xml", "w") as road_net_file:
        print(f"""<?xml version="1.0" encoding="UTF-8"?>

<net version="1.20" junctionCornerDetail="5" limitTurnSpeed="5.50" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/net_file.xsd">

    <location netOffset="85.03,26.17" convBoundary="0.00,0.00,3250.00,0.00" origBoundary="-85.03,-26.17,270.54,-0.17" projParameter="!"/>

    <edge id=":0_0" function="internal">
        <lane id=":0_0_0" index="0" speed="{speed_setting[0]}" length="1.00" width="3.50" shape="2001.48,-3.50 2002.48,-3.50"/>
        <lane id=":0_0_1" index="1" speed="{speed_setting[0]}" length="1.00" width="3.50" shape="2001.48,0.00 2002.48,0.00"/>
        <lane id=":0_0_2" index="2" speed="{speed_setting[0]}" length="1.00" width="3.50" shape="2001.48,3.50 2002.48,3.50"/>
    </edge>
    <edge id=":1_0" function="internal">
        <lane id=":1_0_0" index="0" speed="{speed_setting[0]}" length="3.88" width="3.50" shape="2253.89,-3.50 2257.77,-3.50"/>
        <lane id=":1_0_1" index="1" speed="{speed_setting[0]}" length="3.88" width="3.50" shape="2253.89,0.00 2257.77,0.00"/>
        <lane id=":1_0_2" index="2" speed="{speed_setting[0]}" length="3.88" width="3.50" shape="2253.89,3.50 2257.77,3.50"/>
    </edge>

    <edge id="1" from="1-begin" to="0" priority="-1" type="1" spreadType="center" shape="0.00,0.00 2001.48,0.00">
        <lane id="1_0" index="0" speed="{speed_setting[0]}" length="2001.48" width="3.50" shape="-0.00,-3.50 2001.48,-3.50"/>
        <lane id="1_1" index="1" speed="{speed_setting[0]}" length="2001.48" width="3.50" shape="-0.00,0.00 2001.48,0.00"/>
        <lane id="1_2" index="2" speed="{speed_setting[0]}" length="2001.48" width="3.50" shape="-0.00,3.50 2001.48,3.50"/>
    </edge>
    <edge id="3" from="0" to="1" priority="-1" type="1" spreadType="center" length="247.97" shape="2002.48,0.00 2250.00,0.00">
        <lane id="3_0" index="0" speed="{speed_setting[0]}" length="247.97" width="3.50" acceleration="1" shape="2002.48,-3.50 2253.89,-3.50"/>
        <lane id="3_1" index="1" speed="{speed_setting[0]}" length="247.97" width="3.50" shape="2002.48,0.00 2253.89,0.00"/>
        <lane id="3_2" index="2" speed="{speed_setting[0]}" length="247.97" width="3.50" shape="2002.48,3.50 2253.89,3.50"/>
    </edge>
    <edge id="4" from="1" to="4-end" priority="-1" type="1" spreadType="center" length="1200.00" shape="2257.77,0.00 3250.00,0.00">
        <lane id="4_0" index="0" speed="{speed_setting[0]}" length="1200.00" width="3.50" shape="2257.77,-3.50 3250.00,-3.50"/>
        <lane id="4_1" index="1" speed="{speed_setting[0]}" length="1200.00" width="3.50" shape="2257.77,0.00 3250.00,0.00"/>
        <lane id="4_2" index="2" speed="{speed_setting[0]}" length="1200.00" width="3.50" shape="2257.77,3.50 3250.00,3.50"/>
    </edge>

    <junction id="0" type="priority" x="2000.00" y="0.00" incLanes="1_0 1_1 1_2" intLanes=":0_0_0 :0_0_1 :0_0_2" shape="2002.48,5.25 2002.48,-5.25 2001.48,-5.25 2001.48,5.25">
        <request index="0" response="000" foes="000" cont="0"/>
        <request index="1" response="000" foes="000" cont="0"/>
        <request index="2" response="000" foes="000" cont="0"/>
    </junction>
    <junction id="1" type="priority" x="2250.00" y="0.00" incLanes="3_0 3_1 3_2" intLanes=":1_0_0 :1_0_1 :1_0_2" shape="2257.77,5.25 2257.77,-5.25 2253.89,-5.25 2253.89,5.25">
        <request index="0" response="000" foes="000" cont="0"/>
        <request index="1" response="000" foes="000" cont="0"/>
        <request index="2" response="000" foes="000" cont="0"/>
    </junction>
    <junction id="1-begin" type="dead_end" x="0.00" y="0.00" incLanes="" intLanes="" shape="-0.00,5.25 -0.00,-5.25"/>
    <junction id="4-end" type="dead_end" x="3250.00" y="0.00" incLanes="4_0 4_1 4_2" intLanes="" shape="3250.00,-5.25 3250.00,5.25"/>

    <connection from="1" to="3" fromLane="0" toLane="0" via=":0_0_0" dir="s" state="M"/>
    <connection from="1" to="3" fromLane="1" toLane="1" via=":0_0_1" dir="s" state="M"/>
    <connection from="1" to="3" fromLane="2" toLane="2" via=":0_0_2" dir="s" state="M"/>
    <connection from="3" to="4" fromLane="0" toLane="0" via=":1_0_0" dir="s" state="M"/>
    <connection from="3" to="4" fromLane="1" toLane="1" via=":1_0_1" dir="s" state="M"/>
    <connection from="3" to="4" fromLane="2" toLane="2" via=":1_0_2" dir="s" state="M"/>

    <connection from=":0_0" to="3" fromLane="0" toLane="0" dir="s" state="M"/>
    <connection from=":0_0" to="3" fromLane="1" toLane="1" dir="s" state="M"/>
    <connection from=":0_0" to="3" fromLane="2" toLane="2" dir="s" state="M"/>
    <connection from=":1_0" to="4" fromLane="0" toLane="0" dir="s" state="M"/>
    <connection from=":1_0" to="4" fromLane="1" toLane="1" dir="s" state="M"/>
    <connection from=":1_0" to="4" fromLane="2" toLane="2" dir="s" state="M"/>

</net>
""", file=road_net_file)

# traffic file generation
def generate_routefile(multi_index_0, multi_index_1, MPR):
    # random.seed(42)
    total_vehicles_0 = 100 * multi_index_0          # Actual traffic flow on the main road
    total_vehicles_1 = 100 * multi_index_1          # Actual traffic flow on the ramp
    v_CAV_p = MPR / 100                             # Proportion of CAVs
    v_HDV_p = 1 - MPR / 100                         # Proportion of HDVs
    # Generate the number of two types of vehicles
    num_HDV_0 = int(total_vehicles_0 * v_HDV_p)     # Number of HDVs on the main road
    num_CAV_0 = int(total_vehicles_0 * v_CAV_p)     # Number of CAVs on the main road
    num_HDV_1 = int(total_vehicles_1 * v_HDV_p)     # Number of HDVs on the ramp
    num_CAV_1 = int(total_vehicles_1 * v_CAV_p)     # Number of CAVs on the ramp

    # HDV: green
    # CAV: red

    with open("../../deployment/environment/route.rou.xml", "w") as routes:
        print("""<routes>
        <vType id="HDV_ori" length="5.00" accel="1.5" decel="3.5" emergencyDecel="3.5" mingap="3.5" tau="2.0" color="127,255,0" carFollowModel="IDM"/>
        <vType id="CAV_ori" length="5.00" accel="2.6" decel="4.5" emergencyDecel="4.5" mingap="2.0" tau="1.1" color="255,0,0" carFollowModel="CACC"/>

        <route id="r_1" edges="1 3 4"/>
        <route id="r_2" edges="2 3 4"/>""", file=routes)
        
        # Generate vehicles for the main road
        print('<flow id="flow_HDV_0" begin="0" end="3600" vehsPerHour="%i" departSpeed="max" type="HDV_ori" route="r_1" departLane="random" lcKeepRight="0">' % (num_HDV_0), file=routes)
        print('</flow>', file=routes)
        print('<flow id="flow_CAV_0" begin="0" end="3600" vehsPerHour="%i" departSpeed="max" type="CAV_ori" route="r_1" departLane="random" lcKeepRight="0">' % (num_CAV_0), file=routes)
        print('</flow>', file=routes)
    
        # Generate vehicles for the ramp
        print('<flow id="flow_HDV_1" begin="0" end="3600" vehsPerHour="%i" departSpeed="max" type="HDV_ori" route="r_2" departLane="random" lcKeepRight="0">' % (num_HDV_1), file=routes)
        print('</flow>', file=routes)
        print('<flow id="flow_CAV_1" begin="0" end="3600" vehsPerHour="%i" departSpeed="max" type="CAV_ori" route="r_2" departLane="random" lcKeepRight="0">' % (num_CAV_1), file=routes)
        print('</flow>', file=routes)

        print("</routes>", file=routes)

# traffic file generation
def generate_routefile_without_ramp(multi_index_0, multi_index_1, MPR):
    # random.seed(42)
    total_vehicles_0 = 100 * multi_index_0          # Actual traffic flow on the main road
    v_CAV_p = MPR / 100                             # Proportion of CAVs
    v_HDV_p = 1 - MPR / 100                         # Proportion of HDVs
    # Generate the number of two types of vehicles
    num_HDV_0 = int(total_vehicles_0 * v_HDV_p)     # Number of HDVs on the main road
    num_CAV_0 = int(total_vehicles_0 * v_CAV_p)     # Number of CAVs on the main road

    # HDV: green
    # CAV: red

    with open("../../deployment/environment/route_without_ramp.rou.xml", "w") as routes:
        print("""<routes>
        <vType id="HDV_ori" length="5.00" accel="1.5" decel="3.5" emergencyDecel="3.5" mingap="3.5" tau="2.0" color="127,255,0" carFollowModel="IDM"/>
        <vType id="CAV_ori" length="5.00" accel="2.6" decel="4.5" emergencyDecel="4.5" mingap="2.0" tau="1.1" color="255,0,0" carFollowModel="CACC"/>

        <route id="r_1" edges="1 3 4"/>""", file=routes)
        
        # Generate vehicles for the main road
        print('<flow id="flow_HDV_0" begin="0" end="3600" vehsPerHour="%i" departSpeed="max" type="HDV_ori" route="r_1" departLane="random" lcKeepRight="0">' % (num_HDV_0), file=routes)
        print('</flow>', file=routes)
        print('<flow id="flow_CAV_0" begin="0" end="3600" vehsPerHour="%i" departSpeed="max" type="CAV_ori" route="r_1" departLane="random" lcKeepRight="0">' % (num_CAV_0), file=routes)
        print('</flow>', file=routes)

        print("</routes>", file=routes)