import pandas as pd
data = pd.read_json("data.json")

lenn = len(data)
for i in range(lenn):
    name = data.get("Username Github")[i]
    option = data.get("Bạn đang học lớp nào (Nêu không học thì chọn mục không) [LopHoc]")[i]
    option = str(option)
    fullname = data.get("Họ và Tên")[i]
    lop = data.get("Tên Lớp (Viết in hoa, không dấu cách. Ví dụ: CNTT1-K62)")[i]
    check = data.get("Check")[i]
    check = str(check)
    print(check)