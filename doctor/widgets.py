from django import forms
from django.utils.html import format_html
from django.utils.translation import ugettext as _

class CalendarDateWidget(forms.DateInput):
    @property
    def media(self):
        js = ["calendar.js", "DateTimeShortcuts.js"]
        return forms.Media(js=[static("CalendarWidget/js/%s" % path) for path in js])

    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'vDateField', 'size': '10'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(CalendarDateWidget, self).__init__(attrs=final_attrs, format=format)


class CalendarTimeWidget(forms.TimeInput):
    @property
    def media(self):
        js = ["calendar.js", "DateTimeShortcuts.js"]
        return forms.Media(js=[static("CalendarWidget/js/%s" % path) for path in js])

    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'vTimeField', 'size': '8'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(CalendarTimeWidget, self).__init__(attrs=final_attrs, format=format)


class CalendarSplitDateTime(forms.SplitDateTimeWidget):
    """
    A SplitDateTime Widget that has some admin-specific styling.
    """
    def __init__(self, attrs=None):
        widgets = [CalendarDateWidget, CalendarTimeWidget]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

    def format_output(self, rendered_widgets):
        return format_html('<p class="datetime">{} {}<br />{} {}</p>',
                           _(''), rendered_widgets[0],
                           _(''), rendered_widgets[1])