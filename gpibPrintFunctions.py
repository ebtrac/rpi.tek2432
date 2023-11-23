#!/bin/python3

import gpib

# class for interfacing with the Tektronix 2432 over GPIB

class TekScope:
    def __init__(self, board_pad, device_pad):
        self.con = gpib.dev(board_pad, device_pad)
        gpib.config(board_pad, gpib.IbcTMO, gpib.T30s) # set timeout to 30 secs


    # prints a message to the screen
    def print(self, message):
        from textwrap import wrap
        rows = 16
        cols = 40
        lines = wrap(message, width=cols, max_lines=rows, placeholder='...')
        for i in range(len(lines)):
            gpib.write(self.con, "MESSAGE {}:\"{}\"".format(rows - i, lines[i]))
            if i >= rows:
                break

    # clears the printed text
    def clear_text(self):
        gpib.write(self.con, "MESSAGE CLRSTATE")


class TekPlotSaver:
    def __init__(self, board_pad, device_pad):
        self.con = gpib.dev(board_pad, device_pad)
        gpib.config(board_pad, gpib.IbcTMO, gpib.T1s) # set timeout to 1 sec

    # polls ascii data while data is available, returns bytes
    def poll_data(self):
        data = b''
        while gpib.serial_poll(self.con):
            try:
                data += gpib.read(self.con, 512)
            except gpib.GpibError:
                break
        return data

    # writes all data received into a file
    def write_data_to_file(self, filename):
        with open(filename, 'wb') as f:
            data = self.poll_data()
            f.write(data)


if __name__ == '__main__':
    tek = TekScope(0, 1)
    tek.print("")
    gpib.close(tek.con)
