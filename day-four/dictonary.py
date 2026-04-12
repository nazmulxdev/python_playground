info = {
    "name": "Nazmul",
    "Age": 24,
    "class": "B.SC",
    "marks": [2, 3, 55],
    "cgpa": (
        3.25,
        3,
    ),
    4: "NAZMUL",
    True: "fALSE",
}

print(info)

print(type(info))

print(info["name"])

info["name"] = "fuck"

print(info)

null_dict = {}

null_dict["name"] = None

print(null_dict)


nested_dict = {
    "name": "Nazmul",
    "exam": "Fifth semester",
    "score": {"phy": 98, "che": 95, "math": 99},
}


print(nested_dict)

print(nested_dict["score"]["math"])
nested_dict["address"] = {}

nested_dict["address"]["village"] = "Konda"
nested_dict["address"]["thana"] = "Savar"
nested_dict["address"]["Distict"] = "Dhaka"

print(nested_dict)

print(list(nested_dict.values()))

print(nested_dict.items())
print(isinstance(nested_dict, int))

nested_dict.update({"isValid": {"age": 20}})

print(nested_dict)
