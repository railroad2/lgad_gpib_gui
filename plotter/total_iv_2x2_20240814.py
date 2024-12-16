from Plotter import Plotter


base_input_dir = 'C:/LGAD_test'
date = '2024-08-14'
initial_voltage = '0'
final_voltage = '-300'

# sensor_name = 'UFSD-K1_W5_16x16_(3-4)_good_inner_pad'
sensor_name = 'FBK_54_2x2_T10'
input_data_pad1 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_two_contact_'+date+'_pad1_v1.txt'
input_data_pad2 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_two_contact_'+date+'_pad2_v1.txt'
input_data_pad3 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_two_contact_'+date+'_pad3_v1.txt'
input_data_pad4 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_two_contact_'+date+'_pad4_v1.txt'

#input_data_pad1 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_pad1_v1.txt'
#input_data_pad2 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_pad2_v1.txt'
#input_data_pad3 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_pad3_v1.txt'
#input_data_pad4 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_pad4_v1.txt'


# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter = Plotter('CMS', r'C:\LGAD_test/I-V_test/'+sensor_name+"/")
plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)

colors = plotter.get_n_colors(6)
# label = "Without switching matrix(SW)"
plotter.add_input_data(input_data_pad1, label="Pad 1", color=colors[0], linestyle='--', linewidth=2, y_scale=1e3, draw_half=True, flip_y=True)
plotter.add_input_data(input_data_pad2, label="Pad 2", color=colors[1], linestyle='--', linewidth=2, y_scale=1e3, draw_half=True, flip_y=True)
plotter.add_input_data(input_data_pad3, label="Pad 3", color=colors[2], linestyle='--', linewidth=2, y_scale=1e3, draw_half=True, flip_y=True)
plotter.add_input_data(input_data_pad4, label="Pad 4", color=colors[3], linestyle='--', linewidth=2, y_scale=1e3, draw_half=True, flip_y=True)

plotter.add_input_data(input_data_pad1, label="Total", y_index=2, color=colors[0], linewidth=2, y_scale=1e3, draw_half=True, flip_y=True)
plotter.add_input_data(input_data_pad2, label="Total", y_index=2, color=colors[1], linewidth=2, y_scale=1e3, draw_half=True, flip_y=True)
plotter.add_input_data(input_data_pad3, label="Total", y_index=2, color=colors[2], linewidth=2, y_scale=1e3, draw_half=True, flip_y=True)
plotter.add_input_data(input_data_pad4, label="Total", y_index=2, color=colors[3], linewidth=2, y_scale=1e3, draw_half=True, flip_y=True)

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True)

# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 54', fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best')
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_y_lim((1e-9, 0.9))
plotter.set_current_axis()
plotter.current_axis.grid(axis='y')
plotter.current_axis.grid(axis='x')
plotter.set_y_label("Current [mA]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name=sensor_name+'_two_contact_iv')
#plotter.save_fig(out_name=sensor_name+'_iv')
