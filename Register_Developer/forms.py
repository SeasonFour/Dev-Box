from django.forms import ModelForm
from crispy_forms_foundation.forms import *
from crispy_forms_foundation.layout import Layout,Field, Fieldset, Reset,SplitDateTimeField, Row, Column, ButtonHolder, Submit
from .models import Developer,Portfolio
from django.utils.translation import ugettext as _


class DeveloperRegistrationForm(ModelForm):

    class Meta:
        model = Developer
        exclude = ('date_created', 'date_updated', 'languages' ,'owner')

    def __init__(self, *args, **kwargs):
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action ='/profile/create/'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(

            Field('first_name'),
            Field('last_name'),
            Field('email_address'),
            Field('bio',css_class='bio_area'),
            Field('profile_picture'),
            Field('website_url'),

            ButtonHolder(
                Submit('submit', _('Register'),css_class='save_btn'),
                Reset('reset',_('Reset'),css_class='reset_btn')
            ),
        )
        super(DeveloperRegistrationForm, self).__init__(*args, **kwargs)
