This script does everything that the interal DRUMS batch option does, but faster. 

It sources PNG images from MISC_2 of the school and does the following actions:

-- Creates a temp folder in MISC_2 for working images
-- Composites all images onto schoolday background1 using Pillow, saving them into temp
-- Copies all composites JPG images from temp into the following relaltive paths at correct size.
---- <./VERIFIED_IMAGES> 320x400
---- <./VERIFIED_IMAGES_LARGE> 640x800
---- <./THUMBNAILS> 140x175
-- Copies just "*_1.JPG" images into <./COMPOSITE_IMAGES> with size 640x800
-- Moves PNG images from MISC_2 into <./MISC_1>
-- Deletes temp folder from MISC_2
