with open('libaries.py', 'r') as file:
    libaries = file.read()
exec(libaries)

def explore_data_columns(df, nrows, ncols, plot_type='histplot', figsize=(12, 8)):
    fig, axis = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

    for i, column in enumerate(df.columns):
        plot = getattr(sns, plot_type)
        plot(df[column], ax=axis[i//ncols][i%ncols], color='grey')
        axis[i//ncols][i%ncols].set_xlabel(column)

    plt.tight_layout()

def _get_outlier_range(data):
    q1 = np.quantile(data, q=.25)
    q3 = np.quantile(data, q=.75)
    iqr = q3 - q1
    return (q1 - (1.5 * iqr), q3 + 1.5 * iqr)

def exclude_outliers(df):
    df_copy = df.copy()
    for column in df_copy.columns:
        outlier_range = _get_outlier_range(df_copy[column])
        df_copy = df_copy[(df_copy[column] >= outlier_range[0]) & (df_copy[column] <= outlier_range[1])]
    return df_copy

