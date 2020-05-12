x=['X','X','X']
o=['O','O','O']
p1='X'
ai='O'
# X is player
# O is AI
# T is tie
score={
	'X': int(1),
	'O': int(-1),
	'T':int(0)
}
def PosWin(maze):
	for i in range(3):
		for j in range(3):
			if(maze[i][j]==''):
				return ''
	for i in maze:
		if i==x:
			return 'X'
		elif(i==o):
			return 'O'
	if(maze[0][0]=='X' and maze[1][1]=='X' and maze[2][2]=='X'):
		return 'X'
	elif(maze[0][2]=='X' and maze[1][1]=='X' and maze[2][0]=='X'):
		return 'X'
	elif(maze[0][0]=='O' and maze[1][1]=='O' and maze[2][2]=='O'):
		return 'O'
	elif(maze[0][2]=='O' and maze[1][1]=='O' and maze[2][0]=='O'):
		return 'O'
	for i in range(len(maze)):
		if([maze[j][i] for j in range(len(maze))]==x):
			return 'X'
	for i in range(len(maze)):
		if([maze[j][i] for j in range(len(maze))]==o):
			return 'O'
	return 'T'
def minmax(maze,turn):

def bestmove(maze):
	for i in range(3):
		for j in range(3):
			if(maze[i][j]==''):
				maze[i][j]='O'
				a=minmax(maze,'')
				maze[i][j]=''
	maze[a[0]][a[1]]='O'

def main():	
	mat=[['','','X'],['','',''],['','','']]
	print(maze)
	while('' in maze):
		i,j=map(int,input().split())
		maze[i][j]='X'
		bestmove(maze)

	print(PosWin(mat))


if __name__== "__main__":
	main()

