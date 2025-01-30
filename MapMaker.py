from random import randint as RR

map0 = [
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
'                                        ',
]

mapborder = [0, len(map0)-1]
len
Rooms = {
	0 : {
	# s-size, x y-borders
	# if size x is greater than y, take s as x size. y will be held below.
		's' : 2,
		'x' : 3,
		'y' : 3,
		'tiles' : {
			1:'11',
			2:'1 ',
			},
		},
	1 : {
		's' : 2,
		'x' : 3,
		'y' : 3,
		'tiles' : {
			1:' 1',
			2:'11',
			},
		},
	2 : {
		's' : 3,
		'x' : 4,
		'y' : 4,
		'tiles' : {
			1:'1 1',
			2:'  1',
			3:'111',
			},
		},
	3 : {
		's' : 4,
		'x' : 5,
		'y' : 5,
		'tiles' : {
			1:'1111',
			2:'1  1',
			3:'   1',
			4:'11 1',
			},
		},
	4 : {
		's' : 4,
		'x' : 5,
		'y' : 5,
		'tiles' : {
			1:'1 11',
			2:'1   ',
			3:'1  1',
			4:'1 11',
			},
		},
	5 : {
		's' : 5,
		'x' : 6,
		'y' : 6,
		'tiles' : {
			1:'1 111',
			2:'1    ',
			3:'1  11',
			4:'    1',
			5:'111 1',
			},
		},
	6 : {
		's' : 6,
		'x' : 7,
		'y' : 7,
		'tiles' : {
			1:'  1111',
			2:'1 1  1',
			3:'1    1',
			4:'     1',
			5:'11    ',
			6:' 11111',
			},
		},
	7 : {
		's' : 11,
		'x' : 12,
		'y' : 12,
		'tiles' : {
			1:'    1 1    ',
			2:'  111 111  ',
			3:' 11     11 ',
			4:'11   1   11',
			5:'1    1    1',
			6:'11       11',
			7:'1   111   1',
			8:'1    1    1',
			9:'1 1  1  1 1',
		   10:'     1    1',
		   11:'11111111111',
			},
		},
	8 : {
		's' : 11,
		'x' : 12,
		'y' : 10,
		'tiles' : {
			1:'1 1     1 1',
			2:'  1111111  ',
			3:' 11     11 ',
			4:'11       11',
			5:'1         1',
			6:'11       11',
			7:' 11     11 ',
			8:'  11   11  ',
			9:'1    1    1',
			},
		},
	9 : {
		's' : 6,
		'x' : 7,
		'y' : 7,
		'tiles' : {
			1:'  1111',
			2:'111   ',
			3:'1    1',
			4:'1  111',
			5:'1    1',
			6:'1111 1',
			},
		},
	10 : {
		's' : 6,
		'x' : 7,
		'y' : 7,
		'tiles' : {
			1:' 1 1 1',
			2:'   1  ',
			3:'1 1 1 ',
			4:'  1  1',
			5:'1  1  ',
			6:'  1  1',
			},
		},
	11 : {
		's' : 6,
		'x' : 7,
		'y' : 7,
		'tiles' : {
			1:'11  11',
			2:'1    1',
			3:'      ',
			4:'      ',
			5:'1    1',
			6:'11  11',
			},
		},
	12 : {
		's' : 6,
		'x' : 7,
		'y' : 7,
		'tiles' : {
			1:'  11  ',
			2:'1    1',
			3:'  11  ',
			4:'  11  ',
			5:'1    1',
			6:'  11  ',
			},
		},
	13 : {
		's' : 3,
		'x' : 4,
		'y' : 4,
		'tiles' : {
			1:' 1 ',
			2:'111',
			3:' 1 ',
			},
		},
	14 : {
		's' : 3,
		'x' : 4,
		'y' : 4,
		'tiles' : {
			1:'111',
			2:'   ',
			3:'111',
			},
		},
	15 : {
		's' : 3,
		'x' : 4,
		'y' : 4,
		'tiles' : {
			1:'1 1',
			2:'1 1',
			3:'1 1',
			},
		},
	16 : {
		's' : 3,
		'x' : 4,
		'y' : 4,
		'tiles' : {
			1:'1 1',
			2:' 1 ',
			3:'1 1',

			},
		},
	17 : {
		's' : 5,
		'x' : 4,
		'y' : 4,
		'tiles' : {
			1:'11 11',
			2:' 1 1 ',
			3:' 1 1 ',
			4:'11 11',
			},
		},
}
class WorldGen:
	def __init__(self, map, b1, b2, rooms):
		#map0, b1 b2 start and end of map y0 and y-last
		self.map = map
		self.b1 = b1
		self.b2 = b2
		self.rooms = rooms
		self.custom_coords = [] #all free space
		self.room_coords = [] #room free space
		
		self.CreateBorder(self.map, self.b1, self.b2)
		self.CreateRoom(self.map, self.rooms)
		
	def CreateBorder(self, data, s1, s2):
		for y, tiles in enumerate(data):
			# y-position, tiles-part of map
			for x, item in enumerate(tiles):
				# x-position, item-single tile
				if y == s1:
					# if its first or last row make it a wall "1111111"
					tiles = '1'*len(map0[0])
				elif y == s2:
					tiles = '1'*len(map0[0])
				else:
					#make a wall for each left columns "1     1"
					tiles = tiles[-1:0]+'1 '+tiles[1+1:-1]+'1'	
			self.map[y] = tiles
	
	def SpaceCheck(self, x, y, l, data, rt): #x.y on map0, Rooms[n]['s'], map0, Rooms[n]
		spcrd = [] #coordinates
		my = y-1
		mx = x-1 #custom positions for border so there are no collisions
		check = False
		for crd in range(l+2): #+2 because we are making border and we have already y-1
			for crd1 in range(l+2):
				#adding only coordinates on map the size of room + border
				spcrd.append([mx+crd1,my])
			my += 1
		for col in spcrd:
			#checking each tile for free space
			if data[col[1]][col[0]] == ' ':
				check = True
			else:
				check = False
				break
		if check == True:
			return spcrd
		else:
			return False
	
	def PlaceRoom(self, x, y, rtype, map): #x.y on map0, Rooms[n], map0
		for i in range(1,rtype['s']+1):
			#replace each row with slice of room
			map[y] = map[y][:x]+rtype['tiles'][i]+map[y][x+rtype['s']:]
			y += 1
			self.room_coords.append([x, y])
		self.map = map
	
	def CreateRoom(self, data, rt): #map0, Rooms
		for y, tiles in enumerate(data):
			for x, item in enumerate(tiles):
				try:
					#random rooms
					nwrm = rt[RR(0,18)]
					if data[y][:x] + ' ' + data[y][x+1:] == data[y]:
						# checking for free tile and sending coords
						coords = self.SpaceCheck(x, y, nwrm['s'], data, nwrm)
						if coords == False:
							pass
						else:
							self.PlaceRoom(x, y, nwrm, data)
				except IndexError:
					continue
				except KeyError:
					continue
		self.map = data
		for y, tiles in enumerate(data):
			for x, item in enumerate(tiles):
				if item == ' ':
					self.custom_coords.append([x, y])
#for z in range(1,10):
#	mapp = WorldGen(map0.copy(), mapborder[0], mapborder[1], Rooms,)
#	for i in mapp.map:
#		print(i)
