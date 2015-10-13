import os
from nose.tools import assert_equals, with_setup
from dronekit_sitl import SITL

sitl = SITL('copter', '3.3-rc5')
sitl_args = ['-I0', '--model', 'quad', '--home=-35.363261,149.165230,584,353']

if 'SITL_SPEEDUP' in os.environ:
	sitl_args += ['--speedup', str(os.environ['SITL_SPEEDUP'])]
if 'SITL_RATE' in os.environ:
	sitl_args += ['-r', str(os.environ['SITL_RATE'])]

def setup_sitl():
    sitl.launch(sitl_args, await_ready=True, restart=True)

def teardown_sitl():
    sitl.stop()

def with_sitl(fn):
    @with_setup(setup_sitl, teardown_sitl)
    def test(*args, **kargs):
        return fn('tcp:127.0.0.1:5760', *args, **kargs)
    return test
