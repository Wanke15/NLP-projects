import os
import json

from flask import Markup


TPL_ENTS = """
<div class="entities" style="line-height: 2.5">
    {content} <br><br>
</div>
"""

TPL_ENT = """
<mark class="entity" style="background: {bg}; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em; box-decoration-break: clone; -webkit-box-decoration-break: clone">
    {text}
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem" data-original-title='{conflicts}'  data-placement='top' data-trigger='hover' class='popovers'>{label}</span>
</mark>
"""


def render_entities_content(text, ents):
    color_set = {
        '#7aecec', '#9cc9cc', '#aa9cfc', '#bfe1d9', '#bfeeb7', '#c887fb',
        '#e4e7d2', '#f0d0ff', '#feca74', '#ff8197', '#ff9561', '#ffeb80'
    }
    colors = {}
    entities, original_entities = _get_entities(ents)
    for entity in entities:
        if entity['type'] not in colors:
            colors[entity['type']] = color_set.pop()
    markup = _render_entities(text, entities, original_entities, colors)
    return Markup(markup)


def _is_entity_same(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i]['type'] != b[i]['type'] or a[i]['startIndex'] != b[i]['startIndex'] or a[i]['endIndex'] != b[i]['endIndex']:
            return False
    return True


def _get_entities(res):
    all_entities = sorted(res["entities"], key=lambda x: x.get("startIndex"))
    entities = []
    for entity in all_entities:
        if not _conflict(entities, entity):
            entities.append(entity)
    entities.sort(key=lambda x: x["startIndex"])
    return entities, all_entities


def _get_conflicts(entities, entity):
    all_conflicts = []
    a_start = entity["startIndex"]
    a_end = entity["endIndex"]
    for idx, ent in enumerate(entities):
        if ent == entity:
            continue
        b_start = ent["startIndex"]
        b_end = ent["endIndex"]
        if a_start <= b_start <= a_end or a_start <= b_end <= a_end or b_start <= a_start <= b_end or b_start <= a_end <= b_end:
            all_conflicts.append(ent['entity']+'->'+ent['type'])
    return all_conflicts


def _conflict(entities, entity):
    a_start = entity["startIndex"]
    a_end = entity["endIndex"]
    for ent in entities:
        b_start = ent["startIndex"]
        b_end = ent["endIndex"]
        if a_start <= b_start <= a_end or a_start <= b_end <= a_end or b_start <= a_start <= b_end or b_start <= a_end <= b_end:
            return True
    return False


def _render_entities(text, spans, original_ents, colors):
    markup = ''
    offset = 0
    for span in spans:
        label = span['type']
        start = span['startIndex']
        end = span['endIndex'] + 1
        entity = text[start:end]
        markup += text[offset:start]
        color = colors.get(label)
        all_conflicts = _get_conflicts(original_ents, span)
        if not all_conflicts:
            conf_str = ''
        else:
            conf_str = '; '.join(all_conflicts)
        markup += TPL_ENT.format(label=label, text=entity, conflicts=conf_str, bg=color)
        offset = end
    markup += text[offset:]
    markup = TPL_ENTS.format(content=markup)
    return markup
