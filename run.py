import ms

loop = True
status = 0

print 'Commands:'
print '    o - open'
print '    f - flag'
print '    u - unflag'
print '    s - open all nearby fields that are not flagged'
print '    q - type "q . ." to quit'
print '    TODO'
print 'Example:'
print '    "o 0 1"'
print 'opens box at column 0, row 1'


while loop:
	try:
		c,x,y = raw_input().split(' ')
		if c == 'o':
			status = ms.explore(int(y),int(x))
		elif c == 'f':
			ms.flag(int(y),int(x))
		elif c == 'u':
			ms.unflag(int(y),int(x))
		elif c == 's':
			status = ms.search(int(y),int(x))
		elif c == 'q':
			print 'Quit'
			loop = False
			break
		else:
			print 'Unknown command:',c
		
		if status == -1:
			ms.printEnd(ms.board)
			print 'You just lost!'
			loop = False
		else:
			ms.printCurrentState(ms.board)
			if ms.checkIsFinished():
				print 'You won!'
				loop = False
	except ValueError:
		print 'Invalid value'
