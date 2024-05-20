def check_jumin(jumin):
    # 입력된 주민등록번호가 13자리인지 확인
    if len(jumin) != 13 or not jumin.isdigit():
        return False

    # 각 자리의 가중치
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    # 마지막 자리를 제외한 나머지 자리 곱하고 합하기
    total = sum(int(jumin[i]) * weights[i] for i in range(12))

    # 11로 나눈 나머지 값을 구하고, 11에서 빼기
    remainder = total % 11
    check_digit = (11 - remainder) % 10

    # 계산된 체크 숫자와 마지막 자리 숫자 비교
    return check_digit == int(jumin[-1])


# 사용자로부터 주민등록번호 입력받기
jumin = input("주민등록번호 13자리를 입력하세요 (예: 9901011234567): ")

# 유효성 검사 결과 출력
if check_jumin(jumin):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")