import sched, time
from compare import run_compare

s = sched.scheduler(time.time, time.sleep)

# Seconds
sec = 8


def run(sc, sec):
    run_compare()
    s.enter(sec, 1, run, (sc, sec))

s.enter(5, 1, run, (s, sec))
s.run()

