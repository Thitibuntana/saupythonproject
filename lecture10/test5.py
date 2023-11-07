try: 
    f_dti = open("myfile01.txt", "r", encoding="utf-8")
    data = f_dti.read()
    print(data)

except Exception:
    print("Exception found. Restart.")
finally:
    print("Finished reading.")
    f_dti.close()