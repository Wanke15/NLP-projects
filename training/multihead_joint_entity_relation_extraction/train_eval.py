from training.multihead_joint_entity_relation_extraction import utils
from training.multihead_joint_entity_relation_extraction import tf_utils
from training.multihead_joint_entity_relation_extraction.build_data import build_data
import numpy as np
import tensorflow as tf
import sys
import os.path

'Train the model on the complete train+eval set until the limit specified by ' \
'(1) maximum epochs or (2) early stopping after executing train_es.py, is exceeded'


def checkInputs():
    if (len(sys.argv) <= 3) or os.path.isfile(sys.argv[0])==False :
        raise ValueError(
            'The configuration file and the timestamp should be specified.')

    es_file = sys.argv[3] + "/es_" + sys.argv[2] + ".txt"
    es_epoch= sys.maxsize
    if os.path.isfile(es_file) == True:
        with open(es_file, 'r') as myfile:
            es_epoch = int(myfile.read())
            myfile.close()
    return es_epoch

if __name__ == "__main__":

    es_epoch=checkInputs()


    config=build_data(sys.argv[1])

    config.train_id_docs.extend(config.dev_id_docs)

    
    train_data = utils.HeadData(config.train_id_docs, np.arange(len(config.train_id_docs)))
    test_data = utils.HeadData(config.test_id_docs, np.arange(len(config.test_id_docs)))


    tf.reset_default_graph()
    tf.set_random_seed(1)

    utils.printParameters(config)

    with tf.Session() as sess:
        embedding_matrix = tf.get_variable('embedding_matrix', shape=config.wordvectors.shape, dtype=tf.float32,
                                           trainable=False).assign(config.wordvectors)
        emb_mtx = sess.run(embedding_matrix)

        model = tf_utils.model(config,emb_mtx,sess)

        obj, m_op, predicted_op_ner, actual_op_ner, predicted_op_rel, actual_op_rel, score_op_rel = model.run()

        train_step = model.get_train_op(obj)

        operations=tf_utils.operations(train_step,obj, m_op, predicted_op_ner, actual_op_ner, predicted_op_rel, actual_op_rel, score_op_rel)


        sess.run(tf.global_variables_initializer())

        best_score=0
        nepoch_no_imprv = 0  # for early stopping

        for iter in range(config.nepochs+1):

            model.train(train_data,operations,iter)

            test_score=model.evaluate(test_data,operations,'test')

            print ("\n- Test score {} in {} epoch\n".format(test_score,iter))

            if es_epoch==iter:
                    print("- early stopping after {} epochs".format(iter))
                    break
