import datetime
l = [
    {"type": "Purchase", "date": datetime.date(2025, 12, 1), "amount": 110001},
    {"type": "Sale", "date": datetime.date(2024, 12, 31), "amount": 234142},
    {"type": "Purchase", "date": datetime.date(2025, 1, 29), "amount": 50234},
    {"type": "Purchase", "date": datetime.date(2025, 1, 10), "amount": 87654},
    {"type": "Sale", "date": datetime.date(2025, 1, 29), "amount": 123456},
    {"type": "Sale", "date": datetime.date(2023, 5, 22), "amount": 65432},
    {"type": "Purchase", "date": datetime.date(2024, 3, 8), "amount": 76453},
    {"type": "Sale", "date": datetime.date(2022, 6, 11), "amount": 98231},
    {"type": "Purchase", "date": datetime.date(2025, 1, 29), "amount": 43212},
    {"type": "Sale", "date": datetime.date(2020, 10, 13), "amount": 98765},
    {"type": "Purchase", "date": datetime.date(2023, 2, 25), "amount": 56123},
    {"type": "Sale", "date": datetime.date(2022, 4, 17), "amount": 89321},
    {"type": "Purchase", "date": datetime.date(2021, 7, 30), "amount": 67894},
    {"type": "Sale", "date": datetime.date(2025, 1, 29), "amount": 23412},
    {"type": "Purchase", "date": datetime.date(2019, 8, 14), "amount": 76543},
    {"type": "Sale", "date": datetime.date(2018, 11, 9), "amount": 87654},
    {"type": "Purchase", "date": datetime.date(2017, 3, 21), "amount": 34211},
    {"type": "Sale", "date": datetime.date(2016, 5, 19), "amount": 91234},
    {"type": "Purchase", "date": datetime.date(2015, 10, 8), "amount": 67345},
    {"type": "Sale", "date": datetime.date(2014, 12, 27), "amount": 98723},
    {"type": "Purchase", "date": datetime.date(2013, 6, 15), "amount": 45321},
    {"type": "Sale", "date": datetime.date(2012, 9, 22), "amount": 78912},
    {"type": "Purchase", "date": datetime.date(2011, 4, 3), "amount": 65432},
    {"type": "Sale", "date": datetime.date(2010, 8, 19), "amount": 43219},
    {"type": "Purchase", "date": datetime.date(2025, 1, 29), "amount": 56124}
]



print(sum((1 for i in l if i["date"] == datetime.date(2025, 1, 29))))
print(sum((i["amount"] if i["type"] == "sell" else -i["amount"] for i in l if i["date"] == datetime.date(2025, 1, 29))))
