import ms
from curses import wrapper


def main(stdscr):
	loop = True
	status = 0
	x = 0
	y = 0
	print 'Commands:'
	print '    o - open'
	print '    f - flag'
	print '    u - unflag'
	print '    e - open all nearby fields that are not flagged'
	print '    q - quit'


	#stdscr.clear()

	while loop:
		try:
			print x, y
			c = stdscr.getkey()
			stdscr.clear()
			if c == 'o':
				status = ms.explore(int(y),int(x))
			elif c == 'f':
				ms.flag(int(y),int(x))
			elif c == 'u':
				ms.unflag(int(y),int(x))
			elif c == 'e':
				status = ms.search(int(y),int(x))
			elif c == 'q':
				print 'Quit'
				loop = False
				break
			elif c == 'w':
				y-=1
			elif c == 'a':
				x-=1
			elif c == 's':
				y+=1
			elif c == 'd':
				x+=1
			else:
				print 'Unknown command:',c
			
			if status == -1:
				#ms.printEnd(ms.board)
				print 'You just lost!'
				loop = False
			else:
				#ms.printCurrentState(ms.board)
				if ms.checkIsFinished():
					print 'You won!'
					loop = False
		except ValueError:
			print 'Invalid value'



wrapper(main)
