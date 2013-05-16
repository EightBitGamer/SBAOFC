import os

print "code by Eight"
print "SB animated object files creator v1.4"

curDir = os.getcwd()
AsItOb = curDir + "/" + "assets_items_object"

objectName = None
description = None
shortDescription = None
race = None
dropItem = None
category = None
image = None
imagePosition = None
frames = None
animationCycle = None
spaceScan = None
anchors = None
size = None
names_all = None
rarity = None
while objectName == None:
	objectName = raw_input("Object name (String)> ")
	dotObjectFolder = curDir + "/" + objectName
	if objectName == "":
		objectName = None
	else:
		try:
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
		except:
			print "failed to remove files" 
			objectName = None
while description == None:
	try:
		description = raw_input("Long description (String)> ")
	except:
		description = None
while shortDescription == None:
	try:
		shortDescription = raw_input("Short description (String)> ")
	except:
		shortDescription = None
while race == None:
	try:
		race = raw_input("Race > ")
	except:
		race = None
while dropItem == None:
		try:
			dropItem = raw_input("Name of item (String)> " + objectName + chr(8) * len(objectName))
			if dropItem == "":
				dropItem = objectName
		except:
			dropItem = None
else:
	dropItem = objectName
while category == None:
	try:
		category = raw_input("Category (String)> decorative" + chr(8) * 10)
		if category == "":
			category = "decorative"

	except:
		catagory = None
image = str(objectName) + ".png"
while imagePosition == None:
	try:
		imagePosition = [raw_input("X axis offset (Decimal)> 0" + chr(8)), raw_input("Y axis offset (Decimal)> 0" + chr(8))]
		if imagePosition[0] == "":
			imagePosition[0] = 0
		else:
			imagePosition[0] = float(imagePosition[0])
		if imagePosition[1] == "":
			imagePosition[1] = 0
		else:
			imagePosition[1] = float(imagePosition[1])
	except:
		imagePosition = None
while frames == None:
	try:
		frames = int(raw_input("Number of frames (integer)> "))
	except:
		frames = None
while animationCycle == None:
	try:
		animationCycle = raw_input("Cycle frames (Decimal)> 0.1" + chr(8) * 3)
		if animationCycle == "":
			animationCycle = 0.1
		else:
			animationCycle = float(animationCycle)
	except:
		animationCycle = None
while spaceScan == None:
	try:
		spaceScan = raw_input("Space Scan (Decimal)> 0.1" + chr(8) * 3)
		if spaceScan == "":
			spaceScan = 0.1
		else:
			spaceScan = float(spaceScan)
	except:
		spaceScan = None
while anchors == None:
	try:
		anchors = raw_input("Background or Foreground (String)> ")
	except:
		anchors = None
while size == None:
	try:
		size = [raw_input("Width (Integer)> 8" + chr(8)), raw_input("Height (Integer)> 8" + chr(8))]
		if size[0] == "":
			size[0] = 8
		else:
			size[0] = int(size[0])
		if size[1] == "":
			size[1] = 8
		else:
			size[1] = int(size[1])
	except:
		size = None
dimentions = [frames,1]
while names_all == None:
	try:
		names_all = raw_input("Frame names (String)> ")
	except:
		names_all = None
names = []
nameCount = 0
while nameCount < int(dimentions[0]) + 1:
	names.append(names_all + str(nameCount))
	nameCount = nameCount + 1
itemName = objectName
rarity = raw_input("Rarity (String)> ")
inventoryIcon = objectName + "icon.png"

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
