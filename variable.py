import tensorflow as tf

my_state = tf.Variable(0, name = "counter")
one = tf.constant(1)
new_value = tf.add(my_state, one)
update = tf.assign(my_state, new_value)

init_Op = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init_Op)
	print(sess.run(my_state))
	for _ in range(3):
		sess.run(update)
		print(sess.run(my_state))