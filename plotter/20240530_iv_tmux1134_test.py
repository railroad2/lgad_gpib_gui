from Plotter import Plotter

plotter = Plotter('CMS', r'C:\LGAD_test')

base_input_dir = 'C:/LGAD_test'
date = '2024-05-29'
sensor_name = 'FBK'
initial_voltage = '0'
final_voltage = '-50'

# input_data_path1 = 'C:/LGAD_test/I-V_test/2024-03-26_FBK/IV_SMU+PAU_FBK_2024-03-26_0_-300_pad2.txt'
input_data_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-50_pad2.txt'

sensor_name = 'FBK_MUX_on_drain'
input_data_pad1_switch_v1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_0_-50_pad2.txt'

# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter.create_subplots(rows=1, cols=1, figsize=(10, 10))

label = "Without TMUX1134"
plotter.add_input_data(input_data_pad1, label=label, color='black')

label = "With TUMX1134"
plotter.add_input_data(input_data_pad1_switch_v1, label=label)

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True, flip_y=True, draw_half=True)
plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v1 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v1 34 T9', fontsize=15)
# plotter.write_text("Pad 1 (Not available)")
plotter.write_text("Pad 1", location=(0, 0))
plotter.show_legend(loc='lower right')
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.set_y_label("Current [A]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name='20240530_TMUX1134_test')
