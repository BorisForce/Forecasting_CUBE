import pandas as pd 



def main(): 
    fred_md_url = "https://www.stlouisfed.org/-/media/project/frbstl/stlouisfed/research/fred-md/monthly/2025-09-md.csv?sc_lang=en&hash=5D96977D551585F408B4837C691BED67"
    fred_current_data = pd.read_csv(fred_md_url)

    for n in range(len(fred_current_data.columns[0])):
        print(n)



if __name__ == "__main__":

    main()

