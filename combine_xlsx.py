import pandas as pd
def combine_xlsx(files:list[str]):
    df = pd.concat([pd.read_excel(f) for f in files], ignore_index=True)
    df.to_excel("combined.xlsx", index=False)

def main():
    files = []
    for i in range(1, 10):
        files.append(f"{i}.xlsx")
    combine_xlsx(files)

if __name__ == "__main__":
    main()