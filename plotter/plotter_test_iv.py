from Plotter import Plotter

plotter = Plotter('CMS', r'C:\LGAD_test')

base_input_dir = 'C:/LGAD_test'
date = '2024-03-27'
sensor_name = 'FBK_2022v1_2x2_53'

# input_data_path1 = 'C:/LGAD_test/I-V_test/2024-03-26_FBK/IV_SMU+PAU_FBK_2024-03-26_0_-300_pad2.txt'
input_data_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-300_pad1.txt'
input_data_pad2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-300_pad2.txt'

input_data_pad1_no_switch = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-300_pad1_2.txt'
input_data_pad2_no_switch = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-300_pad2_2.txt'

# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter.create_subplots(rows=1, cols=1, figsize=(10, 10))

plotter.add_input_data(input_data_pad1, label="Pad 1")
plotter.add_input_data(input_data_pad2, label="Pad 2")

plotter.draw(x_index=0, y_index=3, remove_offset=True)
plotter.get_current_axis().set_ylim(-1e-6, 1e-6)
plotter.do_get_renderer()
plotter.set_experiment_label(location=(0, 0), label='FBK T10, offset removed', fontsize=15)
plotter.write_text("Pad 1 and Pad 2")
plotter.show_legend(loc='lower right')
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.set_y_label("Current [A]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name='test_switch_v3')
