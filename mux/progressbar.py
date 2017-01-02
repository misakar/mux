"""
    progressbar.py
    ``````````````
    mux progressbar
"""
import sys
import time
import threading
import functools
from .highlight import ansi_escape_codes


class MuxProgressBar(threading.Thread):
    """
    class <MuxProgressBar>
        progress bar thread
    """
    def __init__(self, mux_stop, mux_kill):
        self.mux_stop = mux_stop
        self.mux_kill = mux_kill
        super(MuxProgressBar, self).__init__()

    def run(self):
        print('\n'+' '*5+ansi_escape_codes.get('green')+'Loading\033[0m'+'    '),
        sys.stdout.flush()
        i = 0
        while self.mux_stop != True:
            if (i%4 == 0): 
                sys.stdout.write('\b/')
            elif (i%4 == 1): 
                sys.stdout.write('\b-')
            elif (i%4 == 2): 
                sys.stdout.write('\b\\')
            elif (i%4 == 3): 
                sys.stdout.write('\b|')
            sys.stdout.flush()
            time.sleep(0.2)
            i+=1
        if self.mux_kill == True: 
            print('\b\b\b\b '+ansi_escape_codes.get('red')+'Abort!\033[0m'),


def mux_progressbar(task):
    """
    function <mux_progressbar>
        a decorator add progress bar to a task
    """
    @functools.wraps(task)
    def task_wrapper(*args, **kwargs):
        mux_kill = False      
        mux_stop = False
        pb = MuxProgressBar(mux_kill, mux_stop)
        pb.start()
        try:
            # run task
            task(*args, **kwargs)
            pb.mux_stop = True
        except KeyboardInterrupt or EOFError:
            pb.mux_kill = True
            pb.mux_stop = True
    return task_wrapper