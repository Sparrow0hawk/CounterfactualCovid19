"""Serializers for Django dates app"""
from rest_framework import serializers
from .models import ModelDateRange, KnotDateSet, PossibleDateSet


class KnotDateSetSerializer(serializers.ModelSerializer):
    """Serializer for KnotDateSetView"""

    iso_code = serializers.PrimaryKeyRelatedField(source="country", read_only=True)

    class Meta:
        """Metaclass for output fields"""

        model = KnotDateSet
        fields = (
            "iso_code",
            "knot_date_1",
            "knot_date_2",
            "n_knots",
            "growth_factor_0_1",
            "growth_factor_1_2",
            "growth_factor_2_3",
            "weight",
        )


class ModelDateRangeSerializer(serializers.ModelSerializer):
    """Serializer for ModelDateRangeView"""

    iso_code = serializers.PrimaryKeyRelatedField(source="country", read_only=True)

    class Meta:
        """Metaclass for output fields"""

        model = ModelDateRange
        fields = (
            "iso_code",
            "initial_date",
            "maximum_date",
            "first_restrictions_date",
            "lockdown_date",
        )


class PossibleLockdownDateSetSerializer(serializers.ModelSerializer):
    """Serializer for PossibleLockdownDateSetView"""

    iso_code = serializers.SerializerMethodField()
    possible_lockdown_dates = serializers.SerializerMethodField()

    class Meta:
        """Metaclass for output fields"""

        model = PossibleDateSet
        fields = (
            "iso_code",
            "possible_lockdown_dates",
        )

    def get_iso_code(self, datadict):  # pylint: disable=no-self-use
        """Getter for iso_code field"""
        return datadict["country__iso_code"]

    def get_possible_lockdown_dates(self, datadict):  # pylint: disable=no-self-use
        """Getter for possible_lockdown_dates field"""
        return datadict["lockdown_dates"]


class PossibleRestrictionsDateSetSerializer(serializers.ModelSerializer):
    """Serializer for PossibleRestrictionsDateSetView"""

    iso_code = serializers.SerializerMethodField()
    possible_restrictions_dates = serializers.SerializerMethodField()

    class Meta:
        """Metaclass for output fields"""

        model = PossibleDateSet
        fields = (
            "iso_code",
            "possible_restrictions_dates",
        )

    def get_iso_code(self, datadict):  # pylint: disable=no-self-use
        """Getter for iso_code field"""
        return datadict["country__iso_code"]

    def get_possible_restrictions_dates(self, datadict):  # pylint: disable=no-self-use
        """Getter for possible_restrictions_dates field"""
        return datadict["restrictions_dates"]
