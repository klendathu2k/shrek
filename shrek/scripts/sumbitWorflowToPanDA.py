#!/usr/bin/env python

import yaml
import argparse
import pydot
import os
import pathlib
import shutil
import glob
import getpass
import uuid
import datetime
import subprocess

from shrek.scripts.buildJobScript import buildJobScript
from shrek.scripts.buildCommonWorklow import buildCommonWorkflow
from shrek.scripts.buildSubmissionDirectory import buildSubmissionDirectory

def main():

    parser = argparse.ArgumentParser(description='Build job submission area')
    parser.add_argument('yaml', metavar='YAML', type=str, nargs="+",
                                        help='input filename')
    parser.add_argument('--tag',  type=str, help='production tag' )
    parser.add_argument('--submit',    dest='submit', action='store_true')
    parser.add_argument('--no-submit', dest='submit', action='store_false')
    parser.set_defaults(submit=False)

    parser.add_argument('--vo', type=str, default='wlcg')
    parser.add_argument('--prodSourceLabel', type=str, default='test')
    parser.add_argument('--workingGroup', type=str,default="sphenix")
    parser.add_argument('--user', type=str,default=getpass.getuser())

    args = parser.parse_args()

    (subdir,cwlfile,yamlfile) = buildSubmissionDirectory( args.tag, args.yaml )

    pchain = [ "pchain" ]

    #pchain = "cd %s; pchain " % subdir

    pchain . append( '--vo %s'%args.vo )
    pchain . append( '--workingGroup %s'%args.workingGroup )
    pchain . append( '--prodSourceLabel %s'%args.prodSourceLabel )
    taguuid = args.tag + '-' + str(uuid.uuid1())
    pchain . append('--outDS user.%s.%s'%( args.user, taguuid ) )
    pchain . append('--cwl %s'%cwlfile )
    pchain . append('--yaml %s'%yamlfile )

    pcheck = pchain
    pcheck .append ( '--check' )

    # Run pchain with --check option to validate against PanDA prior to submission
    #   output is captured
    #   exit code is tested and exception raised if nonzero
    pcheck_result = subprocess.run( ' '.join(pcheck), shell=True, cwd=os.path.abspath(subdir), capture_output=True, check=False )

    # We are now ready to submit the job.  First log everything to a tag file...
    # (can be updated to a local DB)

    # Create a "tag file" which will ride along with the job 
    with open( subdir + '/' + taguuid, 'w' ) as f:
        f.write('SHREK Job Submission %s'%str(datetime.datetime.now()))
        f.write('\ncmd args: ')
        f.write('\n')        
        f.write(str(args))
        f.write('\nsubdir: ')
        f.write('\n')        
        f.write(os.path.abspath(subdir))
        f.write('\ntag: ')
        f.write('\n')        
        f.write(taguuid)
        f.write('\ncheck:')
        f.write('\n')
        f.write(str(pcheck_result.stdout))
        f.write('\n')
        f.write(str(pcheck_result.stderr))

    pchain_result = None
    if args.submit and pcheck_result.returncode==0:
        pchain_result = subprocess.run( ' '.join(pchain), shell=True, cwd=os.path.abspath(subdir), capture_output=True, check=False )
        with open( subdir + '/' + taguuid, 'a' ) as f:
            f.write('\nsubmit:')
            f.write('\n')
            f.write(str(pchain_result.stdout))
            f.write('\n')
            f.write(str(pchain_result.stderr))
        

    

if __name__ == '__main__':
    main()
    
