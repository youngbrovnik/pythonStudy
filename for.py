# for.py

data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result = {}
for blood_type in data:
    if blood_type in result:  # 키 값이 존재하는 경우에는 기존 값에 더함
        result[blood_type] += 1
    else:  # 키 값이 없는 경우에는 새로운 키 생성
        result[blood_type] = 1
print(result)