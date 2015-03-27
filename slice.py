class Slice(object):
    def __init__(self, start_positions, end_positions):
        # Unpack tuples.
        (self.start_x, self.start_y) = start_positions
        (self.end_x, self.end_y) = end_positions

    def get_printable_output(self):
        return str(self.start_x) + ' ' + str(self.start_y) + ' ' + str(self.end_x) + ' ' + str(self.end_y)
