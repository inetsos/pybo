
#strftime 인풋 string을 유니코드 인코딩 후 디코딩
#strftime 아웃풋 string 을 인코딩 후 유니코드 디코딩

# ‘%Y년 %m월 %d일’.encode(‘unicode-escape’).decode()
# strftime( ~ ).encode().decode(‘unicode-escape’))

# print(today.strftime('%Y년 %m월 %d일'.encode('unicode-escape').decode()).encode().decode('unicode-escape'))

def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'):
    return value.strftime(fmt.encode('unicode-escape').decode()).encode().decode('unicode-escape')
