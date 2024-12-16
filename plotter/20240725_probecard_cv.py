from Plotter import Plotter

plotter = Plotter('CMS', r'C:\LGAD_test')

base_input_dir = 'C:/LGAD_test'
date = '2024-07-25'
sensor_name = 'Probecard_connector1_pin1'
initial_voltage = '0'
final_voltage = '-250'

# input_data_path1 = 'C:/LGAD_test/C-V_test/2024-03-26_FBK/CV_LCR+PAU_FBK_2024-03-26_0_-300_pad2.txt'
input_data_pad1 = 'C:/LGAD_test/C-V_test/'+date+'_'+sensor_name+'/CV_LCR+PAU_'+sensor_name+'_'+date+'_0_-60_1000Hz_pad0_2_3_4_5.txt'

# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter.create_subplots(rows=1, cols=1, figsize=(10, 10))

label = "Pad 1"
plotter.add_input_data(input_data_pad1, label=label, color='black')

plotter.draw(x_index=0, y_index=1, remove_offset=False, flip_x=True, flip_y=False, draw_half=True)
# plotter.set_y_lim((-0.8e-8, 1.2e-8), location=(0, 0))
# plotter.set_y_lim((-0.8e-8, 1.2e-8), location=(0, 1))
# plotter.set_y_lim((-0.8e-8, 1.2e-8), location=(1, 0))
plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v1 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='W13 with probecard', fontsize=15)
# plotter.write_text("Pad 1 (Not available)")
# plotter.write_text("Pad 1", location=(0, 0))
plotter.show_legend(loc='best')
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.set_y_label("Capacitance [F]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name=sensor_name+'_cv')
