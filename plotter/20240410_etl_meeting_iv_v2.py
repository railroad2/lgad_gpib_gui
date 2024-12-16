from Plotter import Plotter

plotter = Plotter('CMS', r'C:\LGAD_test')

base_input_dir = 'C:/LGAD_test'
date = '2024-04-08'
sensor_name = 'FBK_54_T9_step1'
initial_voltage = '0'
final_voltage = '-250'

# input_data_path1 = 'C:/LGAD_test/I-V_test/2024-03-26_FBK/IV_SMU+PAU_FBK_2024-03-26_0_-300_pad2.txt'
input_data_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad1.txt'
input_data_pad2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad2.txt'
input_data_pad3 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad3.txt'
input_data_pad4 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad4.txt'

sensor_name = 'FBK_54_T9_steo2_version1'
input_data_pad1_switch_v1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad1.txt'
input_data_pad2_switch_v1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad2.txt'
input_data_pad3_switch_v1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad3.txt'
input_data_pad4_switch_v1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad4.txt'

sensor_name = 'FBK_54_T9_step2_version2'
input_data_pad1_switch_v2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad1.txt'
input_data_pad2_switch_v2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad2.txt'
input_data_pad3_switch_v2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad3.txt'
input_data_pad4_switch_v2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-250_pad4.txt'

# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter.create_subplots(rows=2, cols=2, figsize=(10, 10))

label = "Without switch"
plotter.add_input_data(input_data_pad1, label=label, color='black')
plotter.add_input_data(input_data_pad2, (0, 1), label=label, color='black')
plotter.add_input_data(input_data_pad3, (1, 0), label=label, color='black')
plotter.add_input_data(input_data_pad4, (1, 1), label=label, color='black')

label = "Switch v1"
plotter.add_input_data(input_data_pad1_switch_v1, label=label)
plotter.add_input_data(input_data_pad2_switch_v1, (0, 1), label=label)
plotter.add_input_data(input_data_pad3_switch_v1, (1, 0), label=label)
plotter.add_input_data(input_data_pad4_switch_v1, (1, 1), label=label)

label = "Switch v2"
plotter.add_input_data(input_data_pad1_switch_v2, label=label)
plotter.add_input_data(input_data_pad2_switch_v2, (0, 1), label=label)
plotter.add_input_data(input_data_pad3_switch_v2, (1, 0), label=label)
plotter.add_input_data(input_data_pad4_switch_v2, (1, 1), label=label)

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True, flip_y=True, draw_half=True)
# plotter.set_y_lim((-0.8e-8, 1.2e-7), location=(0, 0))
plotter.set_current_axis(location=(0,0))
plotter.get_current_axis().set_yscale('log')
plotter.set_y_lim((-0.8e-8, 1.2e-8), location=(0, 1))
plotter.set_y_lim((-0.8e-8, 1.2e-8), location=(1, 0))
plotter.set_y_lim((-0.8e-8, 1.2e-8), location=(1, 1))
# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v1 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v1 54 T9', fontsize=15, pad=0.1)
plotter.write_text("Pad 1")
plotter.write_text("Pad 2", location=(0, 1))
plotter.write_text("Pad 3", location=(1, 0))
plotter.write_text("Pad 4", location=(1, 1))
plotter.show_legend(loc='lower right')
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.set_y_label("Current [A]")
plotter.set_y_label("Current [A]", (1,0))
plotter.set_x_label("Bias voltage [V]", (1,0))
# plotter.set_x_label("Bias voltage [V]", (1,1))

plotter.save_fig(out_name='20240410_iv_v2')
