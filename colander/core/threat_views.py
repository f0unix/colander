from django.forms.widgets import Textarea, RadioSelect
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, UpdateView, DetailView

from colander.core.models import Threat, ThreatType
from colander.core.views import get_active_case


class ThreatCreateView(CreateView):
    model = Threat
    template_name = 'pages/collect/threats.html'
    success_url = reverse_lazy('collect_threat_create_view')
    fields = [
        'type',
        'name',
        'description',
        'source_url',
        'tlp',
        'pap'
    ]

    def get_form(self, form_class=None):
        form = super(ThreatCreateView, self).get_form(form_class)
        threat_types = ThreatType.objects.all()
        choices = [
            (t.id, mark_safe(f'<i class="nf {t.nf_icon} text-primary"></i> {t.name}'))
            for t in threat_types
        ]
        form.fields['type'].widget = RadioSelect(choices=choices)
        form.fields['description'].widget = Textarea(attrs={'rows': 2, 'cols': 20})
        return form

    def form_valid(self, form):
        active_case = get_active_case(self.request)
        if form.is_valid() and active_case:
            event = form.save(commit=False)
            event.owner = self.request.user
            event.case = active_case
            event.save()
            form.save_m2m()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['threats'] = Threat.objects.all()
        ctx['is_editing'] = False
        return ctx


class ThreatUpdateView(ThreatCreateView, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['threats'] = Threat.objects.all()
        ctx['is_editing'] = True
        return ctx


class ThreatDetailsView(DetailView):
    model = Threat
    template_name = 'threat/details.html'
