import pickle
import pandas as pd
from flask import Flask, Response, request
from healthinsurance import HealthInsurance

path = 'C:/Users/fmath/repos/comunidade-ds/health-insurance-cross-sell/'
# Carregar o modelo
model = pickle.load(open(path + 'models/model_insurance_cross_sell.pkl', 'rb'))

# Iniciando API
app = Flask( __name__ )

@app.route('/healthinsurance/predict', methods=['POST'])
def health_insurance_predict():
    test_json = request.get_json()

    if test_json: # existe dados
        if isinstance(test_json, dict): # Exemplo unico
            test_raw = pd.DataFrame(test_json, index=[0])

        else: # Vários exemplos
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # Instanciando Health Insurance Class
        pipeline = HealthInsurance()

        # Feature engineering
        df1 = pipeline.feature_engineering(test_raw)

        # Preparação dos dados
        df2 = pipeline.data_preparation(df1)

        # Predição
        df_response = pipeline.get_prediction(model, test_raw, df2)

        return df_response
    
    else:
        return Response( '{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('127.0.0.1')