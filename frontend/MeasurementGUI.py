import time
from frontend.LivePlotWindow import LivePlotWindow
from util import BaseThread

SMU_ID = "MODEL 2410"
PAU_ID = "MODEL 6487"
LCR_ID = "43100"


class MeasurementGUI:

    def __init__(self, line_edit_sensor_name, combo_box_col_num, combo_box_row_num,
                 line_edit_initial_voltage, line_edit_final_voltage,
                 line_edit_voltage_step, check_box_return_sweep, check_box_live_plot,
                 button_measure, label_status):

        self.combo_box_smu = None
        self.combo_box_pau = None
        self.combo_box_lcr = None

        self.line_edit_sensor_name = line_edit_sensor_name
        self.combo_box_col_num = combo_box_col_num
        self.combo_box_row_num = combo_box_row_num
        self.combo_box_col_num.addItems([f'{n}' for n in range(1, 17)])
        self.combo_box_row_num.addItems([f'{n}' for n in range(1, 17)])
        self.line_edit_initial_voltage = line_edit_initial_voltage
        self.line_edit_final_voltage = line_edit_final_voltage
        self.line_edit_voltage_step = line_edit_voltage_step
        self.check_box_return_sweep = check_box_return_sweep
        self.check_box_live_plot = check_box_live_plot
        self.button_measure = button_measure
        self.button_measure.setCheckable(True)
        self.label_status = label_status

        self.resource_map = None
        self.measurement = None
        self.w = None
        self.draw_extra_point = False

    def set_common(self, sensor_name, initial_voltage, final_voltage, voltage_step,
                   live_plot, return_sweep):

        self.set_sensor_name(sensor_name)
        self.set_initial_voltage(initial_voltage)
        self.set_final_voltage(final_voltage)
        self.set_voltage_step(voltage_step)
        self.set_live_plot(live_plot)
        self.set_return_sweep(return_sweep)

    def set_combo_box_items(self, combo_box1, combo_box2, id1, id2):

        items = [*self.resource_map.keys()]
        combo_box1.addItems(items)
        combo_box2.addItems(items)

        try:
            index1 = items.index(id1)
            index2 = items.index(id2)
            combo_box1.setCurrentIndex(index1)
            combo_box2.setCurrentIndex(index2)
        except ValueError as e:
            print("Check", e)

    def set_sensor_name(self, name):
        self.line_edit_sensor_name.setText(name)

    def set_initial_voltage(self, voltage):
        self.line_edit_initial_voltage.setText(str(voltage))

    def set_final_voltage(self, voltage):
        self.line_edit_final_voltage.setText(str(voltage))

    def set_voltage_step(self, step):
        self.line_edit_voltage_step.setText(str(step))

    def set_live_plot(self, live_plot):
        self.check_box_live_plot.setChecked(live_plot)

    def set_return_sweep(self, return_sweep):
        self.check_box_return_sweep.setChecked(return_sweep)

    def get_sensor_name(self):
        return self.line_edit_sensor_name.text()

    def get_col_number(self):
        # TODO if 'use switch number' then return switch number
        return int(self.combo_box_col_num.currentText())

    def get_row_number(self):
        return int(self.combo_box_row_num.currentText())

    def get_initial_voltage(self):
        return int(self.line_edit_initial_voltage.text())

    def get_final_voltage(self):
        return int(self.line_edit_final_voltage.text())

    def get_voltage_step(self):
        return self.line_edit_voltage_step.text()

    def get_live_plot(self):
        return self.check_box_live_plot.isChecked()

    def get_return_sweep(self):
        return self.check_box_return_sweep.isChecked()

    def init_measurement(self):
        pass

    def set_measurement_options(self):
        pass

    def update_status_label(self):
        status_str = ''
        while self.measurement.is_measurement_in_progress():
            temp_str = self.measurement.get_status_str()
            if status_str != temp_str:
                status_str = temp_str
                self.label_status.setText(status_str)
            time.sleep(0.1)
        self.label_status.setText("Measurement DONE, output path: " + self.measurement.get_out_dir())

    def measure_btn_reset(self):
        self.button_measure.setEnabled(True)
        self.button_measure.setText("Start Measurement")
        self.button_measure.setChecked(False)  # for next click to be isChecked() == True 

    def stop_measurement(self):
        self.measurement.stop_measurement()
        self.button_measure.setEnabled(False)

    def control_measurement(self):
        if self.button_measure.isChecked():

            try:
                self.init_measurement()
                self.set_measurement_options()
            except Exception as e:
                print('Something wrong in initialization process...', e)
                self.measure_btn_reset()
                return

            self.label_status.setText("Start measurement...")
            self.measurement.start_measurement()
            self.button_measure.setText("Force return sweep")

            update_thread = BaseThread(target=self.update_status_label, callback=self.measure_btn_reset)
            update_thread.start()

            if self.get_live_plot():
                self.w = LivePlotWindow(self.measurement, self.draw_extra_point)
        else:
            self.stop_measurement()
