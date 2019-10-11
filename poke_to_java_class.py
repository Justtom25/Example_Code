###########################################################################################################################################################################################################
#Author: Tom Cheairs
#Last Modified: 10/11/2019
#Purpose: To convert .txt of Pokemon into a Java class
#Last Change: Finished Capability list and tested. Working on move array and output. Adding and reworking comments 
###########################################################################################################################################################################################################
import  os

#\t is tab
#\n is new line

def construct(file, name):# creates the base constructor class and writes the begining info and name
	n = open(file, "w+") #Opens the new file
	n.write("public class " + name + " extends Pokemon{\n") #Creates the public class with pokeomon name

	n.write( "\t\t" + 'name = "' + name + '";\n') #Provides the name var in the constructor


list = [] #Array used to store all the words in the file 
id = 0 #id for the array
num = 0 #Var used for ablities 
unwanted = [':', '/', '-', ',', '"', "'", '%'] #certain chars to remove to keep consistency 
currentEVO = 'previous' #Sets all evolutions to previous till current evo is find
currentReq = 'prevReq'	#Sets previous level requirements

for subdir, dirs, files in os.walk('./'): #Checks for each file in a folder that this program is in
	for file in files: #checks each file
		ext =  file[-4:] #checks for the .exetension 
		if  ext == ".txt": # only accepts .txt files
			#print(file) #debug 
			print("Starting " + file)
			f = open(file, "r") #allows python to read data in the file
			name = file[:-4] #Pulls the Pokemon name
			file = name + ".java" # Creates a name for the new java file
			n = open(file, "a+") #Creates a java file for the Pokemon
			construct(file, name) #calls the function providing file name and pokemon name
			line = f.readline() #Reads each line in the file
			for line in f: #will go through each line in the text file
				for word in line.split(): #Will go through each file
					for u in unwanted: 
						word = word.replace(u, '')
					if word != '':
						list.append(word)#adds each word into the array
			while id < (len(list) - 1): #Goes through each word in the array
				#print(list)#Debug
				id = id + 1 # goes through each id on the array
				if list[id] == "Stats": #Checks for the base stat block
					Nid = id + 2 #sets the array to where the HP stat is 
					n.write( "\t\tbHP = " + str(list[Nid]) + ";\n") #sets up the bHP var
					Nid = Nid + 2 #goes to atk stat
					n.write( "\t\tbAtk = " + str(list[Nid]) + ";\n") #sets up the bAtk var
					Nid = Nid + 2 #goes to Def stat
					n.write( "\t\tbDef = " + str(list[Nid]) + ";\n") #sets up the bDef var
					Nid = Nid + 3 #goes to bSpAtk stat
					n.write( "\t\tbSpAtk = " + str(list[Nid]) + ";\n") #sets up the bSpAtk var
					Nid = Nid + 3 #goes to bSpDef stat
					n.write( "\t\tbSpDef = " + str(list[Nid]) + ";\n") #sets up the bSpDef var
					Nid = Nid + 2 #goes to bSpd stat
					n.write( "\t\tbSpd = " + str(list[Nid]) + ";\n") #sets up the bSpd var
					id = Nid
				if list[id] == "Type":
					Nid = id + 1
					n.write( "\t\ttype1 = " + '"' + str(list[Nid]) + '";\n') #sets up the type1 var
					Nid = Nid + 1
					if list[Nid] == "/":
						Nid = Nid + 1
						n.write( "\t\ttype2 = " + '"' + str(list[Nid]) + '";\n') #sets up the type2 var
					else:
						n.write( "\t\ttype2 = " + '"' + '";\n')
						Nid = Nid - 1
					id = Nid
				if list[id] == "Ability": #Checks for Ability
					Nid = id + 2
					if list[Nid] == "Evolution":
						if list[Nid - 2] == "Ability":
							Nid = Nid - 1
						if list[Nid - 3] == "Ability":	
							Nid = Nid - 1
					nword = list[Nid]
					Nid = Nid + 1
					if list[Nid] == "Adv":
						Nid = Nid - 1
					if list[Nid] == "Basic":
						Nid = Nid - 1
					if list[Nid] == "High":
						Nid = Nid - 1
					if Nid != (id + 2):
						if list[Nid] != 'Evolution':
							nword = nword + " " + str(list[Nid])
					num += 1
					n.write( "\t\tabilities" + str(num) + " = " + '"' + nword + '";\n') #sets up the Ability skill
					id = Nid
				if list[id] == "Evolution":
					Nid = id + 1 #Moves to find if there are evolutions
					if list[Nid] == "1":
						Nid = Nid + 1
						if list[Nid] != name: #sees if this is the Pokemon current evolution
							n.write( "\t\t" + currentEVO + " = " + str(list[Nid]) + ';\n') #sets up the previous Evolution
							n.write( "\t\t" + currentReq + " = " + str(list[Nid + 4]) + ';\n') #sets up the previous Evolution level
						if list[Nid] == name:
							currentEVO = "next"
							currentReq = "nextReq"
					Nid = Nid + 1
					if list[Nid] == '2':
						Nid = Nid + 1
						if list[Nid] != name: #sees if this is the Pokemon current evolution
							n.write( "\t\t" + currentEVO + " = " + str(list[Nid]) + ';\n') #sets up the previous Evolution
							Nid = Nid + 2
							n.write( "\t\t" + currentReq + " = " + str(list[Nid]) + ';\n') #sets up the previous Evolution level
						if list[Nid] == name:
							currentEVO = "next"
							currentReq = "nextReq"
							Nid = Nid + 2
					Nid = Nid + 1
					if list[Nid] == '3':
						Nid = Nid + 1
						if list[Nid] != name: #sees if this is the Pokemon current evolution
							n.write( "\t\t" + currentEVO + " = " + str(list[Nid]) + ';\n') #sets up the previous Evolution
							Nid = Nid + 2
							n.write( "\t\t" + currentReq + " = " + str(list[Nid]) + ';\n') #sets up the previous Evolution level
				if list[id] == "Height":
					Nid = id + 1
					foot = list[Nid]
					foot = foot[:-1] #Removes the first number
					Nid = Nid + 1
					inch = list[Nid]
					inch = inch[:-1] #Removes the first number
					n.write( "\t\theight = " + '"' + str(foot) + "\\'" + "/" + str(inch) + '\\"' +'";\n')
				if list[id] == "(Small)": #Looking for weight class
					n.write( "\t\tsize = " + '"' + "Small" + '";\n')
				if list[id] == "(Meduim)":
					n.write( "\t\tsize = " + '"' + "Meduim" + '";\n')
				if list[id] == "(Large)":
					n.write( "\t\tsize = " + '"' + "Large" + '";\n')	
				if list[id] == "(Huge)":
					n.write( "\t\tsize = " + '"' + "Huge" + '";\n')	
				if list[id] == "Weight":
					Nid = id + 1
					n.write( "\t\tweight = " + str(list[Nid]) + ';\n')
					Nid = Nid + 3
					wc = list[Nid]
					wc = wc[:-1]
					wc = wc[-1:]
					n.write( "\t\tWC = " + wc + ';\n')
				if list[id] == 'Ratio': # Looks for Gender ratio
					Nid = id + 1
					Male = list[Nid]
					Nid = Nid + 2
					Female = list[Nid]
					n.write( "\t\tmaleRatio = " + Male + ';\n')
					n.write( "\t\tfemaleRatio = " + Female + ';\n')
				if list[id] == 'Group': #Looking for egg group
					Nid = id + 1
					Egggroup = list[Nid]
					n.write( "\t\tegg1 = " + '"' + Egggroup + '";\n')
					Nid = Nid + 1
					Egggroup = list[Nid]
					n.write( "\t\tegg2 = " + '"' + Egggroup + '";\n')
				if list[id] == 'Habitat': #Looking for Habitat
					Nid = id + 1 
					habitat1 = '"' + list[Nid] + '", '
					Nid = Nid + 1
					habitat2 = '"' + list[Nid] + '", '
					Nid = Nid + 1
					habitat3 = '"' + list[Nid] + '"'
					n.write( "\t\thabitats = " + '{' + habitat1 + habitat2 + habitat3 + '};\n')
				if list[id] == 'Capability': #Looking for each Capability in the list. If it is not found it will add it with the corresponding skill of 0
					Nid = id + 2
					if list[Nid] == 'Overland':
						Nid = Nid + 1
						n.write( "\t\toverland = " + list[Nid] + ';\n')
						Nid = Nid - 1
					if list[Nid] != 'Overland':
						n.write( "\t\toverland = " + '0' + ';\n')
						Nid = Nid - 2
					Nid = Nid + 2
					if list[Nid] == 'Swim':
						Nid = Nid + 1
						n.write( "\t\tswim = " + list[Nid] + ';\n')
						Nid = Nid - 1
					if list[Nid] != 'Swim':
						n.write( "\t\tswim = "+ '0' +  ';\n')
						Nid = Nid - 2
					Nid = Nid + 2
					if list[Nid] == 'Levitate':
						Nid = Nid + 1
						n.write( "\t\tlevitate = " + list[Nid] + ';\n')
						Nid = Nid - 1
					if list[Nid] != 'Levitate':
						n.write( "\t\tlevitate = " + '0' + ';\n')
						Nid = Nid - 2
					Nid = Nid + 2
					if list[Nid] == 'Sky':
						Nid = Nid + 1
						n.write( "\t\tsky = " + list[Nid] + ';\n')
						Nid = Nid - 1
					if list[Nid] != 'Sky':
						n.write( "\t\tsky = " + '0' + ';\n')
						Nid = Nid - 2
					Nid = Nid + 2
					if list[Nid] == 'Burrow':
						Nid = Nid + 1
						n.write( "\t\tburrow = " + list[Nid] + ';\n')
						Nid = Nid - 1
					if list[Nid] != 'Burrow':
						n.write( "\t\tburrow = " + '0' + ';\n')
						Nid = Nid - 2
					Nid = Nid + 2
					if list[Nid] == 'Jump':
						Nid = Nid + 1
						Jump = list[Nid]
						n.write( "\t\tlJump = " + Jump[:-1] + ';\n')
						n.write( "\t\thJump = " + Jump[-1:] + ';\n')
						Nid = Nid - 1
					if list[Nid] != 'Jump':
						n.write( "\t\tlJump = " + '0' + ';\n')
						n.write( "\t\thJump = " + '0' + ';\n')
						Nid = Nid - 2
					Nid = Nid + 2
					if list[Nid] == 'Power':
						Nid = Nid + 1
						n.write( "\t\tpower = " + list[Nid] + ';\n')
						Nid = Nid - 1
					if list[Nid] != 'Power':
						n.write( "\t\tpower = " + '0' + ';\n')
						Nid = Nid - 2
					Nid = Nid + 2
					if list[Nid] == 'Naturewalk': 
						Nid = Nid + 1
						walk = list[Nid]
						natureWalk = 'natureWalk = {' #Looks for the natureWalk. Since there is no set number it will keep adding till a ) is found
						print(walk[:-1])
						if walk[:1] == '(':
							walk = walk[1:]
							while True:
								if walk[-1:] == ')':
									natureWalk = natureWalk + '"' + walk[:-1] + '"}'
									Nid = Nid + 1
									break
								natureWalk = natureWalk + '"' + walk + '", '
								Nid = Nid + 1
								walk = list[Nid]
							n.write( "\t\t" + natureWalk + ';\n')
					if list[Nid] == 'Underdog':
						n.write( "\t\tunderdog = " + '"' + 'true' + '";\n')
					if list[Nid] != 'Underdog':
						n.write( "\t\tunderdog = " + '"' + 'false' + '";\n')
					Nid = Nid + 1
					other = '\t\tother = {'#Looks for any fringe case skills
					if list[Nid] != 'Skill':
						other = other + '"' + list[Nid] + '",'
						Nid = Nid + 1
					if list[Nid] == "Skill":
						other = other[:-1]
						n.write(other + '};\n')
				if list[id] == 'Skill':	# Functions like Capability set with the added ability to remove the skill die bonus
					Nid = id + 2
					if list[Nid] == 'Athl':
						Nid = Nid + 1
						athl = list[Nid]
						n.write( "\t\tathl = " + athl[:1] + ';\n')
						if athl[3::2] == '+':
							athl = athl[-1:]
						else:
							athl = '0'
						Nid = Nid - 1
					Nid = Nid + 2
					if list[Nid] == 'Acro':
						Nid = Nid + 1
						acro = list[Nid]
						n.write( "\t\tacro = " + acro[:1] + ';\n')
						print(acro[3::2])
						if acro[3::2] == '+':
							acro = acro[-1:]
						else:
							acro = '0'
						Nid = Nid - 1
					Nid = Nid + 2
					if list[Nid] == 'Combat':
						Nid = Nid + 1
						combat = list[Nid]
						n.write( "\t\tcombat = " + combat[:1] + ';\n')
						if combat[3::2] == '+':
							combat = combat[-1:]
						else:
							combat = '0'
						Nid = Nid - 1
					Nid = Nid + 2
					if list[Nid] == 'Stealth':
						Nid = Nid + 1
						stealth = list[Nid]
						n.write( "\t\tstealth = " + stealth[:1] + ';\n')
						if stealth[3::2] == '+':
							stealth = stealth[-1:]
						else:
							stealth = '0'
						Nid = Nid - 1
					Nid = Nid + 2
					if list[Nid] == 'Percep':
						Nid = Nid + 1
						percep = list[Nid]
						n.write( "\t\tpercep = " + percep[:1] + ';\n')
						if percep[3::2] == '+':
							percep = percep[-1:]
						else:
							percep = '0'
						Nid = Nid - 1
					Nid = Nid + 2
					if list[Nid] == 'Focus':
						Nid = Nid + 1
						focus = list[Nid]
						n.write( "\t\tfocus = " + focus[:1] + ';\n')
						if focus[3::2] == '+':
							focus = focus[-1:]
						else:
							focus = '0'
						Nid = Nid - 1
					n.write( "\t\tathlBouns = " + athl + ';\n')
					n.write( "\t\tacroBonus = " + acro + ';\n')				
					n.write( "\t\tcombatBouns = " + combat + ';\n')
					n.write( "\t\tstealthBonus = " + stealth + ';\n')				
					n.write( "\t\tpercepBouns = " + percep + ';\n')
					n.write( "\t\tfocusBonus = " + focus + ';\n')
				if list[Nid] == 'Move': #Move set array. Work in progress. 
					Nid = Nid + 1
					while list[Nid] != 'TM':
						try:
							level = int(list[Nid])
							levelNumber.append(level)
						except TypeError:
							pass
						if list[Nid] in type:
							moveName = moveName[:-1]
							moves.append(moveName)
							moveName = ''
						else:
							moveName = list[Nid] + '_'
						Nid = Nid + 1
					n.write( "\t\tmoves = {" + moves +'"};\n')

			
			print(list)
			f.close()
			n.write("\t" + name + "(){\n") #Begins the Constructor
			n.write("\t\tsuper();\n")
			n.write("\t}\n")
			n.write("}")
			n.close()
			num = 0
			print("Finished " + file)
	