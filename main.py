import pandas as pd

if __name__ == '__main__':
    # array = list()
    # for i in range(0, 1001):
    #     with open(f'./temp/{i}.txt') as f:
    #         # json_data = json.load(f)
    #         dataframe = pd.read_json(f)
    #         array.append(dataframe)
    result = pd.read_csv(r"data_game.csv")
    result.drop("Unnamed: 0", 1, inplace=True)
    result.drop("Unnamed: 0.1", 1, inplace=True)
    result.drop("Unnamed: 0.1.1", 1, inplace=True)
    result.drop("Unnamed: 0.1.1.1", 1, inplace=True)
    # result.reset_index()
    # result = pd.concat(array)
    result.to_csv(r"data_game.csv", index=True)
