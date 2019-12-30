# Zurich HF2LI x LakeShore 335 Python Program
This manual introduces how to deal with this program with Zurich HF2LI Lock-In Amplifier and LakeShore 335 Temperature Controller.
## Feature
1. Provide **DC offset**, **AC output** and **frequency sweeping** at desired temperature environments with just **one click**.
2. Customized **voltage I/O** and **demodulator** settings.
3. Automatic **file save** function.
## Before Execution
1. Please check that the host PC is connected to LakeShore 335 and Zurich HF2LI, so the code will run suscessfully.
2. Please modify the device name of **HF2LI** and **335 GPIB Serial** in the source code of each `.py` file manually.
3. For **HF2LI** I use `'dev1521'`, and for **335 GPIB Serial** I use `'GPIB0::12::INSTR'`, please checkout these two strings to make your own device work.
4. For **Temperature Controlling**, please modify the source code of `LakeShore331` class of `pymeasure.instruments.Lakeshore331` manually to change the acceptable accuracy about the desired setpoint from % to an absolute value, i.e from 0.5% to 0.5K.
## Execution
1. Enter `python3 launch.py` in the command line to run the program.
2. There will be an **interface showing parameters related to the sweeping**.
## Interface Explaination
1. Input the **DeviceName** for the device to be tested.
1. **Start** is the initial value of the parameter to execute sweeping.
2. **Stop** is the final value of the parameter to execute sweeping.
3. **Step** is the value changed of the parameter of each step.
4. **T Current** is the indicator of current temperature.
5. Press **Start** to execute sweeping, which blocks the whole program.
## Advanced Settings
1. **Advanced Settings** button is at the upper right corner of the interface.
## Code Explaination
1. `launch.py` is the main `.py` file to execute the whole application.
1. `home.py`, `set_xx.py` and `sets.py` are all codes for the interfaces and relates to **instruments**.
3. `manager.py` manages **switches between different windows**.
4. `zurich.py` is the source code to control LakeShore 335 to change the temperature and to execute HF2LI to sweep.
5. Folder `/ui` relates to UI files and corresponding UI codes created by **QtCreator**.
## Contact me
Since I'm not a professional developer and not being trained with CSIE courses, there may be some syntax difficult to understand or errors while running.
**Please contact tingyi.chen0825@gmail.com if there are problems.**
## Reference & Documents
[Zurich HF2LI User Manual](https://www.zhinst.com/sites/default/files/ziHF2_UserManual_LabOne_64000.pdf)
[Zurich HF2LI Python Program Manual](https://www.zhinst.com/sites/default/files/LabOneProgrammingManual_64000.pdf)
[LakeShore331 Python Open Source Code](https://pymeasure.readthedocs.io/en/latest/api/instruments/lakeshore/lakeshore331.html)