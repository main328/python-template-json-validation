import argparse

def parse_args() -> argparse.Namespace:
    '''
    Args:
        None
    Returns:
        argparse.Namespace: 파싱된 명령줄 인자를 담고 있는 Namespace 객체.
    '''
    # ArgumentParser 설정.
    parser = argparse.ArgumentParser()
    # --input_json 설정.
    parser.add_argument(
        '--input_json',
        type=str,
        required=True,
        help='JSON DATA 파일 경로를 입력하시기 바랍니다.'
    )
    # --input_schema 설정.
    parser.add_argument(
        '--input_schema',
        type=str,
        required=True,
        help='JSON SCHEMA 파일 경로를 입력하시기 바랍니다.'
    )

    return parser.parse_args()

def main():
    args = parse_args()

if __name__ == '__main__':
    main()