from Plotter import Plotter


base_input_dir = 'C:/LGAD_test'
date = '2024-07-04'
initial_voltage = '0'
final_voltage = '-250'


# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter = Plotter('CMS', 'C:/LGAD_test/I-V_test/')
plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)

colors = plotter.get_n_colors(9)
# label = "Without switching matrix(SW)"
kwargs = {"linestyle":'--', "linewidth":2, "draw_half":True, "y_scale":1e3, "flip_y":True}

sensor_name = 'FBK_W9a_two_contact_column_test'
diced_pad0 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'
diced_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad1.txt'
diced_pad2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad2.txt'

plotter.add_input_data(diced_pad0, label="W9a diced sensor", y_index=2, color=colors[0], linewidth=2, draw_half=True, y_scale=1e3, flip_y=True)

sensor_name = 'W1a'
date = '2024-08-20'
diced_pad3 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_two_contact_from_left_col7_'+date+'_'+'pad1_v0.txt'
diced_pad4 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_two_contact_from_left_col8_'+date+'_'+'pad1_v0.txt'
diced_pad5 = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_two_contact_from_left_col9_'+date+'_'+'pad1_v0.txt'

plotter.add_input_data(diced_pad3, label="W1a diced sensor", y_index=2, color=colors[1], linewidth=2, draw_half=True, y_scale=1e3, flip_y=True)

date = '2024-08-09'
sensor_name = 'FBK_w4_pad1'
on_wafer_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'

sensor_name = 'FBK_w4_pad2'
on_wafer_pad2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'

sensor_name = 'FBK_w4_pad3'
on_wafer_pad3 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'

plotter.add_input_data(on_wafer_pad1, label="W4 on-wafer sensor 1", color=colors[2], linestyle='--', linewidth=2, draw_half=True, flip_y=True, y_index=2, y_scale=1e3)
plotter.add_input_data(on_wafer_pad2, label="W4 on-wafer sensor 2", color=colors[3], linestyle='--', linewidth=2, draw_half=True, flip_y=True, y_index=2, y_scale=1e3)
plotter.add_input_data(on_wafer_pad3, label="W4 on-wafer sensor 3", color=colors[4], linestyle='--', linewidth=2, draw_half=True, flip_y=True, y_index=2, y_scale=1e3)

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True)

# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='', fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best', ncol=2)
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_y_lim((1e-10, 0.9))
plotter.set_current_axis()
plotter.current_axis.grid(axis='y')
plotter.current_axis.grid(axis='x')
plotter.set_y_label("Total current [mA]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name=sensor_name+'_iv')
