try: 
    f_dti = open("myfile01.txt", "r", encoding="utf-8")
    data = f_dti.readlines()

    for data_by_line in data:
        print(f"B: {data_by_line}", end='')

except Exception:
    print("Exception found. Restart.")
finally:
    print("Finished reading.")
    f_dti.close()