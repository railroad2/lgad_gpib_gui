from Plotter import Plotter

plotter = Plotter('CMS', 'C:/LGAD_test/I-V_test/')

base_input_dir = 'C:/LGAD_test'
date = '2024-06-12'
sensor_name = 'FBK'
initial_voltage = '0'
final_voltage = '-50'

input_data_pad3 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-50_pad3.txt'

sensor_name = 'FBK_SWv2'
input_data_pad3_switch_v2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-50_pad3.txt'

# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)

label = "Without SW"
plotter.add_input_data(input_data_pad3, label=label, linewidth=3, draw_half=True, y_scale=1e3, flip_y=True)

label = "With switching matrix(SW)"
plotter.add_input_data(input_data_pad3_switch_v2, label=label, linewidth=3, draw_half=True, y_scale=1e3, flip_y=True)

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True)
plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='UFSD-K1 2x2 (diced)', fontsize=15)
# plotter.write_text("Pad 1 (Not available)")
plotter.show_legend(loc='best')
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.set_y_label("Current [mA]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name=sensor_name+'_20240612_SWv2_test')
