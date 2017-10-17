import tensorflow as tf

sess = tf.Session()
hello = tf.constant('Hello, TensorFlow')
print(sess.run(hello))
print(str(sess.run(hello), encoding='utf-8'))