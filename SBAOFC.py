import os
import sys

print "code by Eight"
print "SB animated object files creator v1.4"

values = ["objectName", "description", "shortDescription", "race", "dropItem", "category", "image", "imagePath", "imagePosition", "frames", "animationcycle", "spaceScan", "anchors", "size", ]

def setValue(valueName, format, default)	:
	value = None
	while value == None:
		display = valueName + " (" + format + ") > " + str(default) + chr(8) * len(str(default))
		value = raw_input(display)
		if value == "" and default != "":
			result = default
		else:
			try:
				if format == "String":
					result = value
				if format == "Integer":
					value = int(value)
					result = value
				if format == "Decimal":
					value = float(value)
					result = value
				if format == "Image":
					result = value #WIP
			except:
				value = None
	return result

curDir = os.getcwd()
AsItOb = curDir + "/" + "assets_items_object"

preMade = raw_input("Drag pre-made object file here or press enter to create new> ")
if preMade != "":
	try:
		loadedFile = open(preMade, "r")
		objectName = loadedFile.readline()
		description = loadedFile.readline()
		shortDescription = loadedFile.readline()
		race = loadedFile.readline()
		dropItem = loadedFile.readline()
		category = loadedFile.readline()
		image = loadedFile.readline()
		imagePath = loadedFile.readline()
		imageIconPath = loadedFile.readline()
		imagePosition = loadedFile.readline()
		frames = loadedFile.readline()
		animationCycle = loadedFile.readline()
		spaceScan = loadedFile.readline()
		anchors = loadedFile.readline()
		size = loadedFile.readline()
		names_all = loadedFile.readline()
		rarity = loadedFile.readline()
	except:
		print "Could not load files"
	preMade = ""
else:
	if 1 + 1 == 2:
		objectName = setValue("Object Name", "String", "")
		dotObjectFolder = curDir + "/" + objectName
		if os.path.exists(dotObjectFolder):
			print "Item already exists!"
			if raw_input("Overwrite data? (Y/N)>") == "Y":
				files = os.listdir(dotObjectFolder)
				for objectFile in files:
					os.remove(dotObjectFolder + "/" + objectFile)
				os.rmdir(dotObjectFolder)
				dotObjitemLocation = AsItOb + "/" + objectName + ".frames"
				objectIconPngLocation = AsItOb + "/" + objectName + "/" + objectName + "icon.png"
				if os.path.exists(dotObjitemLocation):
					os.remove(dotObjitemLoction)
				if os.path.exists(objectIconPngLocation):
					os.remove(objectDotIconPngLocation)
	else:
		print "failed to remove files"
		sys.exit()
	description = setValue("Description", "String", "")
	shortDescription = setValue("Short Description", "String", "")
	race = setValue("Race", "String", "Human")
	dropItem = setValue("Drop Item", "String", objectName)
	category = setValue("Category", "String", "decorative")
	imagePosition = [None,None]
	imagePosition[0] = setValue("X offset", "Decimal", 0)
	imagePosition[1] = setValue("Y offset", "Decimal", 0)
	frames = setValue("Frames", "Integer", 1)
	print frames
	animationCycle = setValue("Animation Cycle", "Decimal", 0.1)
	spaceScan = setValue("Space Scan", "Decimal", 0.1)
	anchors = setValue("Anchors", "String", "Background")
	size = [None,None]
	size[0] = setValue("Width", "Interger", 8)
	size[1] = setValue("Height", "Interger", 8)
	dimentions = [frames,1]
	names_all = setValue("Frame names", "String", "default")
	names = []
	nameCount = 0
	while nameCount < int(dimentions[0]) + 1:
		names.append(names_all + str(nameCount))
		nameCount = nameCount + 1
	itemName = objectName
	rarity = setValue("Rarity", "String", "common")
	inventoryIcon = objectName + "icon.png"
	imagePath = setValue("Tile sheet (WIP, leave blank)", "Image", " ")
	imageIconPath =setValue("Inventory Icon (WIP, leave blank)", "Image", " ")

print "Saving..."
print "creating object folder"
odotOjectFolder = curDir + "/" + objectName
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
if imagePath != " ":
	imageLocation = AsItOb + "/" + objectName + ".png"
	originalFile = open(imagePath, "r")
	saveFile = open(imageLocation, "w+")
	saveFile.write(originalFile)
	saveFile.close

if imageIconPath != " ":
	originalFile = open(imageIconLPath, "r")
	imageIconLocation = AsItOb + "/" + objectName + "icon.png"
	saveFile = open(imageIconLocation, "w+")
	saveFile.write(originalFile)
	saveFile.close
print "Complete"
if raw_input("create share file? (Y/N)> ") == "Y":
	preMadeFile = objectName + "\n"
	description + "\n"
	shortDescription + "\n"
	race + "\n"
	dropItem + "\n"
	category + "\n"
	image + "\n"
	imagePath + "\n"
	imageIconPath + "\n"
	imagePosition + "\n"
	frames + "\n"
	animationCycle + "\n"
	spaceScan + "\n"
	anchors + "\n"
	size + "\n"
	names_all + "\n"
	rarity
