from Plotter import Plotter

plotter = Plotter('CMS', r'C:\LGAD_test')

base_input_dir = 'C:/LGAD_test'
date = '2024-07-04'
initial_voltage = '0'
final_voltage = '-250'

sensor_name = 'FBK_W9a_two_contact_column_test'
input_data_pad0 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad0.txt'
input_data_pad1 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad1.txt'
input_data_pad2 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad2.txt'
input_data_pad3 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad3.txt'
input_data_pad4 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad4.txt'
input_data_pad5 = 'C:/LGAD_test/I-V_test/'+date+'_'+sensor_name+'/IV_SMU+PAU_'+sensor_name+'_'+date+'_'+initial_voltage+'_'+final_voltage+'_pad5.txt'

plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)


colors = plotter.get_n_colors(7)
# label = "Without switching matrix(SW)"
kwargs = {"linewidth":2, "draw_half":True, "ratio":(2,3)}
plotter.add_input_data(input_data_pad0, label="Pad 0", color=colors[0], **kwargs)
plotter.add_input_data(input_data_pad1, label="Pad 1", color=colors[1], **kwargs)
plotter.add_input_data(input_data_pad2, label="Pad 2", color=colors[2], **kwargs)
plotter.add_input_data(input_data_pad3, label="Pad 3", color=colors[3], **kwargs)
plotter.add_input_data(input_data_pad4, label="Pad 4", color=colors[4], **kwargs)
plotter.add_input_data(input_data_pad5, label="Pad 5", color=colors[5], **kwargs)

plotter.draw(remove_offset=False, flip_x=True)

# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='W5b', fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best', ncol=2)
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.current_axis.grid(axis='y')
plotter.current_axis.grid(axis='x')
plotter.set_y_label("Pad I/Total I")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name='iv_ratio')
