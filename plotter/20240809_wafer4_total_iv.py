from Plotter import Plotter

plotter = Plotter('CMS', 'C:/LGAD_test/I-V_test/')

base_input_dir = 'C:/LGAD_test'
date = '2024-08-09'
initial_voltage = '0'
final_voltage = '-250'

sensor_name = 'FBK_w4_pad1'
input_data_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'

sensor_name = 'FBK_w4_pad2'
input_data_pad2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'

sensor_name = 'FBK_w4_pad3'
input_data_pad3 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'

# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)

colors = plotter.get_n_colors(6)
# label = "Without switching matrix(SW)"
plotter.add_input_data(input_data_pad1, label="Pad 1", color=colors[0], linestyle='--', linewidth=2, draw_half=True, flip_y=True, y_scale=1e3)
plotter.add_input_data(input_data_pad2, label="Pad 2", color=colors[1], linestyle='--', linewidth=2, draw_half=True, flip_y=True, y_scale=1e3)
plotter.add_input_data(input_data_pad3, label="Pad 3", color=colors[2], linestyle='--', linewidth=2, draw_half=True, flip_y=True, y_scale=1e3)

plotter.add_input_data(input_data_pad1, label="Total", color=colors[0], linewidth=2, draw_half=True, flip_y=True, y_index=2, y_scale=1e3)
plotter.add_input_data(input_data_pad2, label="Total", color=colors[1], linewidth=2, draw_half=True, flip_y=True, y_index=2, y_scale=1e3)
plotter.add_input_data(input_data_pad3, label="Total", color=colors[2], linewidth=2, draw_half=True, flip_y=True, y_index=2, y_scale=1e3)

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True)

# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='W4', fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best', ncol=2)
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_y_lim((1e-9, 0.1))
plotter.set_current_axis()
plotter.set_y_label("Current [mA]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name=sensor_name+'total_iv')
