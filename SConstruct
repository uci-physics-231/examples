env = Environment()
env['BUILDERS']['Example'] = Builder(action = './shtowiki.py -i $SOURCE',
	suffix='.textile',src_suffix='.sh')

env.Example('git-internals')
env.Example('git-workflow')

# use scons -c to cleanup
