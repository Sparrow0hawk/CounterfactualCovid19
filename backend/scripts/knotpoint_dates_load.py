"""Load COVID knot points dates data into the database"""
from time import monotonic
import pandas as pd
from dates.models import KnotDateSet
from .utils import create_code_lookup, create_country_lookup


def run():
    """Load COVID knot points dates data into the database"""
    print("Starting to load knot points data...")
    start = monotonic()

    # Source data processed by @KFArnold which serves at source to the counterfactual simulation and the total datasets
    url_best_knot = "https://raw.githubusercontent.com/KFArnold/covid-lockdown/dashboard/Output/knots_best.csv"

    # Load Dates dataframe and parse them allowing for NAT
    df_best_knot = pd.DataFrame(
        pd.read_csv(url_best_knot, parse_dates=["Knot_date_1", "Knot_date_2"])
    )

    # replace all NaT with None needed for django
    df_best_knot.Knot_date_1 = df_best_knot.Knot_date_1.replace({float("nan"): None})
    df_best_knot.Knot_date_2 = df_best_knot.Knot_date_2.replace({float("nan"): None})
    df_best_knot.Min_n_unequal = df_best_knot.Min_n_unequal.replace(
        {float("nan"): None}
    )
    df_best_knot.Growth_factor_1 = df_best_knot.Growth_factor_1.replace(
        {float("nan"): None}
    )
    df_best_knot.Growth_factor_2 = df_best_knot.Growth_factor_2.replace(
        {float("nan"): None}
    )
    df_best_knot.Growth_factor_3 = df_best_knot.Growth_factor_3.replace(
        {float("nan"): None}
    )

    # Delete all existing KnotDateSet data and regenerate the table
    KnotDateSet.objects.all().delete()  # pylint: disable=no-member

    # Add an ISO code column lookup table
    code_lookup = create_code_lookup(df_best_knot["Country"].unique())

    df_best_knot["iso_code"] = df_best_knot.apply(
        lambda row: code_lookup[row.Country], axis=1
    )

    # Create a lookup table from ISO code to Country model
    country_lookup = create_country_lookup(df_best_knot["iso_code"].unique())

    for entry in df_best_knot.itertuples():
        try:
            country = country_lookup[entry.iso_code]
            if country:
                record = KnotDateSet(
                    country=country,
                    knot_date_1=entry.Knot_date_1,
                    knot_date_2=entry.Knot_date_2,
                    n_knots=entry.N_knots,
                    growth_factor_0_1=entry.Growth_factor_1,
                    growth_factor_1_2=entry.Growth_factor_2,
                    growth_factor_2_3=entry.Growth_factor_3,
                    weight=entry.Min_n_unequal,
                )
                record.save()

        except AttributeError:
            continue

    print(f"Finished loading knot points data after {monotonic() - start:.2f} seconds")
