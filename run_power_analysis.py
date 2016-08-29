import nipype.pipeline.engine as pe
from nipype.interfaces.utility import IdentityInterface
from neuropype_ephy.interfaces.mne.power import Power
import nipype.interfaces.io as nio


from params import main_path, data_path 
from params import subject_ids
from params import conditions
# from params import subgroups
from params import power_analysis_name

def create_infosource():

    infosource = pe.Node(interface=IdentityInterface(fields=['subject_id', 'condition']), name="infosource")
    
    infosource.iterables = [('subject_id', subject_ids), ('condition', conditions)]

    return infosource


def create_datasource():
    datasource = pe.Node(interface=nio.DataGrabber(infields=['subject_id', 'condition'], outfields=['epo_file']), name = 'datasource')
    datasource.inputs.base_directory = data_path
    datasource.inputs.template = '%s/%s%s%s'
    datasource.inputs.template_args = dict(
        epo_file = [['subject_id', 'subject_id', 'condition', '-epo.fif']]
        )
    datasource.inputs.sort_filelist = True
    return datasource




def create_main_workflow_power():
    
    main_workflow = pe.Workflow(name=power_analysis_name)
    main_workflow.base_dir = main_path
    
    print "main_path %s" % main_path
    
    ## Info source
    infosource = create_infosource()
    datasource = create_datasource()
    main_workflow.connect(infosource, 'subject_id', datasource, 'subject_id')
    main_workflow.connect(infosource, 'condition', datasource, 'condition')
    power_node = pe.Node(interface=Power(), name='pwr')
    power_node.inputs.fmin = 0;
    power_node.inputs.fmax = 300;
    power_node.inputs.method = 'welch'

    main_workflow.connect(datasource, 'epo_file', power_node, 'epochs_file')
    return main_workflow

# def main():
#     pipeline = pe.Workflow(name='test')
#     pipeline.base_dir = './'
#     epochs_file = '/home/dmalt/Github/python/pipeline/neuropype_ephy/neuropype_ephy/tests/test-epo.fif'
#     test_node = pe.Node(interface=Power(), name='pwr')
#     test_node.inputs.epochs_file = epochs_file
#     test_node.run()

if __name__ == '__main__':
    main_workflow = create_main_workflow_power()
    main_workflow.run()