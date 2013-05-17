import os
import sys

print "code by Eight"
print "SB animated object files creator"

values = ["objectName", "description", "shortDescription", "race", "dropItem", "category", "image", "imagePath", "imagePosition", "frames", "animationcycle", "spaceScan", "anchors", "size", ]

def fileExists(objectNameCheck):
	newNameValid = 0
	while newNameValid == 0:
		dotObjectFolder = curDir + "/" + objectNameCheck
		if os.path.exists(dotObjectFolder):
			print "Item already exists!"
			newName = raw_input("Choose a different name (leave blank to overwrite)> ")
			if newName == "" and raw_input("Are you sure you want to delete %s ? (Y/N)>" % objectName):
				files = os.listdir(dotObjectFolder)
				for objectFile in files:
					os.remove(dotObjectFolder + "/" + objectFile)
				os.rmdir(dotObjectFolder)
				dotObjitemLocation = AsItOb + "/" + objectNameCheck + ".frames"
				objectIconPngLocation = AsItOb + "/" + objectNameCheck + "/" + objectNameCheck + "icon.png"
				if os.path.exists(dotObjitemLocation):
					os.remove(dotObjitemLoction)
				if os.path.exists(objectIconPngLocation):
					os.remove(objectDotIconPngLocation)
		else:
			newNameValid = None
	return objectNameCheck

def setValue(valueName, format, default)	:
	value = None
	while value == None:
		display = valueName + " (" + format + ") > " + str(default) + chr(8) * len(str(default))
		value = raw_input(display)
		if value == "" and default != "":
			result = default
			return result
		elif value == "" and default == "":
			value = raw_input(valueName + " does not have a default > ")
			if value == "":
				return ""
		try:
			if format == "String":
				result = value
			if format == "Integer":
				value = int(value)
				result = value
			if format == "Decimal":
				value = float(value)
				result = value
			if format == "Link":
				if value[-1] == " ":
					value = value[:len(value) - 1]
				result = value
		except:
			value = None
	return result

curDir = os.getcwd()
AsItOb = curDir + "/" + "assets_items_object"

imagePosition = [None,None]
size = [None,None]
names = []

preMade = setValue("Drag pre-made object file here or press enter to create new> ", "Link", "none")
if preMade != "none":
	if "debug" == "debug":
		if not os.path.isdir(preMade):
			print "loading file"
			preMadeFiles = [""]
			
		else:
			print "loading files"
			preMadeFiles = os.listdir(preMade)
		for fileI in preMadeFiles:
			print preMadeFiles
			with open(preMade + "/" + fileI, "r") as pmr:
				loadedFile = pmr.read()	
				loadedFiles = loadedFile.split("split", 3)
				loadedDataFile = loadedFiles[0]
				loadedDataFile = loadedDataFile.split("\n")
				objectName = loadedDataFile[1]
				objectName = fileExists(objectName)
				description = loadedDataFile[2]
				shortDescription = loadedDataFile[3]
				race = loadedDataFile[4]
				dropItem = loadedDataFile[5]
				category = loadedDataFile[6]
				imagePath = "pre loaded"
				imageIconPath = "pre loaded"
				imagePosition[0] = float(loadedDataFile[7])
				imagePosition [1]= float(loadedDataFile[8])
				frames = int(loadedDataFile[9])
				animationCycle = float(loadedDataFile[10])
				spaceScan = float(loadedDataFile[11])
				anchors = loadedDataFile[12]
				size[0] = int(loadedDataFile[13])
				size[1] = int(loadedDataFile[14])
				names_all = loadedDataFile[15]
				rarity = loadedDataFile[1]
				imageData = loadedFiles[1]
				imageIconData = loadedFiles[2]
	else:
		print "Could not load files"
		sys.exit()
