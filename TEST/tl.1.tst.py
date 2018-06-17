tl = [('k1','v1'),('k2','v21'),('k2','v22'),('k2','v23'),('k3','v3'),('k2','v24'),('k4','v4')]
tltl._remove_which(tl,1,key='k2')
t.remove_which(2,key='k2')

tl = [('k1','v1'),('k2','v21'),('k2','v22'),('k2','v23'),('k3','v3'),('k2','v24'),('k4','v4')]
tltl.uniqualize(tl,"k2")
t = tltl.Tlist(tl)
t.uniqualize("k2")

tl = [('k1', 'v1'), ('k2', 'v21'), ('k2', 'v22'), ('k2', 'v23'), ('k3', 'v3'), ('k2', 'v24'), ('k4', 'v4'), ('k3', 'v32')]
tltl.uniqualize_all(tl)
t = tltl.Tlist(tl)
t.uniqualize_all()
