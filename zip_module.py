import zipfile


def zip_main(file_location,paswd):

	with zipfile.ZipFile(file_location) as fi:
		fi.extractall(pwd= bytes(paswd,'utf-8'))


zip_main("/home/dan/Downloads/Foundations.zip","123456")

