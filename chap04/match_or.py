drink = "ビール"

match drink:
    case "ビール" | "日本酒" | "ワイン":
        print("醸造酒です。")
    case "ウィスキー" | "ブランデー" | "ジン":
        print("蒸留酒です。")
