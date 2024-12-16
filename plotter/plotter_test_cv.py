from Plotter import Plotter

plotter = Plotter('CMS', r'C:\LGAD_test')

base_input_dir = 'C:/LGAD_test'
date = '2024-03-28'
sensor_name = 'FBK_53'

# input_data_path1 = 'C:/LGAD_test/I-V_test/2024-03-26_FBK/IV_SMU+PAU_FBK_2024-03-26_0_-300_pad2.txt'
input_data_pad1 = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad1.txt'
input_data_pad2 = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad2.txt'
input_data_pad3 = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad3.txt'
input_data_pad4 = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad4.txt'

input_data_pad1_no_switch = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad1_2.txt'
input_data_pad2_no_switch = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad2_2.txt'
input_data_pad3_no_switch = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad3_2.txt'
input_data_pad4_no_switch = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad4_2.txt'

# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter.create_subplots(rows=2, cols=2, figsize=(10, 10))

plotter.add_input_data(input_data_pad1_no_switch, label="Without Switch board")
plotter.add_input_data(input_data_pad2_no_switch, (0, 1), label="Without Switch board")
plotter.add_input_data(input_data_pad3_no_switch, (1, 0), label="Without Switch board")
plotter.add_input_data(input_data_pad4_no_switch, (1, 1), label="Without Switch board")

plotter.add_input_data(input_data_pad1, label="With Switch board")
plotter.add_input_data(input_data_pad2, (0, 1), label="With Switch board")
plotter.add_input_data(input_data_pad3, (1, 0), label="With Switch board")
plotter.add_input_data(input_data_pad4, (1, 1), label="With Switch board")

plotter.draw(x_index=0, y_index=1, remove_offset=False, flip_x=True, draw_half=True)
# plotter.do_get_renderer()
plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v1 56 T10', fontsize=15, pad=0.1)
plotter.write_text("Pad 1")
plotter.write_text("Pad 2", location=(0, 1))
plotter.write_text("Pad 3", location=(1, 0))
plotter.write_text("Pad 4", location=(1, 1))
plotter.show_legend(loc='lower right')
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.set_y_label("Capacitance [F]")
plotter.set_y_label("Capacitance [F]", (1,0))
plotter.set_x_label("Bias voltage [V]", (1,0))
plotter.set_x_label("Bias voltage [V]", (1,1))

plotter.save_fig(out_name='test_switch_cv_v2')
