import os
import time

class ResultModifier(object):
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, file='flag.txt'):
        self.flag = file

    def start_test(self, data, test):
      # wait condition to start the test, this should typically be a call to a graphana alert.
      while not os.path.isfile(self.flag):
        time.sleep(20)

    def end_test(self, data, test):
         # check if test conditions degraded druing the run, if so, add a tag to the tests results, this should typically be the same call as above
        if not os.path.isfile(self.flag):
            test.tag.add("unstable")
            test.message = 'System became unavailable during the test'
