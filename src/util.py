from google.cloud import storage

def gcs_head(bucket_name: str, file_path: str, character_code: str) -> None:
    """
    GCS上のcsvの先頭1MBだけをダウンロードして出力する
    
    input
    bucket_name: str
        gcsのbucket
    file_path: str
        オブジェクトへのパス
    character_code: str
        オブジェクトの文字コード（downloadしたものはバイナリなのでファイルの中身を出力しようと思うとdecodeする必要がある）
    """
    gcs_blob = storage.Client().bucket(bucket_name).blob(file_path)
    head: bytes = gcs_blob.download_as_bytes(end=100000)
    print(head.decode(character_code))


gcs_head(bucket_name="dataflow_takerumimata", file_path="sjis.txt", character_code="shift-jis")