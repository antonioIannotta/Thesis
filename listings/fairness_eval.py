def fairness_evaluation(self, dataset: pd.DataFrame, protected_attributes: list, output_column_values: list,
                            output_column: str) -> str:
        """
        This method perform an evaluation of the fairness of a given dataset according to the Disparate Impact metric
        :param dataset: this is the dataset on which to be labelled as fair or unfair
        :param protected_attributes: the list of the protected attributes on which compute the disparate impact value
        :param output_column: the column of the dataset that represents the output
        :return: return 'fair' if the dataset is fair, unfair 'otherwise'
        """
        bias_analysis_dataframe = self.bias_detection(dataset, protected_attributes, output_column_values, output_column)
        return_value = 'unfair'
        for value in bias_analysis_dataframe['Disparate Impact'].values:
            if value <= 0.80 or value >= 1.25:
                return_value = 'unfair'
                break
            else:
                return_value = 'fair'

        return return_value
