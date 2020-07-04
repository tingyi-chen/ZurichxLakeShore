import zhinst.ziPython as zp
import zhinst.utils as zu
import time
import pandas as pd
import math
import statistics
from pymeasure.instruments.lakeshore.lakeshore331 import LakeShore331
import threading
import sys

class Zurich():
    ''' This Zurich() Class provides the connecting bridge between HF2LI, LakeShore and PC.'''

    def __init__(self):
        ''' First, __init__() creates an API to communicate with HF2LI with the device ID (ex.'dev1521') 
            and the channel that used for input, output, demodulators and others.
            Second, __init__() also makes a connection to LakeShore335 via GPIB/USB cable, which provided
            by National Instruments.
            Last, __init__() initializes the global parameters that used for sweeping if the user does 
            not assign a value.
        '''
        self.device = 'dev1521'
        discov = zp.ziDiscovery()
        self.props = discov.get(discov.find(self.device))
        self.daq = zp.ziDAQServer(self.props['serveraddress'], self.props['serverport'], self.props['apilevel'])


        self.device_name = 'Default'
        self.tempStart = 300
        self.tempStop = 300
        self.tempStep = 5
        self.vdcStart = 0
        self.vdcStop = 0
        self.vdcStep = 0.1
        self.vacStart = 0.1
        self.vacStop = 0.1
        self.vacStep = 0.1
        self.fStart = 1700000
        self.fStop = 1844000
        self.fSampleCount = 101
        self.LogrithmicPlotting = 1
        self.channel = str(0)
        self.TAgain = 1000
        self.setOutChannel(0)
        self.setDemodChannel(0)
        self.adcselect = 0
        self.order = 4
        self.rate = 225
        self.tc = 10.16

        try:
            self.setACCouplingYes_ZI()
            self.setImp50No()
            self.setDiffNo()
        except RuntimeError:
            print('HF2LI undiscoveralbe.')
            sys.exit()

        try:
            self.tamp_bool = self.daq.getInt('/'+ self.device+ '/zctrls/0/tamp/available')
        except RuntimeError:
            print('Please connect to a transimpedance amplifier.')
            sys.exit()
        
        self.count = 0

    ''' Here are basic I/O parameters that must be in this form because they are called by PyQt's .connect(function)
        method to make them connected to boxes, buttons, ... of the graphic user interface.'''
    def setDeviceName(self, device_name):
        self.device_name = device_name

    ''' Parameters related to signal out'''
    def sigouts(self, out_node):
        self.daq.set(out_node)

    def setOutChannel(self, channel):
        self.out_channel = str(channel)

    def setVoutRange(self, voutRange):
        self.voutRange = float(voutRange)
        out_node = [['/'+ self.device+ '/sigouts/'+ self.out_channel+ '/range', self.voutRange]]
        self.sigouts(out_node)
        
    def sigoutsOff(self):
        out_node = [['/'+ self.device+ '/sigouts/0/on', 0]]
        self.daq.set(out_node)

    def sigoutsOn(self):
        out_node = [['/'+ self.device+ '/sigouts/0/on', 1]]
        self.daq.set(out_node)

    def setVoutACoutput(self, voutACoutput):
        self.voutACoutput = voutACoutput
        out_node = [['/'+ self.device+ '/sigouts/0/amplitudes/6', self.voutACoutput]]
        self.daq.set(out_node)
        
    def setVoutDCoffset(self, voutDCoffset):
        self.voutDCoffset = voutDCoffset
        out_node = [['/'+ self.device+ '/sigouts/0/offset', self.voutDCoffset]]
        self.daq.set(out_node)


    ''' Parameters related to signal in '''
    def sigins(self, in_node):
        self.daq.set(in_node)

        

    def setVinRange(self, vinRange):
        in_node = [['/'+ self.device+ '/sigins/0/range', vinRange]]
        self.sigins(in_node)

    def setDiffYes(self):
        self.diff = 1
        in_node = [['/'+ self.device+ '/sigins/0/diff', self.diff]]
        self.sigins(in_node)

    def setDiffNo(self):
        self.diff = 0
        in_node = [['/'+ self.device+ '/sigins/0/diff', self.diff]]
        self.sigins(in_node)

    def setImp50Yes(self):
        self.imp50 = 1
        in_node = [['/'+ self.device+ '/sigins/0/imp50', self.imp50]]
        self.sigins(in_node)

    def setImp50No(self):
        self.imp50 = 0
        in_node =[['/'+ self.device+ '/sigins/0/imp50', self.imp50]]
        self.sigins(in_node)

    def setACCouplingYes_ZI(self):
        self.acCoupling_ZI = 1
        in_node = [['/'+ self.device+ '/sigins/0/ac', self.acCoupling_ZI]]
        self.sigins(in_node)

    def setACCouplingNo_ZI(self):
        self.acCoupling_ZI = 0
        in_node = [['/'+ self.device+ '/sigins/0/ac', self.acCoupling_ZI]]
        self.sigins(in_node)

    ''' Parameters related to oscillators'''
    def oscs(self, oscs_node):
        self.daq.setDouble(oscs_node[0], oscs_node[1])

    def setOscsFrequency1(self, oscsFrequency1):
        self.oscsFrequency1 = oscsFrequency1
        oscs_node = ['/'+ self.device+ '/oscs/0/freq', self.oscsFrequency1]
        self.oscs(oscs_node)

    def setOscsFrequency2(self, oscsFrequency2):
        self.oscsFrequency2 = oscsFrequency2
        oscs_node = ['/'+ self.device+ '/oscs/1/freq', self.oscsFrequency2]
        self.oscs(oscs_node)

    def setDemodChannel(self, channel):
        self.demods_channel = str(channel)

    def setDemodsADCSelect(self, adcselect):
        self.adcselect = adcselect
        demods_node = [['/'+ self.device+ '/demods/'+ self.demods_channel+ '/adcselect', self.adcselect]]
        self.demods(demods_node)

    def setDemodsOrder(self, order):
        self.order = order
        demods_node = [['/'+ self.device+ '/demods/'+ self.demods_channel+ '/order', self.order]]
        self.demods(demods_node)
        
    def setDemodsTC(self, tc):
        self.tc = tc
        demods_node = [['/'+ self.device+ '/demods/'+ self.demods_channel+ '/timeconstant', self.tc/1000]]
        self.demods(demods_node)

    def setDemodsRate(self, rate):
        self.rate = rate
        demods_node = [['/'+ self.device+ '/demods/'+ self.demods_channel+ '/rate', self.rate]]
        self.demods(demods_node)

    def demods(self, demods_node):
        self.daq.set(demods_node)

    ''' Parameters related to Transimpedance Amplifier
        setTAdccouplingNo() represents that TA is in the AC Coupling mode.
    '''
    def setGain(self, TAgain):
        self.TAgain = float(TAgain)
        tamp_node = [['/'+ self.device+ '/zctrls/0/tamp/0/currentgain', self.TAgain]]
        self.tamp(tamp_node)

    def setTAdccouplingYes(self):
        tamp_node = [['/'+ self.device+ '/zctrls/0/tamp/0/dc', 1]]
        self.tamp(tamp_node)

    def setTAdccouplingNo(self):
        tamp_node = [['/'+ self.device+ '/zctrls/0/tamp/0/dc', 0]]
        self.tamp(tamp_node)

    def tamp(self, tamp_node):
        self.daq.set(tamp_node)
        
    ''' Beneath are the parameters used in T/DC/AC/F Sweeper '''
    def setTempMin(self, tempStart):
        self.tempStart = tempStart

    def setTempMax(self, tempStop):
        self.tempStop = tempStop

    def setTempStep(self, tempStep):
        self.tempStep = tempStep

    def setVdcMin(self, vdcStart):
        self.vdcStart = vdcStart

    def setVdcMax(self, vdcStop):
        self.vdcStop = vdcStop

    def setVdcStep(self, vdcStep):
        self.vdcStep = vdcStep

    def setVacMin(self, vacStart):
        self.vacStart = vacStart

    def setVacMax(self, vacStop):
        self.vacStop = vacStop

    def setVacStep(self, vacStep):
        self.vacStep = vacStep

    def setFreqMin(self, fStart):
        self.fStart = fStart

    def setFreqMax(self, fStop):
        self.fStop = fStop
        
    def setSamplecount(self, fSampleCount):
        self.fSampleCount = fSampleCount

    def setLogrithmicplottingYes(self):
        self.LogrithmicPlotting = 1

    def setLogrithmicplottingNo(self):
        self.LogrithmicPlotting = 0

    ''' END of T/DC/AC/F Sweeper Parameter-Settings'''
    def freqSweeper(self):
        ''' freq_sweeper() is used to obtain the frequency response of a device within a frequency range.
            If the user is calling this function, it should be noted that freq_sweeper() returns a dicti-
            onary-like object.
            Please also call dataPrcs() to transfer this dictionary-like data to a frame-like data, and
            call save() to save the transfered file into .csv.
        '''
        sweeper = self.daq.sweep()
        sweeper.trigger()
        sweep_nodes = [
            ['device', self.device],
            ['gridnode', 'oscs/'+ self.channel+ '/freq'],
            ['start', self.fStart],
            ['stop', self.fStop],
            ['samplecount', self.fSampleCount],
            ['historylength', 100],
            ['xmapping', self.LogrithmicPlotting],
            ['bandwidthcontrol', 2],
            ['bandwidthoverlap', 1],
            ['bandwidth', 100],
            ['maxbandwidth', 100],
            ['scan', 0],
            ['loopcount', 1],
            ['settling/time', 0.01],
            ['settling/inaccuracy', 0.0001],
            ['averaging/tc', 15],
            ['averaging/sample', 20],
            ['averaging/time', 0.02],
            ['order', 8],
            ['omegasuppression', 40],
            ['sincfilter', 0]
        ]
        sweeper.set(sweep_nodes)

        num_path = ('/'+ self.device+ '/demods/0/sample')
        # noise_path = ('/'+ self.device+ '/demods/3/sample')

        sweeper.subscribe(num_path)
        # sweeper.subscribe(noise_path)

        sweeper.execute()
    
        start = time.time()
        timeout = 900
        
        while not sweeper.finished():
            if (time.time() - start) > timeout:
                sweeper.finish()
                continue

        data = sweeper.read(True)
        # print(data)
        # f = data['dev1521']['demods']['0']['sample'][0][0]['frequency']
        for channel in range (0, 4, 3):
            f = data['/'+ self.device+ '/demods/'+ str(self.channel)+ '/sample'][0][0]['frequency']
            demodX = data['/'+ self.device+ '/demods/'+ str(self.channel)+ '/sample'][0][0]['x']
            demodY = data['/'+ self.device+ '/demods/'+ str(self.channel)+ '/sample'][0][0]['y']
            demodR = data['/'+ self.device+ '/demods/'+ str(self.channel)+ '/sample'][0][0]['r']
            demodphase = data['/'+ self.device+ '/demods/'+ str(self.channel)+ '/sample'][0][0]['phase']
            scopeX = abs(demodX * pow(2, 1/2))
            scopeY = abs(demodY * pow(2, 1/2))
            scopeV = pow((pow(scopeX, 2) + pow(scopeY, 2)), 1/2)

            slope = statistics.mean(scopeY) / statistics.mean(scopeX)
            theta = math.atan(slope)
            Z = self.TAgain * self.voutACoutput / scopeV
            R = Z * math.cos(theta)
            X = Z * math.sin(theta)
            Capacitance =  1 / (Z * 2 * math.pi * f)
            G = R / (pow(Z, 2))
            B = X / (pow(Z, 2))
            Capacitance2 = B / (2 * math.pi * f)
            theta2 = math.atan(statistics.mean(B)/statistics.mean(G))
            print("Z", Z, "R", R, "X", X, "G", G, "B", B, sep = '\n')
            scopeR = demodR * pow(2, 1/2)
            phase = -demodphase


            demod_dict = {
                'f': f,
                'conductance': G,
                'susceptance/omega': Capacitance2,
                'r': scopeR,
                'phase': theta2
            }
            # elif channel == 3:
            #     noise_dict = {
            #         'f': f,
            #         'conductance': G,
            #         'susceptance/omega': Capacitance2,
            #         'r': scopeR,
            #         'phase': theta2
            #     }

        sweeper.unsubscribe(num_path)
        # sweeper.unsubscribe(noise_path)
        return demod_dict

    def save(self, data_frame, count, temp):
        csvfile = data_frame.to_csv(self.device_name + "_" + str(int(temp*100)) + "K" + str(count) + "T_SAC.txt", sep='\t', index=False)
        
        return csvfile
    
    def saveCFG(self, vdcCount, vacCount):
        if self.vdcStart == 0 or self.vacStart == 0:
            cfg_dict = {
                self.device_name: '0',
                'A_E': [0.474, 12.000, 0.000],
                'T': [self.tempStart, self.tempStop, self.tempStep],
                'f_as': [self.fStart, self.fStop, self.fSampleCount],
                'Vdc': [self.vdcStart/10, self.vdcStop/10, vdcCount],
                'Vac': [self.vacStart/10, self.vacStop/10, vacCount],
                'Vjv': [-1.500, 1.200, 0.050]
            }
        else:
            cfg_dict = {
                self.device_name: '0',
                'A_E': [0.474, 12.000, 0.000],
                'T': [self.tempStart, self.tempStop, self.tempStep],
                'f_as': [self.fStart, self.fStop, self.fSampleCount],
                'Vdc': [self.vdcStart/10, self.vdcStop/10, int(self.vdcStop/self.vdcStart)],
                'Vac': [self.vacStart/10, self.vacStop/10, int(self.vacStop/self.vacStart)],
                'Vjv': [-1.500, 1.200, 0.050]
            }
        cfg_frame = pd.DataFrame(cfg_dict).T
        cfg_csv = cfg_frame.to_csv(self.device_name + "_CFG.txt", sep='\t', header=False)

        return cfg_csv

    def md_handling(self, mdh_frame):
        ''' Handle the situation of missing datas, if the value is NaN, then use 0 instead. '''
        for col in mdh_frame:
            if pd.isna(mdh_frame[col]) == True:
                mdh_frame.fillna(0)

        return mdh_frame
    
    def dataPrcs(self, dict, data_dict, data_frame, vac, vdc, count, temp):
        freq = dict['f']
        Gp = dict['conductance']
        Cp = dict['susceptance/omega']
        r = dict['r']
        Gp_name = ("Gp" + str(int(temp*100)) + "K" + str(count) + "T" + str(int(vdc*1000)) + "dc" + str(int(vac*1000)) + "ac")
        Cp_name = ("Cp" + str(int(temp*100)) + "K" + str(count) + "T" + str(int(vdc*1000)) + "dc" + str(int(vac*1000)) + "ac")
        r_name = "r"
        if 'f' not in data_dict:
            data_dict = {
                'f': freq,
                Gp_name: Gp,
                Cp_name: Cp,
                r_name: r
                }
            data_frame = pd.DataFrame(data_dict)
        elif 'f' in data_dict:
            data_frame[Gp_name] = Gp
            data_frame[Cp_name] = Cp
            data_frame[r_name] = r
        return data_frame, data_dict

    def Start(self):
        self.tdafSweeper()

    def StartThread(self):
        self.t1 = threading.Thread(target=self.Start)
        self.t1.daemon = True
        self.t1.start()

    def Stop(self):
        self.sigoutsOff()
        sys.exit()

    def tdafSweeper(self):
        ''' tdafSweeper() is the main function of class Zurich(), Zurich() is programmed to sweep "temperature",
            "DC volate source", "AC voltage source" and "frequency" to measure the response of the device to be
            tested with each parameter.
        '''
        self.daq.set([['/dev1521/demods/3/enable', 1]])
        self.daq.set([['/dev1521/demods/3/oscselect', 0]])

        vdcCount = 0
        vacCount = 0
        data_dict = {}
        tdaf_frame = pd.DataFrame(data_dict)
        # noise_frame = pd.DataFrame(self.noise_data_dict)

        for temp in range(self.tempStart, self.tempStop+ 1, self.tempStep):
            # self.lk.setpoint_1 = temp
            # time.sleep(0.2)
            # self.lk.heater_range = 'high'
            # lk.wait_for_temperature(0.5, 0.1, 'A', 1, 900, 5)

            self.sigoutsOn()

            for vdc in range(int(self.vdcStart*10), int(self.vdcStop*10+ 1), int(self.vdcStep*10)):
                vdcCount = vdcCount+ 1
                vdc = vdc/10
                self.setVoutDCoffset(vdc)
                for vac in range(int(self.vacStart*10), int(self.vacStop*10+ 1), int(self.vacStep*10)):
                    vacCount = vacCount+ 1
                    vac = vac/10
                    self.setVoutACoutput(vac)
                    step_dict = self.freqSweeper()
                    tdaf_frame, data_dict = self.dataPrcs(step_dict, data_dict, tdaf_frame, vac, vdc, self.count, temp)
                    # noise_frame, noise_data_dict = self.dataPrcs(noise_dict, noise_data_dict, noise_frame, vac, vdc, self.count, temp)
                    # print(tdaf_frame)
                    # print(noise_frame)
            self.save(tdaf_frame, self.count, temp)
            # self.save('NOISE', noise_frame, self.count, temp)
            self.count = self.count + 1
        
            data_dict = {}
            # noise_data_dict = {}
            tdaf_frame = pd.DataFrame(data_dict)
            # noise_frame = pd.DataFrame(noise_data_dict)
            self.sigoutsOff()

        # self.lk.disable_heater()
        self.saveCFG(vdcCount, vacCount)

        return tdaf_frame