import os
import logging as log
from pathlib import Path
from datetime import datetime

from app.config import Config

# logger 설정.
def setup_logger(set_level=log.INFO) -> log.Logger:
    '''
    Args:
        set_level (int): logger의 최소 로깅 레벨을 지정.
    Returns:
        Logging.Logger: 설정된 핸들러가 추가된 logger 객체.
    '''
    logger: log.Logger = log.getLogger(__name__)
    logger.setLevel(set_level)

    # logger 객체에 파일 핸들러, 콘솔 핸들러가 포함되어 있지 않을 경우,
    if not logger.handlers:
        namefmt: str = f'{datetime.now().strftime('%Y%m%d%H%M%S%f')}.log'
        filename: Path = os.path.join(Config.LOG_PATH / namefmt)

        formatter: log.Formatter = log.Formatter(
            fmt='[%(asctime)s]%(name)s: %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # log 파일에 로그를 기록하는 FileHandler 객체 생성.
        file_handler: log.FileHandler = log.FileHandler(
            filename=filename,
            encoding='utf-8'
        )
        file_handler.setLevel(set_level)
        file_handler.setFormatter(formatter)

        # 콘솔에 로그를 출력하는 StreamHandler 객체 생성.
        console_handler: log.StreamHandler = log.StreamHandler()
        console_handler.setLevel(set_level)
        console_handler.setFormatter(formatter)

        # 설정된 핸들러를 logger에 추가.
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger