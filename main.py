from PIL import Image
import os

matching_files = []
errors = []

root = input("Enter the root : ")
min_size_for_compression = int(input("Enter the miminum size of image to be compressed (IN BYTES) : "))


for path, subdirs, files in os.walk(root):

    for name in files:
        matching_files.append(os.path.join(path, name))
        print(path, end=' ')
        print(name)

input("\n\nList of all files in the given location obtained. Press enter to start compression : ")



for image in matching_files:
	try:
		if os.path.getsize(image) > min_size_for_compression:
			im = Image.open(image)
			im.save(image, format="JPEG", quality=50)
			print("{} compressed.".format(image))
		else:
			print("{} skipped from compression. File size already less than given miminum".format(image))
	except Exception as e:
		print("{} had following error : {}".format(image, e))
		errors.append(image)

if len(errors) > 0:
	print("\n\n{} files could not be processed. They are : \n".format(len(errors)))

	for item in errors:
		print(item)

else:
	print("\n\nAll files processed successfully.")
