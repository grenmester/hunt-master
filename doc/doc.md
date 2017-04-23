# Documentation

## General fields
**url:** A string with the url for this module, i.e. `/content/demo`.

**target:** A string with the url for the target module that this module links to.

**data:** A dictionary with additional data fields depending on the type of module.  More info can be found below.

## Data fields

content
-------
**html:** A string containing the html for the page.

gps
---
**x_coordinate:** The x-coordinate of the trigger location.

**y_coordinate:** The y-coordinate of the trigger location.

find
----
**object_name:** The name of the object being looked for in the picture.

match
-----
**image_filename:** The filename of the image that the user is trying to match with their uploaded image.

qr
--
**html:** A string containing the html for the page.

text
----
**correct_string:** The string that must be entered into the text box to continue
