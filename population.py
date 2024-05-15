import pickle
import pandas as pd

model_pkl_file = 'population_prediction_model.pkl'

# load model from pickle file
with open(model_pkl_file, 'rb') as file:  
    reg = pickle.load(file)

def predict_population(input, flag = 'value' ):

    if flag == 'value':
        year = [[input]]
        # evaluate model 
        return reg.predict(year)[0]
    elif flag == 'array':
        return reg.predict(input)


if __name__ == "__main__":

    # predict_data = predict_population(2025)

    #Add a column against year in the dataframe
    predict_data = pd.read_csv("Predict_Population.csv")
    predicted = predict_population(predict_data, flag = 'array')
    predict_data['predictions'] = predicted

    # check results
    print(predict_data) 