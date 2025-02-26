import pandas as pd
import numpy as np

def generate_alignment_column(df):
        conditions = [
        df['is_op_chain'] == 'yes',
        (df['is_op_chain'] != 'yes'),
        df['is_op_chain'].isna()
        ]

        choices = [
        'OP Chain',
        'OP Stack Fork',
        'Other EVMs'
        ]


        df['alignment'] = np.select(conditions, choices, default='Unknown')
        # Add 'Legacy ' prefix to 'alignment' if 'op_based_version' contains 'Legacy'
        df['alignment'] = df.apply(lambda row: 'Legacy ' + row['alignment'] 
                                if pd.notna(row['op_based_version']) and 'Legacy' in row['op_based_version'] 
                                else row['alignment'], axis=1)

        return df