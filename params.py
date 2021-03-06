# -*- coding: utf-8 -*-
import sys, os
import getpass

test = False


#data_type = "ds"
#data_type = "tsmat"
##data_type = "amplmat"
data_type = 'fif'

main_path = '/media/karim/SSD500/aut_gamma/'
data_folder = 'Moscow_baseline_results_new'
data_path = os.path.join(main_path, data_folder)


# subgroups = ('Controls', 'NEWPATIENTS')
conditions = ('ec', 'eo')
power_analysis_name='power_analyses_aut_gamma'


subject_ids =[ 'K0001', 'K0002', 'K0003', 'K0004', 'K0005', 'K0006',
               'K0008', 'K0010', 'K0011', 'K0012', 'K0013', 'K0014',
               'K0015', 'K0016', 'K0017', 'K0018', 'K0019', 'K0020',
               'K0021', 'K0022', 'K0024', 'K0025', 'K0026', 'K0027',
               'K0028', 'K0029', 'K0030', 'K0031', 'K0032', 'K0033',
               'K0034', 'K0035', 'K0036', 'K0037', 'K0038', 'K0039',
               'K0040', 'K0041', 'K0042', 'K0043', 'K0045', 'K0046',
               'K0047', 'K0049', 'K0050', 'K0051', 'R0001', 'R0002',
               'R0003', 'R0004', 'R0005', 'R0006', 'R0007', 'R0008',
               'R0009', 'R0010', 'R0011', 'R0012', 'R0014', 'R0015',
               'R0016', 'R0017', 'R0018', 'R0020', 'R0021', 'R0022',
               'R0023', 'R0024', 'R0026', 'R0028', 'R0029', 'R0030',
               'R0031', 'R0032', 'R0033', 'R0034', 'R0035', 'R0036',
               'R0037', 'R0038', 'R0039', 'R0040', 'R0042', 'R0044',
               'R0045', 'R0047', 'R0048', 'R0050', 'R0051', 'R0052',
               'R0056', 'R0060', 'R0061', 'R0062']