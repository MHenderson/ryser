# Copyright Matthew Henderson 2013.
# Created Tue Mar 26 10:02:38 GMT 2013
# Last updated: Tue Mar 26 10:10:48 GMT 2013

def extend(P, w, t, e):
    """
    P - a KF-SPLS
    w - wing dimension
    t - tail dimension
    e - tether dimension
    """
    if w==4:
        return {5:2,6:5,13:5,14:6,21:1,22:8,29:6,30:7,33:2,34:5,35:1,\
                36:6,37:8,41:5,42:6,43:8,44:7,46:2}
    else:
        return {7:6,8:8,15:8,16:7,23:2,24:3,31:1,32:2,39:7,40:4,47:4,\
                48:1,49:6,50:8,51:2,52:1,53:7,54:4,55:3,57:8,58:7,59:3,\
                60:2,61:4,62:1,64:6}

