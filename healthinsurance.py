import pickle
import pandas as pd

class HealthInsurance ():
    def __init__ (self):
        self.home_path = 'C:/Users/fmath/repos/comunidade-ds/health-insurance-cross-sell/'
        self.age_scaler                  = pickle.load(open(self.home_path + 'parameter/age_scaler.pkl', 'rb'))
        self.gender_scaler               = pickle.load(open(self.home_path + 'parameter/gender_scaler.pkl', 'rb'))
        self.vintage_scaler              = pickle.load(open(self.home_path + 'parameter/vintage_scaler.pkl', 'rb'))
        self.region_code_scaler          = pickle.load(open(self.home_path + 'parameter/region_code_scaler.pkl', 'rb'))
        self.annual_premmium_scaler      = pickle.load(open(self.home_path + 'parameter/annual_premmium_scaler.pkl', 'rb'))
        self.policy_sales_channel_scaler = pickle.load(open(self.home_path + 'parameter/policy_sales_channel_scaler.pkl', 'rb'))

    def feature_engineering (self, data):
        data = data.assign(
            gender         = lambda x: x['gender'].str.lower(),
            vehicle_age    = lambda x: x['vehicle_age'].map({
                '1-2 Year': 'between_1_2_years',
                '< 1 Year': 'below_1_year',
                '> 2 Years': 'over_2_years'
            }),
            vehicle_damage = lambda x: x['vehicle_damage'].map({'Yes': 1, 'No': 0})
        )

        return data


    def data_preparation (self, data):
        # annual_premium
        data['annual_premium'] = self.annual_premmium_scaler.transform(data[['annual_premium']].values)

        # age
        data['age'] = self.age_scaler.transform(data[['age']].values)

        # vintage
        data['vintage'] = self.vintage_scaler.transform(data[['vintage']].values)

        # gender - One Hot Encoding
        data['gender'] = data['gender'].map(self.gender_scaler)

        # region_code - Frequency Encoding / Target Encoding
        data['region_code'] = data['region_code'].map(self.region_code_scaler)

        # vehicle_age - One Hot Encoding / Ordinal Encoding / Frequency Encoding
        data = pd.get_dummies(data, prefix='vehicle_age', columns=['vehicle_age'])

        # policy_sales_channel - Target Encoding / Frequency Encoding
        data['policy_sales_channel'] = data['policy_sales_channel'].map(self.policy_sales_channel_scaler)

        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage',
                            'policy_sales_channel', 'previously_insured']

        return data[cols_selected].fillna(0)
        

    def get_prediction (self, model, original_data, test_data):
        # Predição do modelo
        pred = model.predict_proba(test_data)

        # Inserindo predição nos dados originais
        original_data['score'] = pred[:,1]

        return original_data.to_json(orient='records', date_format='iso')