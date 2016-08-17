import ms
from curses import wrapper

def putLineToScr(stdscr, line, linexp, fl):
	#stdscr.addstr(line)
	for c in range(len(line)):
		if linexp[c]:
			stdscr.addch(line[c])
		elif fl[c]:
			stdscr.addch('!')
		else:
			stdscr.addch(' ')
	stdscr.addch('\n')







def main(stdscr):
	loop = True
	status = 0
	x = 0
	y = 0
	stdscr.addstr('Commands:')
	stdscr.addstr('  o - open\n')
	stdscr.addstr('  f - flag\n')
	stdscr.addstr('  u - unflag\n')
	stdscr.addstr('  e - open all nearby fields that are not flagged\n')
	stdscr.addstr('  q - quit\n')

	while loop:
		try:
			#stdscr.addstr(str(x)+str(y))
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
				board = ms.buildCurrentState(ms.board)
				for n in range(len(board)):
					putLineToScr(stdscr, board[n], ms.explored[n], 
ms.flagged[n])
				stdscr.addch(y,x, ' ')
				if ms.checkIsFinished():
					print 'You won!'
					loop = False
		except ValueError:
			print 'Invalid value'



wrapper(main)
