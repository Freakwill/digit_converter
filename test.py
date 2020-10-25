from digit_converter import *

import pytest
class Test_DC:
    # 
    def test_color(self):
        print('Color converter as a special binary converter:')
        assert colorConverter.tonumber([1,0,1,0,1,1,1,0]) == 174

    def test_binary(self):
        print('Binary converter: 12.223 <->11000011')
        c = BinaryConverter(exponent=3)
        d = c.tolist(12.223, L=8)
        assert d == [1, 1, 0, 0, 0, 0, 1, 1] and abs(c.tonumber(d) - 12) < 0.2

    def test_interval(self):
        lb, ub = 0, 10
        print(f'Interval [{lb}, {ub}] converter: 2.4 <-> [0, 2, 6, 6, 6, 6, 6, 6]')
        c = IntervalConverter(lb=lb, ub=ub)
        d = c.tolist(n, L=8)
        assert d == [0, 2, 6, 6, 6, 6, 6, 6] or (c(d)-2.4) < 0.1 
        
if __name__ == '__main__':
    pytest.main("-s test_dc.py")