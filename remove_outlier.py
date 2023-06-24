def remove_outlires(df, col, k):
    mean = df[col].mean()
    sd = df[col].std()
    final_list = [x for x in df[col] if (x > (mean - k*sd) and x < (mean + k*sd))]
    a = df.shape
    df = df[df[col].isin(final_list)]
    b = df.shape
    print(f'Total outlires removed are {a[0] - b[0]}')
    return df