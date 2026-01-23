biologicalSex = input("Enter the biological sex (Male/Female): ")
hemoglobinLevel = float(input("Enter the hemoglobin level (g/L): "))
if biologicalSex == "Male":
    if hemoglobinLevel < 134:
        print("The person's hemoglobin value is low")
    elif hemoglobinLevel > 167:
        print("The person's hemoglobin value is high")
    else:
        print("The person's hemoglobin value is normal")
elif biologicalSex == "Female":
    if hemoglobinLevel < 117:
        print("The person's hemoglobin value is low")
    elif hemoglobinLevel > 155:
        print("The person's hemoglobin value is high")
    else:
        print("The person's hemoglobin value is normal")
else:
    print("Invalid biological sex entered.")