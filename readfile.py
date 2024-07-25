def read_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # 줄바꿈 문자를 제거하고 리스트에 저장
    lines = [line.strip() for line in lines]
    return lines

# 예시 사용법
file_path = 'cipher.txt'  # 여기에 파일 경로를 입력하세요
lines_list = read_file_to_list(file_path)
print(lines_list)
