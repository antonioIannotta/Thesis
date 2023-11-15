def _compute_disparate_impact_for_proxy(antecedent, consequent,
                                        original_dataset: pd.DataFrame) -> float:

    proxy = antecedent.split(' = ')[0]
    proxy_value = antecedent.split(' = ')[1]
    if "." in proxy_value:
        proxy_value = float(proxy_value)
    else:
        proxy_value = int(proxy_value)

    protected_column = consequent.split(' = ')[0]
    protected_value = consequent.split(' = ')[1]
    if "." in protected_value:
        protected_value = float(protected_value)
    else:
        protected_value = int(protected_value)

    unprivileged_probability = _compute_probability(original_dataset, proxy, proxy_value, protected_column,
                                                    protected_value, False)
    privileged_probability = _compute_probability(original_dataset, proxy, proxy_value, protected_column,
                                                  protected_value, True)

    
    return unprivileged_probability / privileged_probability
    
