from Plotter import Plotter

plotter = Plotter('CMS', r'C:\LGAD_test')

base_input_dir = 'C:/LGAD_test'
date = '2024-07-08'
initial_voltage = '0'
final_voltage = '-350'

data = ['K1_W1_2-4', 'K1_W1_2-4_2', 'K1_W1_2-5', 'K1_W1_2-5_2', 'W1_5-3', 'W1_5-3_2',
        'W5_K1_2-5', 'W5_K1_2-5_2', 'W13_K1_5-5', 'WS_K1_2-3', 'WS_K1_2-3_(6,16)']

input_data_path = []
for name in data:
    input_data_path.append('C:/LGAD_test/I-V_test/torino/' + name + '.txt')
plotter.create_subplots(rows=1, cols=1, figsize=(15, 10), left=0.15)

colors = plotter.get_n_colors(10)
kwargs = {"linewidth":2, "draw_half":True, 'ratio':(1,2), "flip_y":True}

for index, input_data in enumerate(input_data_path):
    plotter.add_input_data(input_data, label=data[index], color=colors[index], **kwargs)

plotter.draw(remove_offset=False, flip_x=True)

# plotter.do_get_renderer()
# plotter.set_experiment_label(location=(0, 0), label='FBK 2x2 2022v2 56 T10 (offset removed)', fontsize=15, pad=0.1)
plotter.set_experiment_label(location=(0, 0), label='Measured in Torino', fontsize=20)
plotter.get_current_axis().set_yscale('log')
plotter.show_legend(loc='best', ncol=2)
# plotter.set_experiment_label()

plotter.set_axis_label_font_size(20)
plotter.set_current_axis()
plotter.current_axis.grid(axis='y')
plotter.current_axis.grid(axis='x')
plotter.set_y_label("Pad I/Total I")
plotter.set_x_label("Bias voltage [V]")

plotter.save_fig(out_name='torino_iv_ratio')
