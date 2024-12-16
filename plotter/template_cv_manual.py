from Plotter import Plotter


def combine_sensor_name_and_description(sensor_name, description=''):
    if description == '':
        return sensor_name
    else:
        return sensor_name + '_' + description

def make_txt_path(sensor_name, description, date, coln, rown, versin):
    return 'C:/LGAD_test/C-V_test/'+sensor_name+'/IV_SMU+PAU_' + combine_sensor_name_and_description(sensor_name, description) + '_' + date + '_' + coln + '_' + rown + '_v'+ version+'.txt'


base_input_dir = 'C:/LGAD_test'

# TODO update add_input_data()
plotter = Plotter('CMS', 'C:/LGAD_test/C-V_test/')
plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)

colors = plotter.get_n_colors(9)
kwargs = {"linestyle":'--', "linewidth":2, "draw_half":True, "flip_y":False}

sensor_name = 'W1a'
description = ''
date = '2024-10-11'
coln = 'col2'
rown = 'row1'
version = '2'
txt_path = make_txt_path(sensor_name, description, date, coln, rown, version)
plotter.add_input_data(txt_path, label= 'v2 ' + coln + ' ' + rown, y_index=1, color=colors[0], linewidth=2, draw_half=True)

sensor_name = 'W1a'
description = ''
date = '2024-10-11'
coln = 'col2'
rown = 'row1'
version = '3'
txt_path = make_txt_path(sensor_name, description, date, coln, rown, version)
plotter.add_input_data(txt_path, label= 'v3' +coln + ' ' + rown, y_index=1, color=colors[4], linewidth=2, draw_half=True)

plotter.draw(x_index=0, y_index=1, remove_offset=False, flip_x=True)

# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plot_title = 'W1a 16x16(diced)'
plotter.set_experiment_label(location=(0, 0), label=plot_title, fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best', ncol=2)
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
#plotter.set_y_lim((1e-9, 0.9))
plotter.set_current_axis()
plotter.current_axis.grid(axis='y')
plotter.current_axis.grid(axis='x')
plotter.set_y_label("Capacitance [F]")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name=sensor_name+'_pad_cv')
