import tensorflow as tf

x = tf.placeholder(tf.float32, shape = [1,1])
m = tf.matmul(x, x)

with tf.Session() as sess:
	m_out = sess.run(m, feed_dict = {x:[[2.0]]})

print(m_out)