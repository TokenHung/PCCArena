import logging.config

from utils.file_io import get_logging_config
from algs_wrapper.Draco import Draco
from algs_wrapper.GPCC import GPCC
from algs_wrapper.VPCC import VPCC
from algs_wrapper.GeoCNNv1 import GeoCNNv1
from algs_wrapper.GeoCNNv2 import GeoCNNv2
from algs_wrapper.PCGCv1 import PCGCv1
from algs_wrapper.PCGCv2 import PCGCv2

def main():
    LOGGING_CONFIG = get_logging_config('utils/logging.conf')
    logging.config.dictConfig(LOGGING_CONFIG)

    draco = Draco()
    for rate in range(8):
       draco.rate = f'r{rate+1}'
       draco.run_dataset('SNC_Test100', 'experiments')
       draco.run_dataset('SNCC_Test100', 'experiments')
    
    gpcc = GPCC()
    for rate in range(8):
        gpcc.rate = f'r{rate+1}'
        gpcc.run_dataset('SNC_Test100', 'experiments')
        gpcc.run_dataset('SNCC_Test100', 'experiments')

    vpcc = VPCC()
    for rate in range(5):
        vpcc.rate = f'r{rate+1}'
        vpcc.run_dataset('SNCC_Test100', 'experiments')

    # [TODO]
    # fix about paralllel running
    # tensorflow mkl memeory raise
    geocnn_v1 = GeoCNNv1()
    for rate in range(5):
        geocnn_v1.rate = f'r{rate+1}'
        # `nbprocesses` depends on your available memory
        # 1 process may cost up to 51 GB memory
        geocnn_v1.run_dataset('SNC_Test100', 'experiments', nbprocesses=2)

    geocnn_v2 = GeoCNNv2()
    for rate in range(4):
        geocnn_v2.rate = f'r{rate+1}'
        geocnn_v2.run_dataset('SNC_Test100', 'experiments')

    pcgc_v1 = PCGCv1()
    for rate in range(6):
        pcgc_v1.rate = f'r{rate+1}'
        pcgc_v1.run_dataset('SNC_Test100', 'experiments')
    
    pcgc_v2 = PCGCv2()
    for rate in range(7):
        pcgc_v2.rate = f'r{rate+1}'
        pcgc_v2.run_dataset('SNC_Test100', 'experiments')


if __name__ == '__main__':
    main()
