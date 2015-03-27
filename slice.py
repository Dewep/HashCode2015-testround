class Slice(object):
    def __init__(self, line_positions, column_positions):
        # Unpack tuples.
        (self.line_start, self.line_end) = line_positions
        (self.column_start, self.column_end) = column_positions

    def get_printable_output(self):
        return str(self.line_start) + ' ' + str(self.line_end) + ' ' + str(self.column_start) + ' ' + str(self.column_end)
