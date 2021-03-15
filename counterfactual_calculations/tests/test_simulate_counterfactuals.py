"""
Test the functions in simulate_counterfactuals.py
"""
import matplotlib.pyplot as plt
import pandas as pd
import pytest
import os
import pandas as pd
from counterfactual_calculations.src.simulate_counterfactuals import (
    simulate_country_counterfactuals,
)


def test_simulate_counterfactuals():
    url_cases = "https://raw.githubusercontent.com/alan-turing-institute/CounterfactualCovid19-inputs/develop/Data/Formatted/Cases_deaths_data_europe.csv"
    df_cases = pd.read_csv(url_cases)

    url_best_knot = "https://raw.githubusercontent.com/alan-turing-institute/CounterfactualCovid19-inputs/develop/Results/knots_best.csv"
    df_best_knot = pd.read_csv(url_best_knot)

    url_summaries = "https://raw.githubusercontent.com/alan-turing-institute/CounterfactualCovid19-inputs/develop/Results/summary_eur.csv"
    df_summaries = pd.read_csv(url_summaries)

    url_possible_counterfactuals = "https://raw.githubusercontent.com/alan-turing-institute/CounterfactualCovid19-inputs/develop/Results/possible_days_counterfactual.csv"
    df_possible_counterfactuals = pd.read_csv(url_possible_counterfactuals)

    country = "United Kingdom"

    ts_daily_cases, ts_cum_daily_cases = simulate_country_counterfactuals(
        country,
        (7, 7),
        df_cases,
        df_best_knot,
        df_summaries,
        df_possible_counterfactuals,
    )
    ts_daily_cases.to_csv("covid_cases_time_series.csv")

    assert ts_daily_cases.shape[0] == 101
    assert ts_cum_daily_cases.shape[0] == 101

    assert ts_daily_cases[-1] == 256.22020291814306

    assert ts_cum_daily_cases.index[10] == "03-12-2020"
    assert ts_cum_daily_cases.index[-1] == "06-10-2020"
    assert ts_cum_daily_cases.index[0] == "03-02-2020"
