import zipfile 
import shutil

file_zip = zipfile.ZipFile("fichier_excel.zip", 'w', zipfile.Z_DEFLATED)
file_zip.write("octobre.xslx")
file_zip.write("novembre.xslx")
file_zip.write("decembre.xslx")
file_zip.close()

# shutil.make_archive("fichiers_excel2.zip", "extraction_zip")
shutil.unpack_archive("fichiers_excel2.zip", "extraction_zip")