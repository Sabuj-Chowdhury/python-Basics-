dict_example ={
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "grades": {
        "Math": 90,
        "Science": 85,
        "History": 88
    },
    "is_active": True,
    "enrollment_date": "2023-01-01",
    "graduation_date": None,   
}

dict_example["age"]= 18

# print(dict_example.get("age"))

# for info in dict_example:
#     print(info , dict_example[info])

# another way of doing the same thing
# for key,value in dict_example.items():
#     print(key,value)

print(len(dict_example))
