def categorical_to_binary(dataset: pd.DataFrame, attribute: str) -> pd.DataFrame:
    attribute_value = []
    threshold_value = (dataset[attribute].min() + dataset[attribute].max()) / 2
    for index, row in dataset.iterrows():
        if row[attribute] > threshold_value:
            attribute_value.append(1)
        else:
            attribute_value.append(0)

    dataset[attribute] = pd.Series(attribute_value)
    return dataset


def return_most_frequent_value(dataset: pd.DataFrame, attribute: str) -> int:
    unique_values = dataset[attribute].unique()
    most_frequent_value = 0
    max_frequency = 0
    for value in unique_values:
        frequency_value = len(dataset[dataset[attribute] == value])
        if frequency_value >= max_frequency:
            max_frequency = frequency_value
            most_frequent_value = value

    return most_frequent_value