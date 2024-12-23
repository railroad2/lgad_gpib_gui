import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from usbcomm_client import usbcomm
from backend.IVMeasurementBackEnd import IVMeasurementBackend

class Loop_over_switches():
    ivb = []
    swm = []

    initial_voltage = 0
    final_voltage = 100
    voltage_step = 1
    current_compliance = 1e-5
    return_sweep = True
    col_number = 1
    row_number = 1
    live_plot = True

    def __init__(self, smu_visa_resource_name, pau_visa_resource_name, sensor_name):
        self.swm_visa_resource_name = swm_visa_resource_name
        self.pau_visa_resource_name = pau_visa_resource_name
        self.sensor_name = sensor_name

        self.ivb = IVMeasurementBackend(smu_visa_resource_name, pau_visa_resource_name, sensor_name)
        self.ivb.initialize_measurement(smu_visa_resource_name, pau_visa_resource_name, sensor_name)

        ivb.set_measurement_options(self.initial_voltage, 
                                    self.final_voltage, 
                                    self.voltage_step,
                                    self.current_compliance, 
                                    self.return_sweep, 
                                    self.col_number, 
                                    self.row_number, 
                                    self.live_plot):
        self.swm = Usbcomm()
        self.pico = self.swm.findpico()
        self.swm.connect(self.pico)
        

    def set_sw_channel(self, stat, Nsw):
        data = f"{stat.upper()} {Nsw}"
        self.swm.send_data()

    def set_sw_all_off(self):
        allsw = ' '.join([str(i) for i in range(256)])
        self.swm.set_sw_channel("OFF", allsw)

    def start_measurement():
        self.swm.set_sw_all_off()
        for i in range(16):
            self.col_number = (i  % 16) + 1
            self.row_number = (i // 16) + 1
            self.swm.set_sw_channel("ON", i)
            ivb.start_measurement()
            ivb.save_results()
            self.swm.set_sw_channel("OFF", i)


def measure_IV()
    smu_name = ""
    pau_name = ""
    sen_name = ""
    loop = Loop_over_switches(smu_name, pau_name, sen_name)


if __name__=="__main__":
    measure_IV()


