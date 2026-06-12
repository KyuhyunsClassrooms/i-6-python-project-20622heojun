# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 

# ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 아래 예시는 "활동 추천 프로그램"입니다.
# 자신의 주제에 맞게 data를 만드세요.
#
# 현재 열의 의미:
# 0번 열: 활동 이름
# 1번 열: 필요한 시간(분)
# 2번 열: 추천 기분
# 3번 열: 활동 유형
# ------------------------------------------------------------

# 1. 프로그램에서 사용할 전체 할 일 목록을 2차원 리스트로 만듭니다.
# 구조: [ [작업이름, 남은일수, 완료여부], [작업이름, 남은일수, 완료여부] ]
tasks = []

# [함수 1] 새 할 일을 입력받아 리스트에 추가하는 함수
def add_task(task_list):
    print("\n--- 2. 새 할 일 추가하기 ---")
    
    # 1. 사용자에게 할 일 이름과 D-Day 입력받기
    task_name = input("할 일 이름을 입력하세요: ")
    d_day = int(input("남은 기간(D-Day 숫자)을 입력하세요: "))
    
    # 2. 새로운 할 일 정보를 한 행(리스트)으로 묶기
    new_task = [task_name, d_day, "N"]
    
    # 3. 전체 리스트에 추가하기 (빈칸을 알맞은 함수로 채워보세요!)
    task_list.append(new_task)
    
    print(f"'{task_name}' 작업이 성공적으로 추가되었습니다!")
    
    # 4. 데이터가 바뀐 리스트를 돌려주기
    return task_list


# [함수 2] 현재 등록된 모든 할 일 목록을 보여주는 함수
def show_dashboard(task_list):
    print("\n--- 1. 현재 할 일 목록 ---")
    
    # 만약 리스트가 비어있다면 안내 메시지 출력
    if len(task_list) == 0:
        return # 함수를 종료하고 돌아감
        
    # 반복문(for)을 사용해 2차원 리스트의 각 행을 하나씩 꺼내어 출력
    for i in range(len(task_list)):
        # task_list[i][0]: 작업이름, task_list[i][1]: D-Day, task_list[i][2]: 완료여부
        print(f"[{i+1}번] 작업명: {task_list[i][0]} | D-Day: {task_list[i][1]} | 완료여부: {task_list[i][2]}")
# ... 메뉴판 print 출력 부분 생략 ...
def complete_task(task_list):
    print("\n--- 3. 할 일 완료 체크 ---")
    show_dashboard(task_list)
    
    # 1. 일단 사용자가 입력한 번호를 숫자로 바꿉니다.
    user_input = int(input("완료한 작업의 번호를 입력하세요: "))
    task_num = user_input - 1
    
    # 2. [핵심] 입력한 번호가 리스트 범위 안에 있는지 검사합니다!
    # 번호가 0보다 작거나, 리스트의 총 개수(len) 이상이면 없는 번호입니다.
    if task_num < 0 or task_num >= len(task_list):
        print(f"\n🚨 [오류] {user_input}번 작업은 존재하지 않습니다. 올바른 번호를 입력해 주세요.")
        return task_list  # 아무것도 수정하지 않고 리스트를 그대로 돌려줌 (프로그램 안 튕김!)
        
    # 3. 올바른 번호일 때만 "Y"로 변경합니다.
    task_list[task_num][2] = "Y"
    
    print(f"[{user_input}번] 작업이 성공적으로 완료 처리되었습니다!")
    return task_list

