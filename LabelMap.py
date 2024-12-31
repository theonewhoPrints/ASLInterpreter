"""
Label Map creation for TensorFlow model


"""
import tensorflow as tf
# GLOBAL PATHS
WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'
# commit when we get back






def create_map():
    labels = [{'name': 'hello', 'id': 1}, {'name': 'loveyou', 'id': 2}, {'name': 'joke', 'id': 3}]

    with open(ANNOTATION_PATH + '/label_map.pbtxt', 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')




def main():
    create_map()
main()