from django import forms
from django.utils.translation import gettext as _

from utilities.forms import BootstrapMixin, DateTimePicker

__all__ = (
    'ReportForm',
)


class ReportForm(BootstrapMixin, forms.Form):
    schedule_at = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(),
        label=_("Schedule at"),
        help_text=_("Schedule execution of report to a set time"),
    )
    interval = forms.IntegerField(
        required=False,
        label=_("Recurs every"),
        help_text=_("Interval at which this report is re-run (in minutes)")
    )
