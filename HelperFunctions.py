import warnings
import pandas   as pd
import seaborn  as sns

from matplotlib             import pyplot as plt


def jupyter_settings():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    plt.style.use( 'bmh' )
    plt.rcParams['figure.figsize'] = [25, 12]
    plt.rcParams['font.size'] = 24
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    pd.options.display.float_format = '{:.2f}'.format 
    pd.set_option( 'display.expand_frame_repr', False )
    sns.set()