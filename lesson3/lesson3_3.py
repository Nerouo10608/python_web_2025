import tools

def main():
    try:
        data = tools.download_youbike_data()
        print(data)
    except Exception as e:
        print(f"發生錯誤\n{e}")

if __name__ == "__main__":
    main()