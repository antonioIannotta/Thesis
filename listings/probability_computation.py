def _compute_probability(dataset: pd.DataFrame, proxy, proxy_value, protected_column, protected_value,
                         privileged_group: bool) -> float:
    
    if privileged_group is True:
        proxy_columns_data = dataset[dataset[proxy] == proxy_value]
        return len(proxy_columns_data.loc[proxy_columns_data[protected_column] == protected_value]) / len(
            proxy_columns_data)
    else:
        proxy_columns_data = dataset[dataset[proxy] != proxy_value]
        return len(proxy_columns_data.loc[proxy_columns_data[protected_column] == protected_value]) / len(
            proxy_columns_data)