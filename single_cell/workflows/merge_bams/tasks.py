'''
Created on Jul 24, 2017

@author: dgrewal
'''
import pypeliner


def merge_bams(inputs, output, config):
    filenames = inputs.values()
    
    
    cmd = [config['picard'], '-Xmx12G',
           'MergeSamFiles',
           'OUTPUT=' + output,
           'SORT_ORDER=coordinate',
           'ASSUME_SORTED=true',
           'VALIDATION_STRINGENCY=LENIENT',
           ]
    for bamfile in filenames:
        cmd.append('I='+bamfile)
    
    pypeliner.commandline.execute(*cmd)