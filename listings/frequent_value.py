def _frequent_value(attribute: str, dataset: pd.DataFrame):
    unique_values = dataset[attribute].unique()
    frequency_value = [len(dataset[dataset[attribute] == x]) for x in unique_values]
    less_occurrent_value = unique_values[frequency_value.index(min(frequency_value))]
    most_occurrent_value = unique_values[frequency_value.index(max(frequency_value))]
    
    if most_occurrent_value > less_occurrent_value:
        return less_occurrent_value, most_occurrent_value
    else:
        return most_occurrent_value, less_occurrent_value
