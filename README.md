# Zurich HF2LI x LakeShore 335 Python Program
This manual introduces how to provide DC voltage offset, AC voltage source and frequency sweeping with desired temperature environment.
## Before Execution
1. Before execution, please check that the host PC is connected to LakeShore 335 and Zurich HF2LI, so the code will run suscessfully.
2. Please modify the device name of **HF2LI** and **335 GPIB Serial** in the source code of each `.py` file manually.
3. For **HF2LI** I use `'dev1521'`, and for **335 GPIB Serial** I use `'GPIB0::12::INSTR'`, please checkout these two strings to make your own device work.
## Execution

1. Enter `python3 launch.py` in the command line to run the program.
2. There will be an **interface showing parameters related to the sweeping**.
## Interface Explaination
1. Input the **DeviceName** for the device to be tested.
1. **Start** is the initial value of the parameter to execute sweeping.
2. **Stop** is the final value of the parameter to execute sweeping.
3. **Step** is the value changed of the parameter of each step.
4. **T Current** is the indicator of current temperature.
5. Press **Confirm** if all inputs are correct, which disables all input boxes.
6. Press **Start** to execute sweeping. (This program will run loops and save the measured data automatically in the folder where `manager.py` is)
## Advanced Settings
1. **Advanced Settings** button is at the upper right corner of the interface.
## Code Explaination
1. `launch.py` is the main `.py` file to execute the whole application.
1. `home.py`, `set_xx.py` and `sets.py` are all codes for the interfaces and relates to **instruments**.
3. `manager.py` manages **switches between different windows**.
4. `zurich.py` is the source code to control LakeShore 335 to change the temperature and to execute HF2LI to sweep.
5. Folder `/ui` relates to UI files and corresponding UI codes created by QtCreator.
## About/Contact me
I'm not a professional developer and not being trained with CSIE courses, so there may be some syntax difficult to understand or errors while running.
**Please contact tingyi.chen0825@gmail.com if there are problems.**