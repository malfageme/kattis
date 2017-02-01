import sys

h_now, m_now=map(int,sys.stdin.readline().split())

m_new=m_now-45
h_new=h_now-(1 if m_new<0 else 0)

print "{} {}".format(h_new%24, m_new%60)
