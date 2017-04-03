import unittest
import numpy as np

from sample_data import SampleData
from py_technical_indicators import price_oscillator


class TestPriceOscillator(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.po_period_6_period_12_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        0.33656686827876153, 0.24292184988407403, 0.035067724348717487,
        -0.05406071412565526, -0.35004673662314001, -0.62263045093967562,
        -1.0669624544312803, -1.2389906759649123, -1.5110204167512691,
        -1.6261182911679213, -1.3240834310321137, -0.76589021835084514,
        -0.35267550929460328, -0.1786730879846998, -0.0018957725200040563,
        0.26510459125345681, 0.34147055858733261, 0.13086755049222953,
        0.17093670317910095, 0.096918309886777826, -0.082983263863072199,
        -0.66509624116476718, -0.60673235011329774, -0.29303104853489825,
        0.34468226645239197, 0.84878577996669469, 0.94505044858567422,
        0.70542492259487855, 0.47385402792426357, 0.36922095863848386,
        0.5029974674912906, 0.57388300283128812, 0.78520126365945242,
        0.85957069885467585, 0.9790474086415778, 1.108138052258884,
        1.2435314993803779, 1.0501459291579553, 0.76314054832525979,
        0.59228196311429271, 0.30805585730236129, -0.19692723343035684,
        -0.55872288637275969, -0.71355738322346673, -0.60261294452837888,
        -0.5877478343800322, -0.43068973716519604, -0.47083025080268265,
        -0.37843468355578452, -0.34608642350021979, -0.31387826528613755,
        -0.28955368360481154, -0.21918958063625779, -0.15778754789140392,
        0.0119281120121145, 0.13600217040313717, 0.069695669302550042,
        0.27199655996576089, 0.40157811394400944, 0.23393975623873936,
        -0.011195542389162422, -0.25715022670941545, -0.30558063074011871,
        -0.33383569790711165, -0.54774796153781913, -0.64149651755826453,
        -0.42819106933602813, -0.44299913075533054, -0.18328402531894275,
        0.10221462733661768, 0.34374527583026765, 0.26194265370770065,
        0.039925799814725639, -0.081450760143936096, -0.17725646544906976,
        -0.17554524654034062, -0.25467336737352586, -0.28687578727365287,
        -0.1961867421268958, -0.091814743483917272, 0.012686763664971051,
        0.1300784025066562, 0.27887671204644071, 0.3963112610922962,
        0.34506764190501288, 0.36601162718033853, 0.38129264423406917,
        0.38776599342562496, 0.35192439278793131, 0.26736790348106654,
        0.18009281827190562, 0.12789724276004677, -0.10437979447801317,
        -0.21573348592107991, -0.25051871323722097, -0.23638183749156919,
        -0.40178637011632429, -0.97276394255107779, -1.300639292911201,
        -1.528493755981265, -1.6030422566027416, -1.5448610058181429,
        -1.4865959798702686, -1.1697992693745809, -0.9711182594340334,
        -0.75054632710632552, -0.89723094523544311, -0.91396986510553502,
        -0.97842449731343739, -0.97628329013987103, -1.025130875479342,
        -1.2116616444711552, -1.3860949022082569, -1.3721087986499065,
        -1.3470159460391511, -1.1448131863137903]

        self.po_period_8_period_16_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, -0.16270640679322512, -0.44106770729780836,
        -0.82796082645009794, -1.0685185409067595, -1.4224222683985654,
        -1.6321717937653313, -1.5231764351448629, -1.1979144303690854,
        -0.92902995475284533, -0.78617490523814038, -0.61427991026050333,
        -0.36513084442939675, -0.1024583986780202, -0.033042479908235993,
        0.1310937395623098, 0.10578677316521959, 0.0041477681894246977,
        -0.38602387385538145, -0.38091760508137573, -0.25747590667790832,
        0.19059153837308618, 0.61510844668204256, 0.71220612061116739,
        0.49480282962594713, 0.3665291313934137, 0.4523396643251244,
        0.68879631587668455, 0.87880561472639573, 1.0220822217387593,
        1.0003426815287122, 1.0770772882483202, 1.2624590801823654,
        1.4432470188324076, 1.2765078898490787, 1.0457666227722078,
        0.9239154112204776, 0.73622359625779543, 0.39027487473036282,
        0.063836458576423588, -0.25454320688106735, -0.4040491870085352,
        -0.49224381879802298, -0.44077359779702036, -0.61565371148915937,
        -0.64793516402922513, -0.62488686939134364, -0.54390465117295017,
        -0.4846184160166192, -0.38005113270187424, -0.32457859083406831,
        -0.1843997198326002, 0.00018817325936242791, -0.003598928308990358,
        0.16177189975416084, 0.27641096018391614, 0.19506492285238289,
        0.059434439549834135, -0.096249726986007603, -0.17989263926081422,
        -0.21513892471745072, -0.3611479306240194, -0.53564919084454665,
        -0.49630243322591983, -0.57848854843560193, -0.37317826462586379,
        -0.12705458436967046, 0.054770637650484823, 0.0038055879833369635,
        -0.08128488191406405, -0.11918830741470089, -0.13868851473646102,
        -0.061042674948460142, -0.11122370729836616, -0.20587566549859762,
        -0.23114316000152352, -0.14636540935458528, -0.077876617940081078,
        0.014213217155228226, 0.1375361140319393, 0.22146255966391326,
        0.2498470670628519, 0.35948926567271916, 0.44010036862915686,
        0.46971591624195891, 0.46789759454974567, 0.42124727578010124,
        0.33108515495949653, 0.2780082283384695, 0.096732429751769711,
        -0.034154960809407588, -0.111961910002323, -0.15502938048411902,
        -0.33158409656829735, -0.82780608482923013, -1.1981337982092184,
        -1.4947817761396813, -1.6331458905791014, -1.654227020970338,
        -1.7029322502313791, -1.6482107028516373, -1.5793448326156361,
        -1.3736108772262612, -1.443998166565567, -1.4068632199376685,
        -1.4444085051515656, -1.3668748091955638, -1.3185432421196459,
        -1.3924372865176142, -1.566208414152876, -1.6600669374616905,
        -1.6715681693204156, -1.543125031779194]

        self.po_period_10_period_20_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, -1.1737757224811678,
        -1.4475535484135769, -1.4758235971129086, -1.2905181905501459,
        -1.1447781484541981, -1.0974597857588972, -1.0047704622825373,
        -0.81875795420444275, -0.60161286968174643, -0.54231009492677251,
        -0.30211454097089707, -0.17083629969672492, -0.15188960893809067,
        -0.45685201111475604, -0.42875503967734407, -0.25923738069027591,
        0.1827422237366845, 0.56228333931607277, 0.67909412752088638,
        0.52147952948548859, 0.3474521999723087, 0.30616847238929373,
        0.51978073116244305, 0.82753242251665748, 1.0989781436372839,
        1.215124012831805, 1.2456710294324289, 1.3048065028415592,
        1.4379433097083867, 1.4185578382715323, 1.36298086757794,
        1.3322777405084003, 1.1473994592109595, 0.74720495438023093,
        0.39236766644407128, 0.1237047114190349, 0.034408768779919024,
        -0.075535466230372453, -0.14768897282586149, -0.37326663400708709,
        -0.50869581619012416, -0.64404658755338717, -0.67623114748726876,
        -0.66460763145018642, -0.57226692472454221, -0.50884933983253511,
        -0.3745406089509688, -0.23732342214776422, -0.22837738758346862,
        -0.032241004855357157, 0.12054821350398304, 0.1192907889709499,
        0.044190519184570475, -0.079117596411069538, -0.15206915403906718,
        -0.1587330407534005, -0.30668645975865116, -0.43904136048769671,
        -0.36642347920896895, -0.50062457777259017, -0.41493461450533337,
        -0.24901682155657384, -0.1016237368423679, -0.11809702751977427,
        -0.19731908460514716, -0.2842819230491207, -0.26550986345182431,
        -0.18394963539511555, -0.19641266460218784, -0.16546556090404643,
        -0.15085997665528458, -0.13401495064252866, -0.12559420313660308,
        -0.054651380593862695, 0.061350321435350318, 0.1931927044550725,
        0.21076053770381414, 0.26205493136696911, 0.33451941300817339,
        0.38584312820484329, 0.43824973433001246, 0.45895872865446197,
        0.44101233333715606, 0.41461299215320402, 0.2458258554277597,
        0.12118830507632321, 0.055215377540203621, 0.0029460720115578876,
        -0.16767905204208994, -0.62434119732203275, -1.0067418898057001,
        -1.3270244253895094, -1.541019762578848, -1.6561874717762777,
        -1.7395799937459206, -1.7368627507960244, -1.7640309542965522,
        -1.750997976810698, -1.9059875212438928, -1.8860271429149023,
        -1.8947739458528328, -1.798212687290317, -1.7541060412534195,
        -1.8065457953192043, -1.9438636408965346, -1.982567486484605,
        -2.0037874740416379, -1.8918230166356396]

    def test_po_period_6_period_12(self):
        short_period = 6
        long_period = 12
        po = price_oscillator.price_oscillator(self.data, short_period, long_period)
        np.testing.assert_array_equal(po, self.po_period_6_period_12_expected)

    def test_po_period_8_period_16(self):
        short_period = 8
        long_period = 16
        po = price_oscillator.price_oscillator(self.data, short_period, long_period)
        np.testing.assert_array_equal(po, self.po_period_8_period_16_expected)

    def test_po_period_10_period_20(self):
        short_period = 10
        long_period = 20
        po = price_oscillator.price_oscillator(self.data, short_period, long_period)
        np.testing.assert_array_equal(po, self.po_period_10_period_20_expected)

    def test_po_invalid_period_short(self):
        short_period = 128
        long_period = 20
        with self.assertRaises(Exception) as cm:
            price_oscillator.price_oscillator(self.data, short_period, long_period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_po_invalid_period_long(self):
        short_period = 10
        long_period = 128
        with self.assertRaises(Exception) as cm:
            price_oscillator.price_oscillator(self.data, short_period, long_period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
