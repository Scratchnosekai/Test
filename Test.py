codepoint_ranges = [
    [0x20, 0x7F],         # 英数字、記号、基本的なASCII文字（#を除外）
    [0x3041, 0x3096],     # ひらがな
    [0x30A0, 0x30FF],     # カタカナ
    [0x3400, 0x4DB5],     # 漢字（CJK 追加漢字）
    [0x4E00, 0x9FCB],     # 漢字（CJK Ideographs）
    [0xF900, 0xFA6A],     # 漢字（CJK Compatibility Ideographs）
    [0x2E80, 0x2FD5],     # 漢字の部首
    [0x3000, 0x303F],     # 日本語の記号
    [0xFF5F, 0xFF9F],     # カタカナ・記号
    [0xFF01, 0xFF5E],     # 全角アルファベット・記号
]

# コードポイントを取得する関数
def get_code_point(char):
    return ord(char)

# characters.txt と codepoints.txt を作成する
with open("characters.txt", "w", encoding="utf-8") as char_file, open("codepoints.txt", "w", encoding="utf-8") as codepoint_file:
    for start, end in codepoint_ranges:
        for code_point in range(start, end + 1):
            try:
                # コードポイントに対応する文字を取得
                char = chr(code_point)
                
                # 文字をcharacters.txtに書き込む
                char_file.write(char + "\n")
                
                # コードポイント（10進数）を5桁にし、codepoints.txtに書き込む
                codepoint_file.write(f"{code_point:05d}\n")
                
            except ValueError:
                continue  # 無効なコードポイントの場合はスキップ

print("characters.txt と codepoints.txt を作成しました。")
