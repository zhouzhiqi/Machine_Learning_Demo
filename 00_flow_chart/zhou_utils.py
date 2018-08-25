
def show_describe(data):
    describe = data.describe().T
    for c in data.columns:
        describe.loc[c,'dif_vals'] = len(data[c].unique())
        describe.loc[c,'dtype'] = data[c].dtype
        describe.loc[c,'num_null'] = data[c].isnull().sum()
    for c in ['count','dif_vals','num_null']:
        describe[c] = describe[c].astype(np.int64)
    return describe
        
def show_number_describe(data):
    data_tmp = data.select_dtypes(include = ["number"])
    show_describe(data_tmp)

def show_object_describe(data):
    data_tmp = data.select_dtypes(include = ["object"])
    show_describe(data_tmp)

