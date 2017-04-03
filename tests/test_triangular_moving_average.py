import unittest
import numpy as np

from sample_data import SampleData
from py_technical_indicators import triangular_moving_average


class TestTriangularMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.tma_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, 809.53749999999991,
        811.09222222222218, 812.18555555555565, 812.73388888888894,
        812.97722222222228, 812.81555555555553, 811.76416666666671,
        809.32611111111112, 805.76972222222219, 801.20944444444456,
        795.4805555555555, 789.62333333333333, 784.38138888888886,
        780.56499999999994, 777.83472222222224, 776.71500000000003,
        777.42277777777781, 778.9141666666668, 780.08777777777777,
        781.00472222222231, 781.86055555555561, 782.20583333333343,
        781.09416666666675, 779.37222222222226, 778.14444444444428,
        777.44611111111101, 777.64277777777772, 778.6925, 781.39944444444461,
        784.75888888888903, 788.22416666666675, 791.14666666666665,
        793.12250000000006, 794.83888888888896, 796.78777777777793,
        799.55527777777786, 803.21166666666659, 807.7116666666667,
        812.66277777777771, 817.18444444444447, 820.96972222222223,
        823.62944444444429, 824.57138888888869, 823.80777777777769,
        822.09583333333342, 820.05250000000012, 817.25194444444458,
        814.26499999999999, 811.71083333333343, 809.97944444444454,
        808.72388888888884, 807.49277777777786, 806.49305555555554,
        805.41583333333335, 804.5625, 803.94527777777773, 803.67111111111092,
        803.64249999999993, 804.27416666666659, 805.51694444444445,
        806.77250000000004, 807.5486111111112, 807.63472222222219,
        807.59472222222223, 806.76833333333343, 804.90361111111122,
        802.5194444444445, 800.39416666666659, 798.50305555555553,
        796.87722222222237, 795.82055555555564, 795.95972222222235,
        796.77833333333331, 797.41750000000002, 798.28666666666675,
        798.71722222222218, 798.62194444444458, 797.62777777777785,
        796.25250000000005, 795.1444444444445, 794.18555555555542,
        793.66972222222228, 793.59833333333336, 794.20277777777767,
        795.35416666666663, 796.65527777777777, 798.02944444444438,
        799.54444444444437, 801.19055555555553, 802.73138888888889,
        803.9372222222222, 805.04444444444437, 805.91833333333341,
        806.23944444444442, 806.06527777777774, 805.49916666666661,
        804.69416666666666, 803.39111111111106, 800.91972222222228,
        797.7405555555556, 793.67277777777781, 788.6541666666667,
        782.65999999999997, 776.02583333333325, 770.28972222222228,
        765.29583333333346, 761.32472222222225, 757.92888888888899,
        755.03805555555562, 752.4805555555555, 749.48388888888894,
        745.99694444444447, 741.64972222222229, 737.12249999999995,
        732.50222222222226, 727.89138888888886, 723.34472222222223]

        self.tma_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        811.30218750000006, 811.75578125000004, 811.56750000000011,
        810.74453124999991, 809.16359375000002, 806.62343750000002,
        803.16843749999998, 799.24093749999997, 795.04375000000005,
        791.01296875000003, 787.13468749999993, 783.82640624999999,
        781.20890625000004, 779.74406250000004, 779.25812500000006,
        779.43312500000002, 779.77296875000002, 780.09328125000002,
        780.16812500000003, 780.08562500000005, 779.82359374999999,
        779.56859374999999, 779.69437500000004, 779.90750000000003,
        780.28593750000005, 780.9403125, 782.56625000000008, 784.83249999999998,
        787.63499999999999, 790.3309375, 792.54812500000003, 794.83093750000012,
        797.83765625000001, 801.57124999999996, 805.31171874999995,
        808.77750000000003, 812.04921875000002, 815.1328125, 817.96828125000002,
        820.21671874999993, 821.34140624999998, 821.25484374999996,
        820.38499999999999, 819.14625000000001, 817.22671875000003, 814.989375,
        812.8285937500001, 810.91296875, 809.32187500000009, 807.98484374999998,
        806.76593750000006, 805.59937500000001, 805.00156249999998, 804.6846875,
        804.67000000000007, 804.88921874999994, 805.2389062499999,
        805.64218749999998, 806.04046874999995, 806.31406249999998,
        806.28265624999995, 806.0675, 805.22781250000003, 803.91484375000005,
        802.27062500000011, 800.74109375, 799.52171874999999,
        798.64828125000008, 797.85515625000005, 797.26718750000009,
        797.10687499999995, 797.10640624999996, 797.47921874999997,
        797.65390624999998, 797.37093749999997, 796.70562500000005,
        796.10406249999994, 795.57453125000006, 795.18046875000005,
        795.06343749999996, 794.98171875000003, 795.17484375000004,
        795.85781250000002, 796.97624999999994, 798.28046874999995,
        799.67828125000005, 801.04531250000002, 802.28187500000001,
        803.39203125000006, 804.31609375000005, 804.90109374999997,
        805.16765625000005, 805.13937499999997, 804.66281249999997,
        803.41328124999995, 801.44906249999997, 798.69124999999997,
        795.37421874999995, 791.54781249999996, 787.11546874999999,
        782.11124999999993, 776.78234375, 771.90656250000006,
        767.29515624999999, 763.11234375000004, 759.1121875, 755.31312500000001,
        751.80312499999991, 748.36437500000011, 744.79718749999995,
        740.73640624999996, 736.60687499999995, 732.41953125000009]

        self.tma_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 809.38290000000006, 808.3297,
        806.53129999999999, 804.16270000000009, 801.42739999999992,
        798.49129999999991, 795.24619999999993, 791.98450000000003,
        788.86539999999991, 786.22270000000003, 783.90030000000002,
        782.24869999999999, 781.26679999999999, 780.69779999999992,
        780.02559999999994, 779.43410000000006, 779.13599999999997,
        779.26549999999997, 779.72950000000003, 780.27960000000007,
        780.90349999999989, 781.27069999999992, 781.56579999999997,
        782.17129999999997, 783.70579999999995, 785.85879999999986,
        788.38149999999985, 790.80340000000001, 793.12119999999993,
        795.60379999999998, 798.46469999999999, 801.75969999999995,
        805.35699999999986, 808.81119999999999, 811.66800000000001,
        813.89710000000002, 815.62290000000007, 817.08030000000008,
        818.18219999999997, 818.73129999999992, 818.6173, 817.92340000000002,
        816.58420000000001, 814.89790000000005, 813.1776000000001,
        811.60149999999999, 810.14369999999997, 808.77209999999991,
        807.60189999999989, 806.53219999999988, 805.83849999999995,
        805.45900000000006, 805.37609999999995, 805.45009999999991,
        805.53879999999992, 805.57199999999989, 805.60550000000001,
        805.46010000000001, 805.08299999999997, 804.78279999999995,
        804.07530000000008, 803.10799999999995, 802.13229999999999,
        801.26909999999998, 800.4706000000001, 799.66729999999995,
        798.76430000000005, 798.07190000000003, 797.67060000000004,
        797.25159999999983, 797.12559999999996, 797.03829999999994,
        796.80740000000003, 796.38340000000005, 795.97239999999988,
        795.74059999999986, 795.77830000000006, 795.89409999999998, 796.0403,
        796.38080000000014, 796.86210000000005, 797.5847, 798.53019999999992,
        799.66920000000005, 800.8531999999999, 801.86869999999999, 802.6635,
        803.35490000000004, 803.89470000000006, 804.13909999999998,
        803.79090000000008, 802.82860000000005, 801.25909999999999,
        799.12969999999996, 796.45100000000002, 793.39890000000003,
        789.99340000000007, 786.13150000000007, 781.84240000000011,
        777.15330000000017, 772.58740000000012, 768.16180000000008,
        763.98310000000015, 759.97829999999999, 756.03500000000008,
        752.04859999999985, 747.9994999999999, 743.93229999999994,
        739.91300000000001]

    def test_triangular_moving_average_period_6(self):
        period = 6
        tma = triangular_moving_average.triangular_moving_average(self.data, period)
        np.testing.assert_array_equal(tma, self.tma_period_6_expected)

    def test_triangular_moving_average_period_8(self):
        period = 8
        tma = triangular_moving_average.triangular_moving_average(self.data, period)
        np.testing.assert_array_equal(tma, self.tma_period_8_expected)

    def test_triangular_moving_average_period_10(self):
        period = 10
        tma = triangular_moving_average.triangular_moving_average(self.data, period)
        np.testing.assert_array_equal(tma, self.tma_period_10_expected)

    def test_triangular_moving_average_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            triangular_moving_average.triangular_moving_average(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
