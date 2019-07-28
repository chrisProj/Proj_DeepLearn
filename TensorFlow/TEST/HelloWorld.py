import tensorflow as tf

# 创建对象
hello_constant = tf.constant("Hello world!")

A = tf.constant(1234)

B = tf.constant([123])

with tf.Session() as sess:
    # 在Session中运行 tf.constant
    output = sess.run(hello_constant)
    print(output)