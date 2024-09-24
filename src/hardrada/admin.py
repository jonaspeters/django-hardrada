from django.forms import widgets

widgets.Input.template_name = 'hardrada/forms/widgets/input.html'

# Select inputs
widgets.Select.template_name = 'hardrada/forms/widgets/select.html'
widgets.Select.option_template_name = 'hardrada/forms/widgets/select_option.html'
