import os
import sys

'''
This script uses magenta to automatically convert .midi files to SequenceExample objects, which magenta uses as the base object to train on.
You should include two arguments when running the script, the first will specify the input directory for your midi files, the second should specify the output directory of your SequenceExample objects.

e.g. python gen_sequence_examples.py my_input_dir my_output_dir

@author: An Wang 8/12/18
'''

EVAL_RATIO = 0.1
input_dir = sys.argv[1]
output_dir = sys.argv[2]
tmp_note_sequences = "tmp/note_sequences.tfrecord"
os.system("INPUT_DIRECTORY=" + input_dir)
os.system("OUTPUT_DIRECTORY=" + output_dir)
os.system("EVAL_RATIO=" + EVAL_RATIO)
os.system("$SEQUENCES_TFRECORD=" + tmp_note_sequences)

note_sequences_cmd = "convert_dir_to_note_sequences --input_dir=$INPUT_DIRECTORY --output_file=$SEQUENCES_TFRECORD --recursive"
os.system(note_sequences_cmd)

sequence_examples_cmd = "melody_rnn_create_dataset --config=lookback_rnn --input=$SEQUENCES_TFRECORD --output_dir=$OUTPUT_DIRECTORY --eval_ratio=$EVAL_RATIO"
os.system(sequence_examples_cmd)s