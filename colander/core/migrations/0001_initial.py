# Generated by Django 3.2.15 on 2022-11-07 14:56

import colander.core.models
from django.conf import settings
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import uuid
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='ActorType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(default='', help_text='Give a meaningful name to this type of artifact.', max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='Add more details about it.', null=True)),
                ('svg_icon', models.TextField(blank=True, null=True)),
                ('nf_icon', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArtifactType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(default='', help_text='Give a meaningful name to this type of artifact.', max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='Add more details about it.', null=True)),
                ('svg_icon', models.TextField(blank=True, null=True)),
                ('nf_icon', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommonModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier.', primary_key=True, serialize=False)),
                ('description', models.TextField(default='No description', help_text='Add more details about this object.')),
                ('source_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation date of this object.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Latest modification of this object.')),
                ('tlp', models.CharField(choices=[('RED', 'RED'), ('AMBER', 'AMBER'), ('GREEN', 'GREEN'), ('WHITE', 'WHITE')], default='WHITE', help_text='Traffic Light Protocol, designed to indicate the sharing boundaries to be applied.', max_length=6, verbose_name='TLP')),
                ('pap', models.CharField(choices=[('RED', 'RED'), ('AMBER', 'AMBER'), ('GREEN', 'GREEN'), ('WHITE', 'WHITE')], default='WHITE', help_text='Permissible Actions Protocol, designed to indicate how the received information can be used.', max_length=6, verbose_name='PAP')),
                ('owner', models.ForeignKey(editable=False, help_text='Who owns this object.', on_delete=django.db.models.deletion.CASCADE, related_name='core_commonmodel_related', related_query_name='core_commonmodels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetectionRuleType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(default='', help_text='Give a meaningful name to this type of artifact.', max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='Add more details about it.', null=True)),
                ('svg_icon', models.TextField(blank=True, null=True)),
                ('nf_icon', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(default='', help_text='Give a meaningful name to this type of artifact.', max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='Add more details about it.', null=True)),
                ('svg_icon', models.TextField(blank=True, null=True)),
                ('nf_icon', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(default='', help_text='Give a meaningful name to this type of artifact.', max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='Add more details about it.', null=True)),
                ('svg_icon', models.TextField(blank=True, null=True)),
                ('nf_icon', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ObservableType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(default='', help_text='Give a meaningful name to this type of artifact.', max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='Add more details about it.', null=True)),
                ('svg_icon', models.TextField(blank=True, null=True)),
                ('nf_icon', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThreatType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(default='', help_text='Give a meaningful name to this type of artifact.', max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='Add more details about it.', null=True)),
                ('svg_icon', models.TextField(blank=True, null=True)),
                ('nf_icon', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('name', models.CharField(max_length=512)),
                ('type', models.ForeignKey(help_text='Type of this actor.', on_delete=django.db.models.deletion.CASCADE, to='core.actortype')),
            ],
            bases=('core.commonmodel',),
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('extension', models.CharField(blank=True, max_length=64, null=True)),
                ('original_name', models.CharField(blank=True, max_length=512, null=True)),
                ('stored_name', models.CharField(blank=True, max_length=512, null=True)),
                ('storage_name', models.CharField(blank=True, max_length=64, null=True)),
                ('storage_location', models.CharField(blank=True, max_length=512, null=True)),
                ('mime_type', models.CharField(blank=True, max_length=512, null=True)),
                ('detached_signature', models.TextField(blank=True, null=True)),
                ('md5', models.CharField(blank=True, max_length=65, null=True)),
                ('sha1', models.CharField(blank=True, max_length=65, null=True)),
                ('sha256', models.CharField(blank=True, max_length=65, null=True)),
                ('size_in_bytes', models.BigIntegerField(default=0)),
                ('file', models.FileField(max_length=512, upload_to=colander.core.models._get_evidence_upload_dir)),
                ('analysis_index', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Elasticsearch index storing the analysis.')),
                ('attributes', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.commonmodel', models.Model),
        ),
        migrations.CreateModel(
            name='DetectionRule',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('detection_index', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Elasticsearch index storing the detections.')),
            ],
            bases=('core.commonmodel',),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('name', models.CharField(max_length=512)),
                ('attributes', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.commonmodel', models.Model),
        ),
        migrations.CreateModel(
            name='Observable',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('value', models.CharField(max_length=512)),
                ('analysis_index', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Elasticsearch index storing the analysis.')),
                ('attributes', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
            bases=('core.commonmodel', models.Model),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier of the case.', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation date of the case.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Latest modification of the case.')),
                ('content', models.TextField(default='No description', help_text='Add more details about the case here.')),
                ('commented_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.commonmodel')),
                ('owner', models.ForeignKey(editable=False, help_text='Who owns the current case.', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ColanderTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributors', models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier of the case.', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation date of the case.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Latest modification of the case.')),
                ('name', models.CharField(default='', help_text='Give a meaningful name to the case.', max_length=512, verbose_name='name')),
                ('description', models.TextField(default='No description', help_text='Add more details about the case here.')),
                ('owner', models.ForeignKey(help_text='Who owns the current case.', on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL)),
                ('parent_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cases', to='core.case')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='core.colanderteam')),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('name', models.CharField(max_length=1024)),
                ('documentation', models.TextField(default='No documentation', help_text='Add documentation about this threat.')),
                ('type', models.ForeignKey(help_text='Type of this threat.', on_delete=django.db.models.deletion.CASCADE, to='core.threattype')),
            ],
            options={
                'ordering': ['-updated_at'],
            },
            bases=('core.commonmodel',),
        ),
        migrations.CreateModel(
            name='PiRogueDump',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('traffic_index', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Elasticsearch index storing the network traffic.')),
                ('analysis_index', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Elasticsearch index storing the analysis.')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_piroguedump_related', related_query_name='core_piroguedumps', to='core.case')),
                ('extra_files', models.ManyToManyField(blank=True, related_name='extra_files_att', to='core.Artifact')),
                ('pcap', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pirogue_dump_pcap_file', to='core.artifact')),
                ('socket_trace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pirogue_dump_socket_trace_file', to='core.artifact')),
                ('sslkeylog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pirogue_dump_ssl_keys', to='core.artifact')),
                ('target_artifact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pirogue_dump_artifact', to='core.artifact')),
                ('target_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pirogue_dump_device', to='core.device')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.commonmodel', models.Model),
        ),
        migrations.CreateModel(
            name='ObservableRelation',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('name', models.TextField(help_text='Name of this relation between two observables.')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_observablerelation_related', related_query_name='core_observablerelations', to='core.case')),
                ('observable_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relation_origins', to='core.observable')),
                ('observable_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relation_targets', to='core.observable')),
            ],
            options={
                'ordering': ['-updated_at'],
            },
            bases=('core.commonmodel', models.Model),
        ),
        migrations.AddField(
            model_name='observable',
            name='associated_threat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observables', to='core.threat'),
        ),
        migrations.AddField(
            model_name='observable',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_observable_related', related_query_name='core_observables', to='core.case'),
        ),
        migrations.AddField(
            model_name='observable',
            name='extracted_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observables', to='core.artifact'),
        ),
        migrations.AddField(
            model_name='observable',
            name='operated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observables', to='core.actor'),
        ),
        migrations.AddField(
            model_name='observable',
            name='type',
            field=models.ForeignKey(help_text='Type of this observable.', on_delete=django.db.models.deletion.CASCADE, to='core.observabletype'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commonmodel')),
                ('first_seen', models.DateTimeField(help_text='First time the event has occurred.')),
                ('last_seen', models.DateTimeField(help_text='First time the event has occurred.')),
                ('count', models.BigIntegerField(default=0)),
                ('name', models.CharField(max_length=512)),
                ('attributes', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_event_related', related_query_name='core_events', to='core.case')),
                ('detected_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.detectionrule')),
                ('extracted_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.artifact')),
                ('involved_observables', models.ManyToManyField(blank=True, null=True, to='core.Observable')),
                ('observed_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.device')),
                ('type', models.ForeignKey(help_text='Type of this event.', on_delete=django.db.models.deletion.CASCADE, to='core.eventtype')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.commonmodel', models.Model),
        ),
        migrations.AddField(
            model_name='device',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_device_related', related_query_name='core_devices', to='core.case'),
        ),
        migrations.AddField(
            model_name='device',
            name='operated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='core.actor'),
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.ForeignKey(help_text='Type of this device.', on_delete=django.db.models.deletion.CASCADE, to='core.devicetype'),
        ),
        migrations.AddField(
            model_name='detectionrule',
            name='detected_observables',
            field=models.ManyToManyField(blank=True, null=True, to='core.Observable'),
        ),
        migrations.AddField(
            model_name='detectionrule',
            name='type',
            field=models.ForeignKey(help_text='Type of this detection rule.', on_delete=django.db.models.deletion.CASCADE, to='core.detectionruletype'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_artifact_related', related_query_name='core_artifacts', to='core.case'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='type',
            field=models.ForeignKey(help_text='Type of this artifact.', on_delete=django.db.models.deletion.CASCADE, to='core.artifacttype'),
        ),
    ]
