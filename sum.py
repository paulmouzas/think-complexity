import os

def etime():
        user, sys, chuser, chsys, real = os.times()
        return user+sys