try: 
    f_dti = open("myfile01.txt", "r", encoding="utf-8")
    data = f_dti.readline()
    print(data, end='')
    data = f_dti.readline()
    print(data, end='')

except Exception:
    print("Exception found. Restart.")
finally:
    print("Finished reading.")
    f_dti.close()