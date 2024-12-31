import subprocess
from LabelMap import *


command_1 = [
    "python",
    f"{SCRIPTS_PATH}/generate_tfrecord.py",
    "-x", f"{IMAGE_PATH}/train",
    "-l", f"{ANNOTATION_PATH}/label_map.pbtxt",
    "-o", f"{ANNOTATION_PATH}/train.record"
]


command_2 = [
    "python",
    f"{SCRIPTS_PATH}/generate_tfrecord.py",
    "-x", f"{IMAGE_PATH}/test",
    "-l", f"{ANNOTATION_PATH}/label_map.pbtxt",
    "-o", f"{ANNOTATION_PATH}/test.record"
]

subprocess.run(command_1, check=True)
subprocess.run(command_2, check=True)




