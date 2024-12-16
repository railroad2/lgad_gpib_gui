from Plotter import Plotter

plotter = Plotter('CMS', r'C:\LGAD_test')

base_input_dir = 'C:/LGAD_test'
date = '2024-07-01'
sensor_name = 'FBK_w13_two_contact_guard_ring_#12'
initial_voltage = '0'
final_voltage = '-250'

input_data_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'
input_data_pad2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad1.txt'
input_data_pad3 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad2.txt'
input_data_pad4 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad3.txt'

sensor_name = 'FBK_w13_four_contact_guard_ring_#12'
input_data_four_contact_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'
input_data_four_contact_pad2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad1.txt'
input_data_four_contact_pad3 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad2.txt'
input_data_four_contact_pad4 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad3.txt'

# TODO update add_input_data()
# plotter.add_input_data(sensor_name, date, measurement_type, initial_voltage, final_voltage, pad_name)
plotter.create_subplots(rows=1, cols=1, figsize=(10, 10), left=0.15)

colors = plotter.get_n_colors(4)
# label = "Without switching matrix(SW)"
plotter.add_input_data(input_data_pad1, label="Pad 0", color=colors[0], linewidth=2)
plotter.add_input_data(input_data_pad2, label="Pad 1", color=colors[1], linewidth=2)
plotter.add_input_data(input_data_pad3, label="Pad 2", color=colors[2], linewidth=2)
plotter.add_input_data(input_data_pad4, label="Pad 3", color=colors[3], linewidth=2)

plotter.add_input_data(input_data_four_contact_pad1, label="Pad 0 (four contact)", color=colors[0], linestyle='--')
plotter.add_input_data(input_data_four_contact_pad2, label="Pad 1 (four contact)", color=colors[1], linestyle='--')
plotter.add_input_data(input_data_four_contact_pad3, label="Pad 2 (four contact)", color=colors[2], linestyle='--')
plotter.add_input_data(input_data_four_contact_pad4, label="Pad 3 (four contact)", color=colors[3], linestyle='--')

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True, flip_y=True, draw_half=True)
# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='W13', fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best')
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.set_y_label("Current [A]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name='20240701_16x16_w13_#12')
