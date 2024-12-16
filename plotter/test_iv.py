from Plotter import Plotter


def combine_sensor_name_and_description(sensor_name, description=''):
    if description == '':
        return sensor_name
    else:
        return sensor_name + '_' + description

def make_txt_path(sensor_name, description, date, coln, rown, versin):
    return 'C:/LGAD_test/I-V_test/'+sensor_name+'/IV_SMU+PAU_' + combine_sensor_name_and_description(sensor_name, description) + '_' + date + '_' + coln + '_' + rown + '_v'+ version+'.txt'


base_input_dir = 'C:/LGAD_test'

# TODO update add_input_data()
plotter = Plotter('CMS', 'C:/LGAD_test/I-V_test/')
plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)

colors = plotter.get_n_colors(9)
kwargs = {"linestyle":'--', "linewidth":2, "draw_half":True, "y_scale":1e3, "flip_y":True}

sensor_name = 'W9b'
description = 'probecard_full_ground'
date = '2024-09-02'
coln = 'col1'
rown = 'row1'
version = '0'
txt_path = make_txt_path(sensor_name, description, date, coln, rown, version)
plotter.add_input_data(txt_path, label= 'W9b ' + coln + ' ' + rown, y_index=3, color=colors[0], linewidth=2, draw_half=True, y_scale=1e3, flip_y=True)

sensor_name = 'W12'
description = 'Compare'
date = '2024-10-18'
coln = 'col1'
rown = 'row1'
version = '0'
txt_path = make_txt_path(sensor_name, description, date, coln, rown, version)
plotter.add_input_data(txt_path, label= 'W12,' +coln + ' ' + rown, y_index=3, color='black', linewidth=2, draw_half=True, y_scale=1e3, flip_y=True)

plotter.draw(x_index=0, y_index=3, remove_offset=False, flip_x=True)

# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plot_title = 'W9b 16x16(diced)'
plotter.set_experiment_label(location=(0, 0), label=plot_title, fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best', ncol=2)
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_y_lim((1e-9, 0.9))
plotter.set_current_axis()
plotter.current_axis.grid(axis='y')
plotter.current_axis.grid(axis='x')
plotter.set_y_label("Current [mA]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name=sensor_name+'_pad_iv')
