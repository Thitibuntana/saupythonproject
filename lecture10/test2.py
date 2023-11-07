f_dti = open("myfile01.txt", "w", encoding="utf-8")
f_dti.write("Hello\n")
f_dti.write("กกกก\n")
f_dti.write("ดดดด_Hello\n")
f_dti.close()

print("Finished memo.")