def check_urgent_tasks(task_list):
    print("\n--- 4. 마감 임박 (D-3 이하) 미완료 작업 ---")
    
    # 1. 등록된 할 일이 아예 없으면 미리 안내하고 종료
    if len(task_list) == 0:
        print("등록된 할 일이 없습니다. 먼저 할 일을 등록해 주세요.")
        return
        
    urgent_count = 0
    
    # 2. 리스트 순회 검사
    for i in range(len(task_list)):
        # 안전장치: 혹시 D-Day가 정수가 아닌 문자열로 들어가 있다면 정수로 변환 시도
        try:
            d_day = int(task_list[i][1])
        except ValueError:
            # 숫자로 바꿀 수 없는 데이터면 건너뜀
            continue
            
        status = task_list[i][2]
        
        # 3. [조건 검사] 남은 기간이 3일 이하이고, 완료 여부가 "N"인 경우
        if d_day <= 3 and status == "N":
            print(f"🚨 [긴급] 작업명: {task_list[i][0]} | 남은기간: D-{d_day}")
            urgent_count += 1
            
    # 4. 검사가 끝난 후 긴급 작업이 하나도 없다면 출력
    if urgent_count == 0:
        print("현재 마감이 임박한 미완료 작업이 없습니다.👍")

# [추가 기능 1] 프로젝트 진행률 계산 및 시각화 함수
def show_progress(task_list):
    if len(task_list) == 0:
        print("📊 현재 프로젝트 진행률: 등록된 작업이 없습니다.")
        return

    completed_count = 0
    # 전체 리스트를 돌며 완료("Y")된 작업의 개수를 셉니다.
    for task in task_list:
        if task[2] == "Y":
            completed_count += 1
            
    # 진행률 계산 공식: (완료된 개수 / 전체 개수) * 100
    progress_rate = (completed_count / len(task_list)) * 100
    
    # 로딩바(그래프) 모양 만들기 (10칸 기준)
    bar_length = int(progress_rate // 10)
    progress_bar = "██" * bar_length + "░░" * (10 - bar_length)
    
    print(f"📊 현재 프로젝트 진행률: [{progress_bar}] {progress_rate:.1f}% ({completed_count}/{len(task_list)} 완료)")


# [추가 기능 2] 선택한 할 일을 리스트에서 지우는 함수
def delete_task(task_list):
    print("\n--- 6. 할 일 삭제하기 ---")
    show_dashboard(task_list)
    
    if len(task_list) == 0:
        return task_list
        
    user_input = int(input("삭제할 작업의 번호를 입력하세요: "))
    task_num = user_input - 1
    
    # 안전장치: 없는 번호를 입력했는지 검사
    if task_num < 0 or task_num >= len(task_list):
        print(f"\n🚨 [오류] {user_input}번 작업은 존재하지 않습니다.")
        return task_list
        
    # 리스트에서 특정 위치의 요소를 삭제하는 pop() 내장 함수 사용!
    deleted = task_list.pop(task_num)
    print(f"🗑️ '{deleted[0]}' 작업이 성공적으로 삭제되었습니다.")
    
    return task_list


# 2. 사용자가 종료를 선택할 때까지 무한히 반복하는 메뉴판입니다.
while True:
    print("\n====== 프로젝트 일정 관리기 ======")
    print("1. 할 일 목록 보기 (진행률 포함)")
    print("2. 새 할 일 추가하기")
    print("3. 할 일 완료 체크")
    print("4. 마감 임박 긴급 작업 확인")
    print("5. 할 일 삭제하기")  # 새 메뉴 추가!
    print("6. 프로그램 종료")   # 종료 번호 변경!
    print("=================================")
    
    menu = input("원하는 기능의 번호를 입력하세요: ")
    
    if menu == "1":
        show_dashboard(tasks)
        show_progress(tasks)  # 목록 보여준 뒤 진행률도 같이 출력!
        
    elif menu == "2":
        tasks = add_task(tasks)
      
    elif menu == "3":
        tasks = complete_task(tasks)
        
    elif menu == "4":
        check_urgent_tasks(tasks)
        
    elif menu == "5":
        tasks = delete_task(tasks)  # 삭제 함수 연동!
        
    elif menu == "6":
        print("\n프로그램을 종료합니다. 수고하셨습니다!")
        break
        
    else:
        print("\n[오류] 잘못된 번호입니다. 1~6 사이의 숫자를 입력해 주세요.")
