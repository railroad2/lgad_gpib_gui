from util import USBComm
from serial.tools import list_ports


class SwitchMatrixGUI:
    def __init__(self, combo_box, status_label):

        self.combo_box = combo_box
        self.status_label = status_label

        #usb_port = "COM3" for windows
        ports = self.find_board()
        self.usb_port = ports[0]
        self.comm = USBComm(self.usb_port)
        #print (self.usb_port)
        if self.comm.is_connected():
            self.status_label.setText(self.usb_port + " is connected")
            self.combo_box.addItems(['0', '1', '2', '3', 'All'])
            self.combo_box.currentIndexChanged.connect(self.set_switch)
            self.set_switch()
        else:
            self.status_label.setText("Switch matrix is not ready")
            self.combo_box.setEnabled(False)

    def find_board(self):
        l = list_ports.comports()
        pico = []
        for i in l:
            if i.manufacturer == 'MicroPython':
                pico.append(i.device)
        return pico

    def set_switch(self):
        current_index = self.combo_box.currentIndex()
        #
        if current_index == 1:
            current_index = 1
        if current_index == 2:
            current_index = 2
        if current_index == 3:
            current_index = 3
        msg = self.comm.send_data(f"ON {current_index}")
        #print(msg)
        self.status_label.setText(msg)

