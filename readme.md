### README

### **面向SUMO初学者的控制程序模板**

此模板专为SUMO（城市交通仿真）初学者设计，帮助用户快速入门基本的仿真控制与数据收集。

#### **使用方法**

要启动SUMO仿真，运行 main.py：

```
python main.py
```

#### **工作流程**

1. **参数传递与文件生成**

   main.py 首先将仿真参数传入到生成路网和流量文件的函数中，以创建所需的SUMO配置文件。

2. **启动仿真**

   文件生成完成后，main.py 会启动 run_for_main.py 中定义的 run 函数。

3. **模块化控制与数据收集**

   run 函数会调用目录下的控制和数据收集模块，以管理车辆行为并收集仿真数据。

------

### **Template for Beginners**

This template is designed for beginners working with SUMO (Simulation of Urban MObility) to help them get started with basic simulation control and data collection.

#### **Usage**

To start the SUMO simulation, simply run main.py:

```
python main.py
```

#### **How It Works**

1. **Parameter Passing and File Generation**

   main.py first passes simulation parameters to functions responsible for generating network and traffic files. This step creates the necessary SUMO configuration files.

2. **Running the Simulation**

   Once the files are generated, main.py initiates the run function from run_for_main.py.

3. **Modular Control and Data Collection**

   The run function utilizes control and data collection modules located in its directory to manage vehicle behavior and gather simulation data.

