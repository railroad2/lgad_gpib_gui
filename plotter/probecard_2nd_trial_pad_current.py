from Plotter import Plotter


base_input_dir = 'C:/LGAD_test'
date = '2024-09-06'
initial_voltage = '0'
final_voltage = '-250'


# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter = Plotter('CMS', 'C:/LGAD_test/I-V_test/')
plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)

colors = plotter.get_n_colors(9)
# label = "Without switching matrix(SW)"
kwargs = {"linestyle":'--', "linewidth":2, "draw_half":True, "y_scale":1e3, "flip_y":True}

sensor_name = 'W9b'
probecard = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_Before_1_'+date+'_'+'col1_row1_v2.txt'
plotter.add_input_data(probecard, label="Probecard", y_index=3, color=colors[0], linewidth=3, draw_half=True, y_scale=1e3, flip_y=True)

#probecard_many_ground = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_probecard_test_more_ground_'+date+'_'+'pad3_v0.txt'
#plotter.add_input_data(probecard_many_ground, label="Probecard (more ground)", y_index=3, color=colors[1], linewidth=2, draw_half=True, y_scale=1e3, flip_y=True)

date = '2024-08-20'
probestation = 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_two_contact_rightmost_'+date+'_'+'pad4_v0.txt'
plotter.add_input_data(probestation, label="Probe station", y_index=3, color=colors[1], linewidth=3, draw_half=True, y_scale=1e3, flip_y=True)

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True)

# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='UFSD-K1 16x16(diced)', fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best', ncol=2, fontsize="large")
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_y_lim((1e-10, 0.9))
plotter.set_current_axis()
plotter.current_axis.grid(axis='y')
plotter.current_axis.grid(axis='x')
plotter.set_y_label("Current [mA]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name=sensor_name+'_connection_test_iv')
