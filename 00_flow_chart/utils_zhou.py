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
    print('共有：[{0}]条样本，特征数为：[{1}]，其中有[{2}]个特征是number'.format(
            data.shape[0], data.shape[1], data_tmp.shape[1]))
    return show_describe(data_tmp)

def show_object_describe(data):
    data_tmp = data.select_dtypes(include = ["object"])
    print('共有：[{0}]条样本，特征数为：[{1}]，其中有[{2}]个特征是object'.format(
            data.shape[0], data.shape[1], data_tmp.shape[1]))
    return show_describe(data_tmp) 

    