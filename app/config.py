import os
from pathlib import Path

class Config:
    # 디렉토리 경로 설정.
    BASE_PATH: Path = Path(__file__).parent.parent
    DATA_PATH: Path = BASE_PATH / 'statements'
    LOG_PATH: Path = DATA_PATH / 'logs'

    def __init__(self):
        self._create_directories()

    @classmethod
    def _create_directories(cls):
        '''
        Args:
            cls: 클래스 자체를 참조하는 클래스 메서드 인자.
        Returns:
            None
        '''
        os.makedirs(cls.DATA_PATH, exist_ok=True)
        os.makedirs(cls.LOG_PATH, exist_ok=True)

# 프로그램 실행 시 디렉토리 생성 보장.
Config._create_directories()