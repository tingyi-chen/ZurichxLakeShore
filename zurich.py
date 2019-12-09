import zhinst.ziPython as zp
import zhinst.utils as zu
import time
import pandas as pd
import math
import statistics
from pymeasure.instruments.lakeshore.lakeshore331 import LakeShore331

class Zurich():
    '''1. 多一個 self，是使用自己的類別中的變數，而不是外部變數
    2. 外部變數沒有 self，內部變數有 self。
    3. 可以確保不要人用不同的 self 卻得到相同的回傳值。
    4. 簡單一點說，一個變數需要被跨函數存取，就加 self，如果只是在一個函數內被用到，就不要加 self。
    5. zurich.py 的 self 就是 Zurich() 本身
    '''

    def __init__(self, device_id, channel):
        self.device = device_id
        discov = zp.ziDiscovery()
        self.props = discov.get(discov.find(self.device))
        self.daq = zp.ziDAQServer(self.props['serveraddress'], self.props['serverport'], self.props['apilevel'])
        self.channel = str(channel)

        # self.lk = LakeShore331("GPIB0::12::INSTR")

        self.data_dict = {}
        self.count = 0
        self.device_name = 'Default'
        self.acCoupling_ZI = 1
        self.imp50 = 0
        self.diff = 0
        self.TAgain = 1000
        self.setTAdccouplingNo()
        self.tempStart = 300
        self.tempStop = 310
        self.tempStep = 10
        self.vdcStart = 0.1
        self.vdcStop = 0.2
        self.vdcStep = 0.1
        self.vacStart = 0.1
        self.vacStop = 0.4
        self.vacStep = 0.1
        self.fStart = 100
        self.fStop = 10000
        self.fSampleCount = 21
        self.tdaffLogrithmicPlotting = 1
        
    '''Basic Settings'''
    '''Parameters related to signal out'''
    def setDeviceName(self, device_name):
        self.device_name = device_name

    def sigouts(self, out_node):
        self.daq.set(out_node)

    def sigoutsOn(self):
        out_node = [['/'+ self.device+ '/sigouts/'+ self.channel+ '/on', 1]]
        self.daq.set(out_node)

    def sigoutsOff(self):
        out_node = [['/'+ self.device+ '/sigouts/'+ self.channel+ '/on', 0]]
        self.daq.set(out_node)

    def setVoutRange(self, voutRange):
        self.voutRange = float(voutRange)
        out_node = [['/'+ self.device+ '/sigouts/'+ self.channel+ '/range', self.voutRange]]
        self.sigouts(out_node)

    def setVoutACoutput(self, voutACoutput):
        self.voutACoutput = voutACoutput
        out_node = [['/'+ self.device+ '/sigouts/'+ self.channel+ '/amplitudes/6', self.voutACoutput]]
        self.sigouts(out_node)

    def setVoutDCoffset(self, voutDCoffset):
        self.voutDCoffset = voutDCoffset
        out_node = [['/'+ self.device+ '/sigouts/'+ self.channel+ '/offset', self.voutDCoffset]]
        self.sigouts(out_node)

    '''Parameters related to signal in'''
    def sigins(self, in_node):
        self.daq.set(in_node)

    def setVinRange(self, vinRange):
        self.vinRange = vinRange
        in_node = [['/'+ self.device+ '/sigins/'+ self.channel+ '/range', self.vinRange]]
        self.sigins(in_node)

    def setDiffYes(self):
        self.diff = 1
        in_node = [['/'+ self.device+ '/sigins/'+ self.channel+ '/diff', self.diff]]
        self.sigins(in_node)

    def setDiffNo(self):
        self.diff = 0
        in_node = [['/'+ self.device+ '/sigins/'+ self.channel+ '/diff', self.diff]]
        self.sigins(in_node)

    def setImp50Yes(self):
        self.imp50 = 1
        in_node = [['/'+ self.device+ '/sigins/'+ self.channel+ '/imp50', self.imp50]]
        self.sigins(in_node)

    def setImp50No(self):
        self.imp50 = 0
        in_node =[['/'+ self.device+ '/sigins/'+ self.channel+ '/imp50', self.imp50]]
        self.sigins(in_node)

    def setACCouplingYes_ZI(self):
        self.acCoupling_ZI = 1
        in_node = [['/'+ self.device+ '/sigins/'+ self.channel+ '/ac', self.acCoupling_ZI]]
        self.sigins(in_node)

    def setACCouplingNo_ZI(self):
        self.acCoupling_ZI = 0
        in_node = [['/'+ self.device+ '/sigins/'+ self.channel+ '/ac', self.acCoupling_ZI]]
        self.sigins(in_node)

    '''Parameters related to oscillators'''
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

    def setDemodsADCSelect(self, adcselect):
        demods_node = [['/'+ self.device+ '/demods/'+ self.channel+ '/adcselect', adcselect]]
        self.demods(demods_node)
    
    def setDemodsOrder(self, order):
        demods_node = [['/'+ self.device+ '/demods/'+ self.channel+ '/order', order]]
        self.demods(demods_node)
        
    def setDemodsTC(self, tc):
        demods_node = [['/'+ self.device+ '/demods/'+ self.channel+ '/timeconstant', tc]]
        self.demods(demods_node)

    def setDemodsRate(self, rate):
        demods_node = [['/'+ self.device+ '/demods/'+ self.channel+ '/rate', 10e3]]
        self.demods(demods_node)

    def demods(self, demods_node):
        self.daq.set(demods_node)

    '''Parameters related to Transimpedance Amplifier
    1. 控制轉阻放大器。
    2. dccoupling = 0 代表此放大器處使用 AC coupling模式。
    '''
    def setGain(self, TAgain):
        self.TAgain = float(TAgain)
        tamp_node = [['/'+ self.device+ '/zctrls/'+ self.channel+ '/tamp/0/currentgain', self.TAgain]]
        self.tamp(tamp_node)

    def setTAdccouplingYes(self):
        tamp_node = [['/'+ self.device+ '/zctrls/'+ self.channel+ '/tamp/0/dc', 1]]
        self.tamp(tamp_node)
    
    def setTAdccouplingNo(self):
        tamp_node = [['/'+ self.device+ '/zctrls/'+ self.channel+ '/tamp/0/dc', 0]]
        self.tamp(tamp_node)

    def tamp(self, tamp_node):
        self.daq.set(tamp_node)

    '''freq_sweeper:
    1. 此函數之功能為掃描頻率，以對數軸紀錄頻率範圍，並且需搭配 data_prcs 以及 save 函數。
    2. 此函數需輸入 (1) 起始頻率 (2) 結束頻率 (3) 中間分隔成幾個點 (4) 掃幾次
    '''
    def freqSweeper(self, Start, Stop, SampleCount, LogrithmicPlotting):  
        sweeper = self.daq.sweep()
        sweeper.trigger()
        sweep_nodes = [
            ['device', self.device],
            ['gridnode', 'oscs/'+ self.channel+ '/freq'],
            ['start', Start],
            ['stop', Stop],
            ['samplecount', SampleCount],
            ['historylength', 100],
            ['xmapping', LogrithmicPlotting],
            ['bandwidthcontrol', 2],
            ['bandwidthoverlap', 0],
            ['scan', 0],
            ['loopcount', 1],
            ['settling/time', 0],
            ['settling/inaccuracy', 0.001],
            ['averaging/tc', 10],
            ['averaging/sample', 10],
        ]
        sweeper.set(sweep_nodes)

        num_path = ('/'+ self.device+ '/demods/'+ self.channel+ '/sample')
        sweeper.subscribe(num_path)

        sweeper.execute()
    
        start = time.time()
        timeout = 60
    
        while not sweeper.finished():
            if (time.time() - start) > timeout:
                sweeper.finish()
            continue

        data = sweeper.read(True)
        # f = data['dev1521']['demods']['0']['sample'][0][0]['frequency']
        f = data['/dev1521/demods/0/sample'][0][0]['frequency']
        demodX = data['/dev1521/demods/0/sample'][0][0]['x']
        demodY = data['/dev1521/demods/0/sample'][0][0]['y']
        demodR = data['/dev1521/demods/0/sample'][0][0]['r']
        demodphase = data['/dev1521/demods/0/sample'][0][0]['phase']
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

        sweeper.unsubscribe(num_path)

        return demod_dict

    '''存檔，量測到的資料會存在 C_ + "temp*100" + K + "num" + T_SAC.txt。
    配合 C_CFG.txt 一起丟到 igor 跑圖。
    '''
    def save(self, device_name, data_frame, count, temp):
        csvfile = data_frame.to_csv(device_name + "_" + str(int(temp*100)) + "K" + str(count) + "T_SAC.txt", sep='\t', index=False)

        return csvfile
    
    def saveCFG(self, device_name, fStart, fStop, fSampleCount, vdcStart, vdcStop, vdcStep, vacStart, vacStop, vacStep, tStart, tStop, tStep):
        cfg_dict = {
            device_name: '0',
            'A_E': [0.474, 12.000, 0.000],
            'T': [tStart, tStop, tStep],
            'f_as': [fStart, fStop, fSampleCount],
            'Vdc': [vdcStart, vdcStop, vdcStep],
            'Vac': [vacStart, vacStop, vacStep],
            'Vjv': [-1.500, 1.200, 0.050]
        }
        cfg_frame = pd.DataFrame.from_dict(cfg_dict, orient="index")
        cfg_csv = cfg_frame.to_csv(device_name + "_CFG.txt", sep='\t', index=False)

        return cfg_csv

    '''1. 處理資料遺失的狀況。
    2. 若資料的值為 NaN，用 0 取代掉該資料
    '''
    def md_handling(self, mdh_frame):
        for col in mdh_frame:
            if pd.isna(mdh_frame[col]) == True:
                mdh_frame.fillna(0)

        return mdh_frame
    
    '''1. 傳入「字典」形式之資料，轉成表格輸出。
    2. 若傳入新資料，則在表格右方新增欄位。
    3. 若傳入資料之欄位名稱重複，則不予新增新欄位。
    '''
    def dataPrcs(self, demod_dict, vac, vdc, count, temp):
        freq = demod_dict['f']
        Gp = demod_dict['conductance']
        Cp = demod_dict['susceptance/omega']
        Gp_name = ("Gp" + str(int(temp*100)) + "K" + str(count) + "T" + str(int(vdc*1000)) + "dc" + str(int(vac*1000)) + "ac")
        Cp_name = ("Cp" + str(int(temp*100)) + "K" + str(count) + "T" + str(int(vdc*1000)) + "dc" + str(int(vac*1000)) + "ac")

        if 'f' not in self.data_dict:
            self.data_dict = {
                'f': freq,
                Gp_name: Gp,
                Cp_name: Cp
                }
            self.data_frame = pd.DataFrame(self.data_dict)
        elif 'f' in self.data_dict:
            self.data_frame[Gp_name] = Gp
            self.data_frame[Cp_name] = Cp
        
        return self.data_frame

    '''Beneath are the parameters used in T/DC/AC/F Sweeper, called by gui.py and executed by mainwindow.ui'''
    def setDeviceName(self, device_name):
        self.device_name = device_name

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
        self.tdaffLogrithmicPlotting = 1

    def setLogrithmicplottingNo(self):
        self.tdaffLogrithmicPlotting = 0

    def Start(self):
        self.tdafSweeper(self.device_name, self.tempStart, self.tempStop, self.tempStep, self.vdcStart, self.vdcStop, self.vdcStep, self.vacStart, self.vacStop, self.vacStep, self.fStart, self.fStop, self.fSampleCount, self.tdaffLogrithmicPlotting)
    '''END of T/DC/AC/F Sweeper Parameter-Settings'''

    def tdafSweeper(self, device_name, tempStart, tempStop, tempStep, vdcStart, vdcStop, vdcStep, vacStart, vacStop, vacStep, fStart, fStop, fSampleCount, tdaffLogrithmicPlotting):
        tempStart = int(tempStart)
        tempStop = int(tempStop+1)
        tempStep = int(tempStep)
        vdcStart = int(vdcStart*10)
        vdcStop = int(vdcStop*10+1)
        vdcStep = int(vdcStep*10)
        vacStart = int(vacStart*10)
        vacStop = int(vacStop*10+1)
        vacStep = int(vacStep*10)
        
        # print(self.lk.temperature_A)

        # for temp in range(tempStart, tempStop, tempStep):
        #     self.lk.setpoint_1 = temp
        #     self.lk.heater_range = 'high'
        #     self.lk.wait_for_temperature()

        #     self.sigoutsOn()

        for vdc in range(vdcStart, vdcStop, vdcStep):
            vdc = vdc/10
            self.setVoutDCoffset(vdc)
            for vac in range(vacStart, vacStop, vacStep):
                vac = vac/10
                self.setVoutACoutput(vac)
                step_dict = self.freqSweeper(fStart, fStop ,fSampleCount, tdaffLogrithmicPlotting)
                tdaf_frame = self.dataPrcs(step_dict, vac, vdc, self.count, temp=300)
                print(tdaf_frame)

        self.sigoutsOff()

        self.save(device_name, tdaf_frame, self.count, temp=300)
        self.count = self.count + 1
        self.data_dict = {}
        
        self.saveCFG(device_name, fStart, fStop, fSampleCount, vdcStart, vdcStop, vdcStep, vacStart, vacStop, vacStep, tStart=300, tStop=310, tStep=10)

        return tdaf_frame