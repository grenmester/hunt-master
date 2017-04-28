# HuntMaster
HuntMaster is a modular framework made to create puzzle hunts at the intersection of reality and technology.

The creation of HuntMaster came about through an interest in puzzle/scavenger hunts. Our team desired to bring digital media into these kinds of experiences and to make it easy for anyone else to do so.

## What it does
With HuntMaster, it's easy to create custom experiences known as hunts. You provide the story and tasks, HuntMaster does the heavy lifting.

Want to create a guided tour of your campus? Make a hunt that directs players to various parts of your campus and automatically proceeds to the next part of the tour when they reach them by using their GPS. All you need to do is write a few lines of python, the instructions/descriptions, and deploy using HuntMaster.

Want to play a cross between Bingo and a scavenger hunt where players are tasked with taking pictures of randomized items (e.g. basketballs, muffins) to cross them off their Bingo card? If you write the Bingo game logic, it's just a matter of interfacing with HuntMaster and then deploying.

Most setup for a hunt is done in python, although if you want your resulting page to look nice it's worth writing some HTML/CSS. Currently HuntMaster supports feature detection of images (e.g. determining whether a picture for the hypothetical Bingo hunt is valid), GPS location tracking, image comparison, QR code generation, as well as basic forms of input (text, buttons, etc.). Interfacing with these functions is often a matter of a single call.

## How we built it
HuntMaster is built for the most part on python 2.7. It hosts a Flask server with a Bootstrap front-end. When a player in the hunt submits something, it's relayed to a python function which connects to whichever API is needed for that particular part of the hunt. If, for example, the player is tasked with finding an image of a dog, when she finds it and sends it to the server, the server then queries Google's Vision API to determine the contents of the picture. If it is of a dog, she'll receive the next part of the hunt.

Regarding modules,
* Feature detection is done through Google's Vision API
* GPS-based location tracking is done through HTML5
* Image comparison is done through OpenCV (specifically feature tracking with SIFT)
* QR Code generation is done through the `qrcode` python module

## Links

Demo: [https://seek-165508.appspot.com](https://seek-165508.appspot.com)

Devpost: [https://devpost.com/software/huntmaster](https://devpost.com/software/huntmaster)

---

HuntMaster was created by Jacky Lee, Cole Kurashige, and Owen Gillespie
