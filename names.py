def f(n):
	print '     local n in f is',id(n),n
	n = n + 1

a = 0
print 'global a before f is',id(a),a
f(a)
print ' global a after f is',id(a),a