else:
	objectName = setValue("Object Name", "String", "")
	objectName = fileExists(objectName)
	description = setValue("Description", "String", "")
	shortDescription = setValue("Short Description", "String", "")
	race = setValue("Race", "String", "Human")
	dropItem = setValue("Drop Item", "String", objectName)
	category = setValue("Category", "String", "decorative")
	imagePosition[0] = setValue("X offset", "Decimal", 0)
	imagePosition[1] = setValue("Y offset", "Decimal", 0)
	frames = setValue("Frames", "Integer", 1)
	animationCycle = setValue("Animation Cycle", "Decimal", 0.1)
	spaceScan = setValue("Space Scan", "Decimal", 0.1)
	anchors = setValue("Anchors", "String", "Background")
	size[0] = setValue("Width", "Interger", 8)
	size[1] = setValue("Height", "Interger", 8)
	names_all = setValue("Frame names", "String", "default")
	rarity = setValue("Rarity", "String", "common")
	imagePath = setValue("Tile sheet", "Link", " ")
	imageIconPath =setValue("Inventory Icon", "Link", " ")

dimentions = [frames,1]
itemName = objectName
inventoryIcon = objectName + "icon.png"
nameCount = 0
while nameCount < int(dimentions[0]) + 1:
	names.append(names_all + str(nameCount))
	nameCount = nameCount + 1

print "Saving..."
print "creating object folder"
dotObjectFolder = curDir + "/" + objectName
os.mkdir(dotObjectFolder)

print "Formatting %s.object" % objectName
dotObject = """{"ObjectName" : "%s",
"descritpion" : "%s",
"shortDescription" : "%s",
"race" : "%s",
"dropItem" : "%s",
"category" : "%s",

"orientations" : [
	{
		"image" : "%s.png:{colour}.{frames}",

		"imagePosition" : %r,
		
		"frames" : %d,
		
		"animationCycle" : %d,
		
		"spaceScan" : %d,
		
		"anchors" : "%s"
	}
]
}""" % (objectName, description, shortDescription, race, dropItem, category, objectName, imagePosition, frames, animationCycle, spaceScan, anchors)

print "Saving %s.object" % objectName
dotObjectLocation = curDir + "/" + objectName + "/" + objectName + ".object"
saveFile = open(dotObjectLocation, "w+")
saveFile.write(dotObject)
saveFile.close

print "Formatting %s.frames" % objectName
dotFrames = """{
	"frameGrid" : {
		"size" : %r,
		"dimentions" : %r,
		"names" : [
			%r
		]
	}
}""" % (size, dimentions, names)

print "Saving %s.frames" % objectName
dotFramesLocation = curDir + "/" + objectName + "/" + objectName + ".frames"
saveFile = open(dotFramesLocation, "w+")
saveFile.write(dotFrames)
saveFile.close

print "Fromatting %s.objitem" % objectName
dotObjitem = """{
	"itemName" : "%s",
	"rarity" : "%s",
	"inventoryIcon" : "%s",
	"dropCollision" : [-4.0, -5, 4, 5],
	"descritpion" : "%s",
	"shortDescription" : "%s",
	"race" : "%s",
	"objectName" : "%s",
}""" % (itemName, rarity, inventoryIcon, description, shortDescription, race, objectName)

print "Checking for /assets/items/objects folder (pre-release)"
if not os.path.exists(AsItOb):
	print "Folder not found\nCreating folder"
	os.mkdir(AsItOb)
else:
	print "Folder found"
print "Saving %s.objitem" % objectName
dotObjitemLocation = AsItOb + "/" + objectName + ".objitem"
saveFile = open(dotObjitemLocation, "w+")
saveFile.write(dotObjitem)
saveFile.close
print "Saving Images"
if imagePath != "pre loaded":
	with open(imagePath, "r") as oip:
		imageData = oip.read()
with open(curDir + "/" + objectName + "/" + objectName + ".png", "w") as nip:
	nip.write(imageData)
	if imagePath != "pre loaded":
		oip.close()
	nip.close()

