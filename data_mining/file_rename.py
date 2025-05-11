import pandas as pd
import numpy as np
import seaborn as sns


# csv파일 이름 읽으되 한글 깨짐 방지 
def read_csv_auto_encoding(filepath):
    """
    한글이 포함된 CSV 파일을 자동으로 적절한 인코딩(cp949 또는 utf-8)으로 읽습니다.
    
    Parameters:
        filepath (str): CSV 파일 경로

    Returns:
        pd.DataFrame: 읽은 데이터프레임
    """
    try:
        # 먼저 utf-8로 시도
        return pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            # 실패하면 cp949로 시도 (Excel 저장 기본값)
            return pd.read_csv(filepath, encoding='cp949')
        except UnicodeDecodeError as e:
            print("인코딩 오류: utf-8 및 cp949 모두 실패")
            raise e
        
def read_excel_file(filepath, sheet_name=0):
    """
    한글이 포함된 Excel (.xlsx) 파일을 읽습니다.

    Parameters:
        filepath (str): Excel 파일 경로 (.xlsx)
        sheet_name (str or int): 읽을 시트 이름 또는 인덱스 (기본: 0번째 시트)

    Returns:
        pd.DataFrame: 읽은 데이터프레임
    """
    try:
        return pd.read_excel(filepath, sheet_name=sheet_name)
    except Exception as e:
        print(f"❌ Excel 파일 읽기 오류: {e}")
        raise e
    
import requests

# API에서 데이터를 가져오는 함수 
def fetch_api_data(url: str, params: dict = None, headers: dict = None) -> dict:
    """
    API에서 데이터를 가져오는 함수.

    Parameters:
        url (str): API 요청 URL
        params (dict): 쿼리 파라미터 (예: {"query": "value"})
        headers (dict): 요청 헤더 (예: {"Authorization": "Bearer <token>"})

    Returns:
        dict: JSON 형식으로 변환된 응답 데이터
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 오류 발생: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 실패: {e}")
    except ValueError:
        print("JSON 디코딩 실패")
    return {}

    
