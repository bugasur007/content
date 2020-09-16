import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *

mitre_id = demisto.get(demisto.args()['indicator'], 'CustomFields.mitrevalue') or ''

demisto.results(
    {'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': f'# {mitre_id}'})