if imageIconPath != "pre loaded":
	with open(imageIconPath, "r") as oiip:
		imageIconData = oiip.read()
with open(AsItOb + "/" + objectName + ".png", "w") as niip:
	niip.write(imageIconData)
	if imageIconPath != "pre loaded":
		oiip.close()
	niip.close()

print "Complete"
preMadeBasicFolder = curDir + "/premadebasic"
preMadeFileBasic = "v1.0\n" + objectName + "\n" + description + "\n" + shortDescription + "\n" + race + "\n" + dropItem + "\n" + category + "\n" + imagePath + "\n" + imageIconPath + "\n" + str(imagePosition[0]) + "\n" + str(imagePosition[1]) + "\n" + str(frames) + "\n" + str(animationCycle) + "\n" + str(spaceScan) + "\n" + anchors + "\n" + str(size[0]) + "\n" + str(size[1]) + "\n" + names_all + "\n" + rarity
if not os.path.exists(preMadeBasicFolder + "/" + objectName):
	if raw_input("create Pre-made object file? (Y/N)> ") == "Y":
		print "Checking for Pre-made Basic folder (pre-release)"
		if not os.path.exists(preMadeBasicFolder):
			print "Folder not found\nCreating folder"
			os.mkdir(preMadeBasicFolder)
		else:
			print "Folder found"
		os.mkdir(preMadeBasicFolder + "/" + objectName)
		saveFile = open(preMadeBasicFolder + "/" + objectName + "/" + objectName + ".pmb", "w")
		saveFile.write(preMadeFileBasic)
		saveFile.close
		if imagePath != "pre loaded":
			with open(imagePath, "r") as oip:
				imageData = oip.read()
				with open(preMadeBasicFolder + "/" + objectName + "/" + objectName + ".png", "w") as nip:
					nip.write(imageData)
					oip.close()
					nip.close()
		else:
			with open(preMadeBasicFolder + "/" + objectName + "/" + objectName + ".png", "w") as nip:
					nip.write(imageData)
					nip.close()

		if imageIconPath != "pre loaded":
			with open(imageIconPath, "r") as oiip:
				imageData = oiip.read()
				with open(preMadeBasicFolder + "/" + objectName + "/" + objectName + "icon.png", "w") as niip:
					niip.write(imageData)
					oiip.close()
					niip.close()
		else:
			with open(preMadeBasicFolder + "/" + objectName + "/" + objectName + "icon.png", "w") as niip:
					niip.write(imageData)
					niip.close()

preMadeFolder = curDir + "/premade"
if not os.path.exists(preMadeFolder + "/" + objectName + ".pmf"):
	if raw_input("create .pof? (experimental) Y/N> ") == "Y":
		print "Checking for Pre-made objects folder"
		if not os.path.exists(preMadeFolder):
			print "Folder not found\nCreating folder"
			os.mkdir(preMadeFolder)
		else:
			print "Folder found"
		with open(imagePath, "r") as oip:
			imageData = oip.read()
			oip.close()
		with open(imageIconPath, "r") as oiip:
			imageIconData = oiip.read()
			oiip.close()
		preMadeFile = "v1.0\n" + objectName + "\n" + description + "\n" + shortDescription + "\n" + race + "\n" + dropItem + "\n" + category + "\n" + str(imagePosition[0]) + "\n" + str(imagePosition[1]) + "\n" + str(frames) + "\n" + str(animationCycle) + "\n" + str(spaceScan) + "\n" + anchors + "\n" + str(size[0]) + "\n" + str(size[1]) + "\n" + names_all + "\n" + rarity
		preMadeFileData = str(preMadeFile) + "split" + str(imageData) + "split" + str(imageIconData)
	
		with open(preMadeFolder + "/" + objectName + ".pmf", "w") as pmfd:
			pmfd.write(preMadeFileData)
			pmfd.close()
